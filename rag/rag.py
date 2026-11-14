import csv
import hashlib
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime
from pathlib import Path

import numpy as np
import pymupdf
from sentence_transformers import CrossEncoder, SentenceTransformer

THINKING_LEVELS = ("low", "medium", "high")

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
TESTS_CSV = DATA / "psi_tests_clean.csv"
CACHE = HERE / ".cache"
MAX_TOKENS = 220
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RRF_K = 60
KEYWORD_WEIGHT = 0.5
MEANING_WEIGHT = 0.5
CANDIDATES = 40
EXPERIMENT_BOOST = 0.02
OTHER_EXPERIMENT_PENALTY = 0.005
TEST_ID_BOOST = 0.02
SUMMARY_BOOST = 0.03
SPEC_PENALTY = 0.006
RERANK_TOP = 30
RERANK_BONUS = 2.0
MAX_PER_DOCUMENT = 2
MIN_COVERAGE = 0.4
MIN_COVERAGE_WITH_EXPERIMENT = 0.2
NOT_FOUND = "The documents I have don't answer this."
SYSTEM = """You are a NASA microgravity-combustion research assistant for fire-safety engineers and students.
Rules:
1. Use ONLY the numbered passages. Never add outside knowledge, even if you know it.
2. Cite every factual sentence with passage numbers like [1] or [2][4].
3. Copy numbers and units exactly as written. Say which experiment or test each number comes from.
4. Keep microgravity (0 g, low-g, ISS, Cygnus) results separate from normal-gravity (1 g) results. Never present a
   Moon or Mars (partial gravity) value as measured: at most say it should lie between the 0 g and 1 g results.
5. If the passages don't answer the question, reply exactly: "The documents I have don't answer this."
   If they answer only part of it, answer that part and say what is missing.
6. Be concise: a direct answer first (1 to 3 sentences), then short supporting points if useful."""

SPEC_FILE = re.compile(r"SRD|ISRD|SORD|SCR|Requirements|Operations_Manual|DoD|DLD|Concept_Description|"
                       r"data_file_description", re.I)
EXCLUDE = re.compile(r"MergeResult|Planned_Test_Matrix|Image_Directory_Nomenclature|DataOrganization|"
                     r"As_Run_Test_Matrix|BASS-II_Test\.Matrices", re.I)
TABLE_INTENT = re.compile(r"\b(how many|which tests?|what tests?|list|range|conditions?|what (fuels?|materials?|pressures?)|"
                          r"maximum|minimum|highest|lowest|average|tested|test matrix)\b", re.I)
SPEC_INTENT = re.compile(r"\b(requirement|hardware|instrument|camera|sensor|rack|chamber|burner|design|"
                         r"operat|procedure|igniter|apparatus|diagnostic|measur)", re.I)
TEST_ID = re.compile(r"\b((?:I|II|III|IV|V|VI)-\d+|\d-\d+|S\d+|test (?:no\.? )?\d+|#\s?\d+)\b", re.I)
SYNONYMS = {"heat release rate": "hrr", "hrr": "heat release rate", "o2": "oxygen", "oxygen": "o2",
            "co2": "carbon dioxide", "carbon monoxide": "co", "pmma": "acrylic", "sibal": "cotton fiberglass",
            "microgravity": "micro-g low-gravity", "extinction diameter": "dext", "extinguish": "extinction",
            "spread": "propagation", "smoke": "aerosol particulate", "pressure": "kpa atm mbar",
            "fast": "rate speed", "hot": "temperature", "fuel": "material sample"}
DOMAIN = re.compile(r"(fire|flam|burn|combust|smoke|soot|oxyg|\bo2\b|gravit|spacecraft|\biss\b|astronaut|fuel|droplet|"
                    r"ignit|extin|suppress|pressure|pmma|cotton|sibal|hazard|safety|heat|\bco2?\b|nasa|psi|aerosol|"
                    r"particle|experiment|tests?\b|sample|material|habitat|cabin|apollo|mir\b|detect|alarm|toxic|"
                    r"temperature|space|station|orbit|crew|module|cygnus|lunar|moon|mars)", re.I)
