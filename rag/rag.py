import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import pymupdf
from sentence_transformers import SentenceTransformer

HERE = Path(__file__).resolve().parent
PDF = HERE.parent / "data" / "papers" / "ICES-2026-577.pdf"
TESTS_CSV = HERE.parent / "data" / "psi_tests_clean.csv"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RRF_K = 60
KEYWORD_WEIGHT = 0.5
MEANING_WEIGHT = 0.5

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


def read_pdf(path):
    doc = pymupdf.open(path)
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
        if AFFILIATION.search(line) or len(AUTHOR_LIST.findall(line)) >= 2:
            continue
        if len(line) < 30 and not line.endswith((".", ":", ";", ",")):
            continue
        lines.append(line)
    return lines


def make_chunk(sentences, document):
    return {"text": " ".join(s for s, _ in sentences),
            "document": document,
            "pages": sorted({p for _, p in sentences})}


def load_pdf(path, max_tokens=220):
    name = Path(path).name
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

    chunks, cur = [], []
    for s, page in sentences:
        current_text = " ".join(x for x, _ in cur)
        if cur and n_tokens(current_text + " " + s) > max_tokens:
            chunks.append(make_chunk(cur, name))
            cur = cur[-1:]
        cur.append((s, page))
    if cur:
        chunks.append(make_chunk(cur, name))
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
            chunks.append({"text": row_text(row, label),
                           "document": Path(row["source_file"]).name,
                           "pages": [int(page)] if page.isdigit() else []})
        chunks.append({"text": summary_text(rows, label),
                       "document": "psi_tests_clean.csv",
                       "pages": []})
    return chunks


def load_all():
    return load_pdf(PDF) + load_tests(TESTS_CSV)


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
        self.vectors = self.model.encode(texts, normalize_embeddings=True)

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
        chunks = load_all()
        print(len(chunks), "chunks\n")
        for c in chunks[:5]:
            print("pages", c["pages"], "|", c["text"][:250], "\n")
    elif sys.argv[1:2] == ["ask"]:
        for i, c in enumerate(search(sys.argv[2]), 1):
            print(f"[{i}] {c['document']} p.{c['pages']} | {c['text'][:200]}\n")
    else:
        evaluate()