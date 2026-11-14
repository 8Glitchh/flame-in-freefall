import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

import numpy as np
import pymupdf
from sentence_transformers import SentenceTransformer

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
TESTS_CSV = DATA / "psi_tests_clean.csv"
CACHE = HERE / ".cache"
MAX_TOKENS = 220
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RRF_K = 60
KEYWORD_WEIGHT = 0.5
MEANING_WEIGHT = 0.5

EXCLUDE = re.compile(r"MergeResult|Planned_Test_Matrix|Image_Directory_Nomenclature|DataOrganization|"
                     r"As_Run_Test_Matrix|BASS-II_Test\.Matrices", re.I)
FINDING_FIELDS = ("finding", "evidence", "safety_implication", "fuel_material", "oxygen_raw", "pressure_raw",
                  "flow_raw", "gravity", "spread_rate_raw", "peak_heat_release_rate_raw", "time_to_detection_raw",
                  "other_measurements", "sensors", "variables", "earth_application", "partial_g_applicability")

COUNTRIES = r"(USA|France|Germany|Japan|Russia|Netherlands|Slovenia|Sweden|Italy|Canada|UK|Belgium|Spain)"
AFFILIATION = re.compile(rf",\s*{COUNTRIES}\b")
AUTHOR_LIST = re.compile(r"[a-z]\d{1,2},")
SKIP_COLUMNS = {"record_id", "experiment_key", "flags", "psi_id", "experiment", "test_id", "test_id_basis",
                "gravity", "source_file", "source_row", "row_kind", "duplicate_of_source_row", "source_page",
                "source_table", "source_url", "reported_na_fields", "workbook_join", "workbook_file",
                "workbook_sheet", "workbook_row"}
UNITS = [("_pct", " (%)"), ("_kpa", " (kPa)"), ("_mm_s", " (mm/s)"), ("_cm_s", " (cm/s)"), ("_mg_s", " (mg/s)"),
         ("_mg_m3", " (mg/m3)"), ("_ppm", " (ppm)"), ("_mmhg", " (mmHg)"), ("_mbar", " (mbar)"), ("_mm", " (mm)"),
         ("_atm", " (atm)"), ("_w", " (W)"), ("_s", " (s)")]
STOP = set("a an the of to in on for and or with by at from as is are was were be been it its this that "
           "what which who how why when where does do did can".split())


def n_tokens(text):
    return int(len(text.split()) / 0.75) + 1


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)
    return [p.strip() for p in parts if p.strip()]


def make_chunk(text, document, pages=()):
    return {"text": text, "document": document, "pages": sorted(set(pages))}


def pack(sentences, document, prefix=""):
    chunks, cur = [], []
    for s, page in sentences:
        current_text = " ".join(x for x, _ in cur)
        if cur and n_tokens(current_text + " " + s) > MAX_TOKENS:
            chunks.append(make_chunk(prefix + current_text, document, [p for _, p in cur if p]))
            cur = cur[-1:]
        cur.append((s, page))
    if cur:
        chunks.append(make_chunk(prefix + " ".join(x for x, _ in cur), document, [p for _, p in cur if p]))
    return chunks


def clean_value(value):
    if value is None:
        return ""
    if isinstance(value, (datetime, date)):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, float):
        return f"{value:.6g}"
    return re.sub(r"\s+", " ", str(value)).strip()


def read_pdf(path):
    with pymupdf.open(path) as doc:
        return [(i + 1, page.get_text()) for i, page in enumerate(doc)]


def line_key(line):
    return re.sub(r"\d+", "#", line.strip().lower())


def repeated_lines(pages):
    counts = {}
    for _, text in pages:
        for key in {line_key(l) for l in text.splitlines() if l.strip()}:
            counts[key] = counts.get(key, 0) + 1
    limit = max(3, 0.4 * len(pages))
    return {k for k, c in counts.items() if c >= limit}


def clean_lines(text, repeated):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line_key(line) in repeated:
            continue
        if line == "References":
            lines.append(line)
            continue
        if AFFILIATION.search(line) or len(AUTHOR_LIST.findall(line)) >= 2:
            continue
        if len(line) < 30 and not line.endswith((".", ":", ";", ",")):
            continue
        lines.append(line)
    return lines


def load_pdf(path):
    pages = read_pdf(path)
    repeated = repeated_lines(pages)
    sentences = []
    for page_no, text in pages:
        lines = clean_lines(text, repeated)
        stop = "References" in lines
        if stop:
            lines = lines[:lines.index("References")]
        joined = " ".join(lines)
        joined = re.sub(r"([a-z])- ([a-z])", r"\1\2", joined)
        for s in split_sentences(joined):
            sentences.append((s, page_no))
        if stop:
            break
    return pack(sentences, path.name)


def load_markdown(path):
    sentences = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip("#-* ").strip()
        if line:
            sentences += [(s, None) for s in split_sentences(line)]
    return pack(sentences, path.name)