FINDING_FIELDS = ("finding", "evidence", "safety_implication", "fuel_material", "oxygen_raw", "pressure_raw",
                  "flow_raw", "gravity", "spread_rate_raw", "peak_heat_release_rate_raw", "time_to_detection_raw",
                  "other_measurements", "sensors", "variables", "earth_application", "partial_g_applicability")

EXPERIMENTS = {
    "SAFFIRE-I": ("PSI-98", "Spacecraft Fire Safety Experiment I", r"saffire[\s_-]*(i|1)(?![iv\d])"),
    "SAFFIRE-II": ("PSI-99", "Spacecraft Fire Experiment II", r"saffire[\s_-]*(ii|2)(?![iv\d])"),
    "SAFFIRE-III": ("PSI-100", "Spacecraft Fire Experiment III", r"saffire[\s_-]*(iii|3)(?![iv\d])"),
    "SAFFIRE-IV": ("", "Spacecraft Fire Experiment IV", r"saffire[\s_-]*(iv|4)(?![iv\d])"),
    "SAFFIRE-V": ("", "Spacecraft Fire Experiment V", r"saffire[\s_-]*(v|5)(?![iv\d])"),
    "SAFFIRE-VI": ("", "Spacecraft Fire Experiment VI", r"saffire[\s_-]*(vi|6)(?![iv\d])"),
    "BASS": ("PSI-26", "Burning and Suppression of Solids", r"\bbass(?![\s_-]*(ii|2)\b)\b"),
    "BASS-II": ("PSI-25", "Burning and Suppression of Solids II", r"\bbass[\s_-]*(ii|2)\b"),
    "FLEX": ("PSI-69", "Flame Extinguishment Experiment", r"\bflex(?![\s_-]*(2|ii)\b)\b"),
    "FLEX-2": ("PSI-68", "Flame Extinguishment Experiment 2", r"\bflex[\s_-]*(2|ii)\b"),
    "CFI": ("PSI-39", "Cool Flames Investigation", r"\bcfi\b(?![\s_-]*g)"),
    "CFI-G": ("PSI-159", "Cool Flames Investigation with Gases", r"\bcfi[\s_-]*g\b"),
    "ACME-FLAME-DESIGN": ("PSI-10", "ACME Flame Design", r"flame[\s_-]*design"),
    "ACME-BRE": ("PSI-20", "ACME Burning Rate Emulator", r"\bbre\b|burning rate emulator"),
    "ACME-CLD": ("PSI-21", "ACME Coflow Laminar Diffusion Flame", r"\bcld\b|coflow laminar"),
    "ACME-EFIELD": ("PSI-22", "ACME Electric-Field Flames", r"e[\s_-]*field|electric[\s_-]*field"),
    "ACME-SFLAME": ("PSI-23", "ACME Structure and Response of Spherical Diffusion Flames", r"s[\s_-]*flame\b"),
    "SAME": ("PSI-102", "Smoke and Aerosol Measurement Experiment", r"(?-i)\bSAME\b(?![\s_-]*R\b)"),
    "SAME-R": ("PSI-101", "Smoke Aerosol Measurement Experiment Reflight", r"(?-i)\bSAME[\s_-]*R\b"),
    "SPICE": ("PSI-107", "Smoke Point In Co-flow Experiment", r"\bspice\b"),
    "SLICE": ("PSI-106", "Structure and Liftoff In Combustion Experiment", r"\bslice\b"),
    "DAFT": ("PSI-47", "Dust and Aerosol Measurement Feasibility Test", r"\bdaft\b"),
}
FAMILIES = {
    r"\bsaffire\b(?![\s_-]*(i|ii|iii|iv|v|vi|[1-6])\b)": [k for k in EXPERIMENTS if k.startswith("SAFFIRE")],
    r"\bacme\b": [k for k in EXPERIMENTS if k.startswith("ACME")] + ["CFI-G"],
    r"cool flame": ["CFI", "CFI-G"],
}
PSI_TO_KEY = {psi: k for k, (psi, _, _) in EXPERIMENTS.items() if psi}
PSI_GROUND = {"PSI-60": ["SPICE"], "PSI-62": ["BASS", "BASS-II"], "PSI-115": ["SAME", "SAME-R"],
              "PSI-117": ["FLEX"], "PSI-142": ["CFI-G"]}
