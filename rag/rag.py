import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
PDF = HERE.parent / "data" / "papers" / "ICES-2026-577.pdf"

COUNTRIES = r"(USA|France|Germany|Japan|Russia|Netherlands|Slovenia|Sweden|Italy|Canada|UK|Belgium|Spain)"
AFFILIATION = re.compile(rf",\s*{COUNTRIES}\b")
AUTHOR_LIST = re.compile(r"[a-z]\d{1,2},")
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


INDEX = None


def get_index():
    global INDEX
    if INDEX is None:
        INDEX = BM25(load_pdf(PDF))
    return INDEX


def search(question, k=6):
    index = get_index()
    scores = index.scores(question)
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return [index.chunks[i] for i in order[:k] if scores[i] > 0]


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
        chunks = load_pdf(PDF)
        print(len(chunks), "chunks\n")
        for c in chunks[:5]:
            print("pages", c["pages"], "|", c["text"][:250], "\n")
    elif sys.argv[1:2] == ["ask"]:
        for i, c in enumerate(search(sys.argv[2]), 1):
            print(f"[{i}] {c['document']} p.{c['pages']} | {c['text'][:200]}\n")
    else:
        evaluate()