def load_docx(path):
    import docx
    document = docx.Document(str(path))
    sentences = []
    for paragraph in document.paragraphs:
        text = clean_value(paragraph.text)
        if text:
            sentences += [(s, None) for s in split_sentences(text)]
    chunks = pack(sentences, path.name)
    for table in document.tables:
        rows = [[clean_value(cell.text) for cell in row.cells] for row in table.rows]
        if len(rows) < 2:
            continue
        header = rows[0]
        for row in rows[1:]:
            facts = "; ".join(f"{h}: {v}" for h, v in zip(header, row) if h and v)
            if facts:
                chunks.append(make_chunk(facts + ".", path.name))
    return chunks


def load_xlsx(path):
    import openpyxl
    label = path.stem.split("_")[1] if path.name.startswith("PSI-") else path.stem
    book = openpyxl.load_workbook(path, read_only=True, data_only=True)
    chunks = []
    for sheet in book.worksheets:
        if re.search(r"camera|graph", sheet.title, re.I):
            continue
        rows = [[clean_value(v) for v in row] for row in sheet.iter_rows(values_only=True)]
        rows = [r for r in rows if any(r)]
        if len(rows) < 2:
            continue
        header = rows[0]
        for row in rows[1:]:
            facts = "; ".join(f"{h}: {v}" for h, v in zip(header, row) if h and v)
            if facts.count(":") >= 2:
                chunks.append(make_chunk(f"{label} {sheet.title}: {facts}.", path.name))
    book.close()
    return chunks


def pretty(column):
    column = column.replace("_per_", "_")
    for end, unit in UNITS:
        if column.endswith(end):
            return column[:-len(end)].replace("_", " ") + unit
    return column.replace("_", " ")


def useful_columns(row):
    return [c for c in row if c not in SKIP_COLUMNS and not c.endswith(("_approx", "_raw"))]


def row_text(row, label):
    facts = []
    for column in useful_columns(row):
        value = row[column]
        if not value:
            continue
        if row.get(column + "_approx") == "True":
            value = "~" + value
        facts.append(f"{pretty(column)}: {value}")
    text = f"{label} test {row['test_id']}. Gravity: {row['gravity'] or 'not stated'}. " + "; ".join(facts) + "."
    if row["flags"]:
        text += f" Data quality flags: {row['flags'].replace(';', ', ')}."
    return text


def to_number(value):
    try:
        return float(value)
    except ValueError:
        return None


def summary_text(rows, label):
    parts = [f"{label} experiment table: {len(rows)} tests."]
    for column in useful_columns(rows[0]):
        values = [r[column] for r in rows if r[column]]
        if not values:
            continue
        numbers = [to_number(v) for v in values]
        if None not in numbers:
            parts.append(f"{pretty(column)}: from {min(numbers):g} to {max(numbers):g}.")
            continue
        counts = Counter(values)
        if len(counts) <= 25 and counts.most_common(1)[0][1] > 1:
            listed = ", ".join(f"{v} ({n})" for v, n in counts.most_common(10))
            parts.append(f"{pretty(column)}: {listed}.")
    return " ".join(parts)


def load_tests(path):
    groups = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["duplicate_of_source_row"] or row["row_kind"] != "data":
                continue
            groups.setdefault(row["experiment_key"], []).append(row)

    chunks = []
    for label, rows in groups.items():
        for row in rows:
            page = row["source_page"]
            chunks.append(make_chunk(row_text(row, label), Path(row["source_file"]).name,
                                     [int(page)] if page.isdigit() else []))
        chunks.append(make_chunk(summary_text(rows, label), "psi_tests_clean.csv"))
    return chunks


def load_investigations(path):
    chunks = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = f"{row['acronym'] + ' – ' if row['acronym'] else ''}{row['title']} ({row['psi_id']})"
            overview = (f"{name}. Type: {row['type']}. Area: {row['sub_area'] or row['research_area']}. "
                        f"Dates: {row['start'] or '?'} to {row['end'] or '?'}. DOI: {row['doi']}.")
            chunks.append(make_chunk(overview, path.name))
            for field in ("objective", "approach", "hypothesis", "impacts"):
                if row[field]:
                    sentences = [(s, None) for s in split_sentences(row[field])]
                    chunks += pack(sentences, path.name, f"{name} – {field}: ")
    return chunks


def load_findings(path):
    chunks = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("quote_found", "true").lower() != "true":
                continue
            facts = "; ".join(f"{k.replace('_raw', '').replace('_', ' ')}: {row[k]}" for k in FINDING_FIELDS if row.get(k))
            page = row.get("page", "")
            chunks.append(make_chunk(f"Finding ({row.get('investigation', '')}): {facts}.",
                                     row.get("document_name", path.name),
                                     [int(page)] if page.isdigit() else []))
    return chunks