FACT_SHEETS = {"acme": [k for k in EXPERIMENTS if k.startswith("ACME")] + ["CFI-G"],
               "suppression-of-solids": ["BASS", "BASS-II"], "-daft": ["DAFT"], "-flex": ["FLEX", "FLEX-2"],
               "saffire": [k for k in EXPERIMENTS if k.startswith("SAFFIRE")], "-same": ["SAME", "SAME-R"],
               "-slice": ["SLICE"], "-spice": ["SPICE"]}
KEY_ALIASES = {"COOL-FLAME-TRANSITIONS": ["CFI-G"]}

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


def experiments_in(text):
    raw = str(text)
    low = raw.lower()
    found = {}
    for key, (_, _, pattern) in EXPERIMENTS.items():
        if pattern.startswith("(?-i)"):
            m = re.search(pattern[5:], raw)
        else:
            m = re.search(pattern, low)
        if m:
            found[key] = m.start()
    for pattern, keys in FAMILIES.items():
        m = re.search(pattern, low)
        if m:
            for k in keys:
                found.setdefault(k, m.start() + 0.5)
    return sorted(found, key=found.get)


def experiments_for_file(name):
    m = re.match(r"(PSI-\d+)", name)
    if m:
        psi = m.group(1)
        return [PSI_TO_KEY[psi]] if psi in PSI_TO_KEY else PSI_GROUND.get(psi, [])
    if name.startswith("ICES-2026-577"):
        return ["SAFFIRE-IV", "SAFFIRE-V", "SAFFIRE-VI"]
    low = name.lower()
    for word, keys in FACT_SHEETS.items():
        if word in low:
            return keys
    return []


def experiments_for_key(key, psi=""):
    key = key.strip().upper()
    if key in EXPERIMENTS:
        return [key]
    if psi in PSI_TO_KEY:
        return [PSI_TO_KEY[psi]]
    if psi in PSI_GROUND:
        return PSI_GROUND[psi]
    return KEY_ALIASES.get(key, [])


def make_chunk(text, document, kind, experiments, pages=()):
    return {"text": text, "document": document, "kind": kind,
            "experiments": list(experiments), "pages": sorted(set(pages))}


def pack(sentences, document, kind, experiments, prefix=""):
    chunks, cur = [], []
    for s, page in sentences:
        current_text = " ".join(x for x, _ in cur)
        if cur and n_tokens(current_text + " " + s) > MAX_TOKENS:
            chunks.append(make_chunk(prefix + current_text, document, kind, experiments,
                                     [p for _, p in cur if p]))
            cur = cur[-1:]
        cur.append((s, page))
    if cur:
        chunks.append(make_chunk(prefix + " ".join(x for x, _ in cur), document, kind, experiments,
                                 [p for _, p in cur if p]))
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
    if "fact_sheets" in path.parts:
        kind = "factsheet"
    elif SPEC_FILE.search(path.name):
        kind = "spec"
    else:
        kind = "paper"
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
    return pack(sentences, path.name, kind, experiments_for_file(path.name))


def load_markdown(path):
    sentences = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip("#-* ").strip()
        if line:
            sentences += [(s, None) for s in split_sentences(line)]
    return pack(sentences, path.name, "background", [])


def load_docx(path):
    import docx
    document = docx.Document(str(path))
    experiments = experiments_for_file(path.name)
    sentences = []
    for paragraph in document.paragraphs:
        text = clean_value(paragraph.text)
        if text:
            sentences += [(s, None) for s in split_sentences(text)]
    chunks = pack(sentences, path.name, "doc", experiments)
    for table in document.tables:
        rows = [[clean_value(cell.text) for cell in row.cells] for row in table.rows]
        if len(rows) < 2:
            continue
        header = rows[0]
        for row in rows[1:]:
            facts = "; ".join(f"{h}: {v}" for h, v in zip(header, row) if h and v)
            if facts:
                chunks.append(make_chunk(facts + ".", path.name, "table_row", experiments))
    return chunks