def load_file(path):
    if path == TESTS_CSV:
        return load_tests(path)
    if path.name == "investigations.csv":
        return load_investigations(path)
    if path.parent.name == "findings" and path.suffix == ".csv":
        return load_findings(path)
    if path.name == "background.md":
        return load_markdown(path)
    if "papers" in path.parts:
        if path.suffix == ".pdf":
            return load_pdf(path)
        if path.suffix == ".docx":
            return load_docx(path)
        if path.suffix == ".xlsx":
            return load_xlsx(path)
    return []


def load_all(verbose=False):
    chunks = []
    for path in sorted(DATA.rglob("*")):
        if not path.is_file() or EXCLUDE.search(path.name):
            continue
        try:
            loaded = load_file(path)
        except Exception as e:
            print(f"skipped {path.name}: {e}")
            continue
        chunks += loaded
        if verbose and loaded:
            print(f"{len(loaded):>5}  {path.relative_to(DATA)}")
    return chunks


def stem(w):
    if len(w) > 4 and not w[0].isdigit():
        if w.endswith("ies"):
            return w[:-3] + "y"
        if w.endswith("ing") and len(w) > 6:
            return w[:-3]
        if w.endswith("ed") and len(w) > 5:
            return w[:-2]
        if w.endswith("s") and not w.endswith(("ss", "us", "is")):
            return w[:-1]
    return w


def tokens(text):
    words = re.findall(r"[a-z0-9]+(?:[.\-/][a-z0-9]+)*", text.lower())
    return [stem(w) for w in words if w not in STOP]


class BM25:
    def __init__(self, chunks, k1=1.5, b=0.75):
        self.chunks = chunks
        self.docs = [Counter(tokens(c["text"])) for c in chunks]
        self.lengths = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.lengths) / len(self.lengths)
        n = len(self.docs)
        df = Counter(w for d in self.docs for w in d)
        self.idf = {w: math.log(1 + (n - f + 0.5) / (f + 0.5)) for w, f in df.items()}
        self.k1, self.b = k1, b

    def scores(self, question):
        q = set(tokens(question))
        out = []
        for d, length in zip(self.docs, self.lengths):
            s = 0.0
            norm = self.k1 * (1 - self.b + self.b * length / self.avg)
            for w in q:
                tf = d.get(w, 0)
                if tf:
                    s += self.idf[w] * tf * (self.k1 + 1) / (tf + norm)
            out.append(s)
        return out


class Dense:
    def __init__(self, chunks):
        self.model = SentenceTransformer(EMBED_MODEL)
        texts = [c["text"] for c in chunks]
        key = hashlib.md5((EMBED_MODEL + "\n".join(texts)).encode("utf-8")).hexdigest()[:16]
        path = CACHE / f"vectors-{key}.npy"
        if path.exists():
            self.vectors = np.load(path)
        else:
            print(f"Embedding {len(texts)} passages (first run only, then cached)...")
            self.vectors = self.model.encode(texts, normalize_embeddings=True, batch_size=64, show_progress_bar=True)
            CACHE.mkdir(exist_ok=True)
            np.save(path, self.vectors)

    def scores(self, question):
        q = self.model.encode(QUERY_PREFIX + question, normalize_embeddings=True)
        return self.vectors @ q


class Index:
    def __init__(self, chunks):
        self.chunks = chunks
        self.bm25 = BM25(chunks)
        self.dense = Dense(chunks)


def ranks(scores, only_positive=False):
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return {i: r for r, i in enumerate(order, 1) if scores[i] > 0 or not only_positive}


INDEX = None


def get_index():
    global INDEX
    if INDEX is None:
        INDEX = Index(load_all())
    return INDEX


def search(question, k=6):
    index = get_index()
    keyword = ranks(index.bm25.scores(question), only_positive=True)
    meaning = ranks(index.dense.scores(question))
    fused = {}
    for ranking, weight in ((keyword, KEYWORD_WEIGHT), (meaning, MEANING_WEIGHT)):
        for i, r in ranking.items():
            fused[i] = fused.get(i, 0) + weight / (RRF_K + r)
    order = sorted(fused, key=lambda i: -fused[i])
    return [index.chunks[i] for i in order[:k]]


def evaluate(path=HERE / "eval_questions.json"):
    qs = json.load(open(path, encoding="utf-8"))
    first = top = 0
    for item in qs:
        if item.get("expect") == "not_found":
            continue
        hits = search(item["q"])
        rank = next((i + 1 for i, c in enumerate(hits)
                     if any(a.lower() in c["text"].lower() for a in item["any"])), 0)
        first += rank == 1
        top += rank > 0
        print(f"{rank or 'MISS':>4}  {item['q']}")
    print(f"\nfirst: {first}   in top 6: {top}")


if __name__ == "__main__":
    if sys.argv[1:] == ["chunks"]:
        chunks = load_all(verbose=True)
        print(len(chunks), "chunks")
    elif sys.argv[1:2] == ["ask"]:
        for i, c in enumerate(search(sys.argv[2]), 1):
            print(f"[{i}] {c['document']} p.{c['pages']} | {c['text'][:200]}\n")
    else:
        evaluate()