def load_xlsx(path):
    import openpyxl
    experiments = experiments_for_file(path.name)
    label = experiments[0] if experiments else path.stem
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
                chunks.append(make_chunk(f"{label} {sheet.title}: {facts}.", path.name, "spreadsheet_row", experiments))
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
        experiments = experiments_for_key(label, rows[0]["psi_id"])
        for row in rows:
            page = row["source_page"]
            chunks.append(make_chunk(row_text(row, label), Path(row["source_file"]).name, "table_row",
                                     experiments, [int(page)] if page.isdigit() else []))
        chunks.append(make_chunk(summary_text(rows, label), "psi_tests_clean.csv", "table_summary", experiments))
    return chunks


def load_investigations(path):
    chunks = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            psi = row["psi_id"]
            experiments = [PSI_TO_KEY[psi]] if psi in PSI_TO_KEY else PSI_GROUND.get(psi, [])
            name = f"{row['acronym'] + ' – ' if row['acronym'] else ''}{row['title']} ({psi})"
            overview = (f"{name}. Type: {row['type']}. Area: {row['sub_area'] or row['research_area']}. "
                        f"Dates: {row['start'] or '?'} to {row['end'] or '?'}. DOI: {row['doi']}.")
            chunks.append(make_chunk(overview, path.name, "experiment", experiments))
            for field in ("objective", "approach", "hypothesis", "impacts"):
                if row[field]:
                    sentences = [(s, None) for s in split_sentences(row[field])]
                    chunks += pack(sentences, path.name, "experiment", experiments, f"{name} – {field}: ")
    return chunks


def load_findings(path):
    chunks = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("quote_match", "") == "unverified":
                continue
            facts = "; ".join(f"{k.replace('_raw', '').replace('_', ' ')}: {row[k]}" for k in FINDING_FIELDS if row.get(k))
            page = row.get("page", "")
            experiments = [k for k in row.get("experiment_keys", "").split(";") if k in EXPERIMENTS]
            chunks.append(make_chunk(f"Finding ({row.get('investigation', '')}): {facts}.",
                                     row.get("document_name", path.name), "finding", experiments,
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
    chunks, seen = [], {}
    for path in sorted(DATA.rglob("*")):
        if not path.is_file() or EXCLUDE.search(path.name):
            continue
        try:
            loaded = load_file(path)
        except Exception as e:
            print(f"skipped {path.name}: {e}")
            continue
        added = 0
        for c in loaded:
            key = re.sub(r"\W+", " ", c["text"].lower()).strip()
            if len(key) < 20:
                continue
            if key in seen:
                kept = seen[key]
                kept["experiments"] += [e for e in c["experiments"] if e not in kept["experiments"]]
                continue
            seen[key] = c
            chunks.append(c)
            added += 1
        if verbose and loaded:
            print(f"{added:>5} of {len(loaded):>5}  {path.relative_to(DATA)}")
    return chunks


def header(c):
    pages = f" p.{','.join(map(str, c['pages']))}" if c["pages"] else ""
    about = f" · {', '.join(c['experiments'][:3])}" if c["experiments"] else ""
    return f"{c['document']}{pages}{about}"


def expand(question):
    low = question.lower()
    extra = [more for words, more in SYNONYMS.items() if re.search(rf"\b{re.escape(words)}\b", low)]
    return question + " " + " ".join(extra)


def test_ids(question):
    return [re.sub(r"^(test (no\.? )?|#\s?)", "", m.lower()) for m in TEST_ID.findall(question)]


def mentions_id(c, ids):
    start = c["text"][:160].lower()
    return any(re.search(rf"(?<![\w-]){re.escape(t)}(?![\w-])", start) for t in ids)


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
        self.docs = [Counter(tokens(header(c) + " " + c["text"])) for c in chunks]
        self.lengths = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.lengths) / len(self.lengths)
        self.n = len(self.docs)
        self.df = Counter(w for d in self.docs for w in d)
        self.idf = {w: math.log(1 + (self.n - f + 0.5) / (f + 0.5)) for w, f in self.df.items()}
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
        keys = [hashlib.md5(t.encode("utf-8")).hexdigest() for t in texts]
        path = CACHE / (EMBED_MODEL.replace("/", "_") + ".npz")
        saved = {}
        if path.exists():
            data = np.load(path)
            saved = dict(zip(data["keys"], data["vectors"]))
        missing = [(k, t) for k, t in zip(keys, texts) if k not in saved]
        if missing:
            print(f"Embedding {len(missing)} new passages (saved for next time)...")
            vectors = self.model.encode([t for _, t in missing], normalize_embeddings=True,
                                        batch_size=64, show_progress_bar=True)
            saved.update({k: v for (k, _), v in zip(missing, vectors)})
            CACHE.mkdir(exist_ok=True)
            np.savez(path, keys=np.array(list(saved)), vectors=np.array(list(saved.values())))
        self.vectors = np.array([saved[k] for k in keys])

    def scores(self, question):
        q = self.model.encode(QUERY_PREFIX + question, normalize_embeddings=True)
        return self.vectors @ q


class Index:
    def __init__(self, chunks):
        self.chunks = chunks
        self.bm25 = BM25(chunks)
        self.dense = Dense(chunks)
        try:
            self.reranker = CrossEncoder(RERANK_MODEL, max_length=512)
        except Exception as e:
            print(f"reranker off ({e})")
            self.reranker = None


def ranks(scores, only_positive=False):
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return {i: r for r, i in enumerate(order, 1) if scores[i] > 0 or not only_positive}


INDEX = None


def get_index():
    global INDEX
    if INDEX is None:
        INDEX = Index(load_all())
    return INDEX


def search(question, k=6, experiment=None):
    index = get_index()
    chunks = index.chunks
    keyword = ranks(index.bm25.scores(expand(question)), only_positive=True)
    meaning = ranks(index.dense.scores(question))
    fused = {}
    for ranking, weight in ((keyword, KEYWORD_WEIGHT), (meaning, MEANING_WEIGHT)):
        for i, r in ranking.items():
            fused[i] = fused.get(i, 0) + weight / (RRF_K + r)

    named = set(experiments_in(question))
    if experiment:
        named.add(experiment)
    ids = test_ids(question)
    table_question = bool(TABLE_INTENT.search(question))
    spec_question = bool(SPEC_INTENT.search(question))

    order = sorted(fused, key=lambda i: -fused[i])
    candidates = order[:CANDIDATES]
    if ids:
        candidates += [i for i, c in enumerate(chunks) if mentions_id(c, ids)]
    if named:
        inside = [i for i in order if named & set(chunks[i]["experiments"])]
        candidates += inside[:CANDIDATES]
        if table_question:
            candidates += [i for i in inside if chunks[i]["kind"] == "table_summary"]

    scored = []
    for i in dict.fromkeys(candidates):
        c = chunks[i]
        if experiment and experiment not in c["experiments"]:
            continue
        about = bool(named & set(c["experiments"]))
        s = fused.get(i, 0)
        bonus = 0
        if named and about:
            s += EXPERIMENT_BOOST
            bonus += 1
        elif named and c["experiments"]:
            s -= OTHER_EXPERIMENT_PENALTY
        if ids and mentions_id(c, ids):
            s += TEST_ID_BOOST
            bonus += 1
        if table_question and not ids and about and c["kind"] == "table_summary":
            s += SUMMARY_BOOST
            bonus += 1
        if c["kind"] == "spec" and not spec_question:
            s -= SPEC_PENALTY
            bonus -= 1
        scored.append((i, s, bonus))
    scored.sort(key=lambda x: -x[1])
    scored = rerank(question, scored, chunks, index.reranker)
    return diversify(scored, chunks, k)


def rerank(question, scored, chunks, reranker):
    if reranker is None or not scored:
        return scored
    top = scored[:RERANK_TOP]
    pairs = [(question, header(chunks[i]) + "\n" + chunks[i]["text"]) for i, _, _ in top]
    points = reranker.predict(pairs)
    top = [(i, float(p) + RERANK_BONUS * bonus, bonus) for (i, _, bonus), p in zip(top, points)]
    top.sort(key=lambda x: -x[1])
    return top + scored[RERANK_TOP:]


def diversify(scored, chunks, k):
    results, per_kind, per_document = [], Counter(), Counter()
    for i, _, _ in scored:
        c = chunks[i]
        if per_kind[(c["document"], c["kind"])] >= MAX_PER_DOCUMENT:
            continue
        if per_document[c["document"]] >= 2 * MAX_PER_DOCUMENT:
            continue
        per_kind[(c["document"], c["kind"])] += 1
        per_document[c["document"]] += 1
        results.append(c)
        if len(results) == k:
            break
    return results


def coverage(question, hits):
    bm25 = get_index().bm25
    words = {w for w in tokens(question) if len(w) > 2} - {"saffire", "experiment", "test", "nasa", "data"}
    if not words:
        return 1.0
    found = set(tokens(" ".join(header(c) + " " + c["text"] for c in hits)))

    def rarity(w):
        if w not in bm25.df:
            return math.log(bm25.n)
        return math.log(1 + bm25.n / bm25.df[w])

    total = sum(rarity(w) for w in words)
    return sum(rarity(w) for w in words if w in found) / total


def load_env():
    for path in (HERE / ".env", HERE.parent / ".env"):
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                m = re.match(r"\s*([A-Z_]+)\s*=\s*(.*?)\s*$", line)
                if m and not os.getenv(m.group(1)):
                    os.environ[m.group(1)] = m.group(2).strip('"').strip("'")


def call_llm(question, sources, thinking=None):
    passages = "\n\n".join(f"[{s['n']}] ({s['label']})\n{s['text']}" for s in sources)
    payload = {"model": os.getenv("LLM_MODEL"), "temperature": 0,
               "messages": [{"role": "system", "content": SYSTEM},
                            {"role": "user", "content": f"QUESTION: {question}\n\nPASSAGES:\n{passages}"}]}
    if thinking in THINKING_LEVELS:
        payload["reasoning_effort"] = thinking
    base = os.getenv("LLM_BASE_URL", "").rstrip("/")
    request = urllib.request.Request(base + "/chat/completions", data=json.dumps(payload).encode("utf-8"), headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('LLM_API_KEY', '')}"})
    with urllib.request.urlopen(request, timeout=60 if thinking == "high" else 20) as response:
        return json.loads(response.read())["choices"][0]["message"]["content"].strip()


def ask(question, experiment=None, use_llm=True, thinking=None):
    hits = search(question, experiment=experiment)
    named = experiments_in(question)
    cover = coverage(question, hits)
    sources = [{"n": n, "label": header(c), "document": c["document"], "pages": c["pages"], "kind": c["kind"],
                "experiments": c["experiments"], "text": c["text"]} for n, c in enumerate(hits, 1)]
    result = {"question": question, "answer": None, "mode": "passages only", "coverage": round(cover, 2),
              "experiments": named, "sources": sources, "cited": []}

    on_topic = bool(named) or bool(DOMAIN.search(question))
    minimum = MIN_COVERAGE_WITH_EXPERIMENT if named else MIN_COVERAGE
    if not hits or cover < minimum or not on_topic:
        result.update(answer=NOT_FOUND, mode="refused")
        return result

    load_env()
    if not (use_llm and os.getenv("LLM_MODEL") and os.getenv("LLM_API_KEY")):
        return result
    text, error = None, None
    for attempt in range(3):
        try:
            text = call_llm(question, sources, thinking)
            break
        except (urllib.error.URLError, KeyError, TimeoutError, ValueError) as e:
            error = e
            time.sleep(3 * (attempt + 1))
    if text is None:
        result["error"] = f"AI call failed ({error}), showing passages only."
        return result

    valid = {str(s["n"]) for s in sources}
    text = re.sub(r"\[(\d+)\]", lambda m: m.group(0) if m.group(1) in valid else "", text)
    cited = sorted({int(n) for n in re.findall(r"\[(\d+)\]", text)})
    if NOT_FOUND.lower()[:30] in text.lower():
        cited = []
    result.update(answer=text, mode=os.getenv("LLM_MODEL"), cited=cited)
    return result


def print_result(r):
    print(f"\nQ: {r['question']}")
    if r["experiments"]:
        print(f"   about: {', '.join(r['experiments'][:4])}")
    print(f"   mode: {r['mode']}   coverage: {r['coverage']}")
    if r.get("error"):
        print("   !!", r["error"])
    print(f"\nA: {r['answer']}\n" if r["answer"] else "\n(no answer written: add LLM settings to .env)\n")
    for s in r["sources"]:
        mark = "*" if s["n"] in r["cited"] else " "
        print(f" {mark}[{s['n']}] {s['label']} | {s['kind']}\n      {s['text'][:200]}")

STORY_MIN_SCORE = 3
STORY_GAP = 3


def load_stories():
    path = DATA / "stories.json"
    return json.load(open(path, encoding="utf-8")) if path.exists() else []


def story_score(story, question, answer, experiments):
    q, a = question.lower(), (answer or "").lower()
    score = 0
    for word in story["keywords"]:
        pattern = rf"\b{re.escape(word)}"
        if re.search(pattern, q):
            score += 3
        elif re.search(pattern, a):
            score += 1
    if set(story["experiments"]) & experiments:
        score += 1
    return score


def story_for(result, shown=(), answers_since_last=None):
    if result["mode"] == "refused":
        return None
    if answers_since_last is not None and answers_since_last < STORY_GAP:
        return None
    experiments = set(result["experiments"])
    for s in result["sources"]:
        if s["n"] in result["cited"]:
            experiments.update(s["experiments"])
    best, best_score = None, STORY_MIN_SCORE - 1
    for story in load_stories():
        if story["id"] in shown:
            continue
        score = story_score(story, result["question"], result["answer"], experiments)
        if score > best_score:
            best, best_score = story, score
    return best

def evaluate(path=HERE / "eval_questions.json"):
    qs = json.load(open(path, encoding="utf-8"))
    first = top = refused = 0
    for item in qs:
        if item.get("expect") == "not_found":
            ok = ask(item["q"], use_llm=False)["mode"] == "refused"
            refused += ok
            print(f"{'OK' if ok else 'FAIL':>4}  {item['q']}  (should be refused)")
            continue
        hits = search(item["q"])
        rank = next((i + 1 for i, c in enumerate(hits)
                     if any(a.lower() in c["text"].lower() for a in item["any"])), 0)
        first += rank == 1
        top += rank > 0
        print(f"{rank or 'MISS':>4}  {item['q']}")
    print(f"\nfirst: {first}   in top 6: {top}   refused off-topic: {refused}")


if __name__ == "__main__":
    if sys.argv[1:] == ["chunks"]:
        chunks = load_all(verbose=True)
        print(len(chunks), "chunks")
        print(Counter(c["kind"] for c in chunks))
        print(Counter(e for c in chunks for e in c["experiments"]))
    elif sys.argv[1:2] == ["detect"]:
        print(experiments_in(sys.argv[2]))
    elif sys.argv[1:2] == ["search"]:
        print("about:", experiments_in(sys.argv[2]) or "no experiment named", "\n")
        for i, c in enumerate(search(sys.argv[2]), 1):
            print(f"[{i}] {header(c)} | {c['kind']} | {c['text'][:200]}\n")
    elif sys.argv[1:2] == ["ask"]:
        r = ask(sys.argv[2])
        print_result(r)
        s = story_for(r)
        if s:
            print(f"\n[ Why this matters: {s['title']} ]\n{s['story']}\nLesson: {s['lesson']}\n"
                  f"Our data: {s['data_says']}\nSource: {s['source']['name']} ({s['source']['url']})")
    elif sys.argv[1:2] == ["heldout"]:
        evaluate(HERE / "heldout.json")
    elif sys.argv[1:2] == ["answers"]:
        name = sys.argv[2] if len(sys.argv) > 2 else "eval_questions.json"
        lines = []
        for item in json.load(open(HERE / name, encoding="utf-8")):
            r = ask(item["q"])
            print(f"\nQ: {r['question']}\nA: {r['answer'] or r.get('error', '')}")
            lines.append(f"Q: {r['question']}\nA: {r['answer'] or r.get('error', '')}\n")
            time.sleep(5)
        (HERE.parent / "answers.md").write_text("\n".join(lines), encoding="utf-8")
        print("\nsaved answers.md")
    else:
        evaluate()