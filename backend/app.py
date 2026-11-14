import csv
import os
import sys
from pathlib import Path

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.append(str(ROOT / "rag"))
import rag

KPA_TO_PSI = 0.145038
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


def read_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def number(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


TESTS = read_csv(DATA / "psi_tests_clean.csv")
INVESTIGATIONS = read_csv(DATA / "investigations.csv")
FINDINGS = read_csv(DATA / "findings" / "psi_findings_source_checked.csv")

def load_saffire():
    saffire = []
    for row in TESTS:
        if row["experiment_key"] not in ("SAFFIRE-IV", "SAFFIRE-V", "SAFFIRE-VI"):
            continue
        spread = number(row["micro_g_spread_rate_mm_s"])
        growth = number(row["flame_length_growth_rate_mm_s"])
        saffire.append({
            "id": row["test_id"],
            "material": row["material"],
            "sides": int(row["sides_burning"]),
            "o2": number(row["o2_pct"]),
            "mbar": number(row["pressure_mbar_reported"]),
            "psi": round(number(row["pressure_kpa"]) * KPA_TO_PSI, 1),
            "rate": spread if spread else growth,
            "kind": "spread" if spread else "growth",
            "heat": number(row["peak_hrr_w"]),
            "co": number(row["max_co_increase_ppm"]),
            "alarm": number(row["time_to_alarm_s"]),
            "page": row["source_page"],
        })
    return saffire


SAFFIRE = load_saffire()


@app.get("/experiments")
def experiments(category: str = "", fuel: str = ""):
    result = []
    for inv in INVESTIGATIONS:
        tests = [t for t in TESTS if t["psi_id"] == inv["psi_id"]]
        if category and category.lower() not in (inv["research_area"] + " " + inv["sub_area"]).lower():
            continue
        if fuel and not any(fuel.lower() in t["fuel"].lower() for t in tests):
            continue
        result.append({
            "id": inv["psi_id"],
            "name": inv["acronym"],
            "title": inv["title"],
            "area": inv["sub_area"],
            "tests": len(tests),
        })
    return result


@app.get("/experiments/{psi_id}")
def experiment(psi_id: str):
    for inv in INVESTIGATIONS:
        if inv["psi_id"].lower() == psi_id.lower() or inv["acronym"].lower() == psi_id.lower():
            tests = [t for t in TESTS if t["psi_id"] == inv["psi_id"]]
            findings = [f for f in FINDINGS if f["psi_id"] == inv["psi_id"]]
            return {**inv, "tests": [clean(t) for t in tests], "findings": findings}
    raise HTTPException(404, "Experiment not found")


def clean(row):
    return {key: value for key, value in row.items() if value.strip()}


@app.get("/tests")
def tests(o2_min: float = 0, o2_max: float = 100, psi_min: float = 0, psi_max: float = 100):
    result = []
    for row in TESTS:
        o2 = number(row["o2_pct"])
        kpa = number(row["pressure_kpa"])
        if o2 is None or kpa is None:
            continue
        psi = round(kpa * KPA_TO_PSI, 1)
        if o2_min <= o2 <= o2_max and psi_min <= psi <= psi_max:
            result.append({
                "experiment": row["experiment"],
                "test": row["test_id"],
                "o2": o2,
                "psi": psi,
                "gravity": row["gravity"],
                "fuel": row["fuel"] or row["material"],
            })
    return result


@app.get("/findings")
def findings(theme: str = "", investigation: str = "", featured: bool = False):
    result = []
    for f in FINDINGS:
        themes = [t.strip() for t in f["safety_theme"].lower().split(",")]
        if theme and theme.lower() not in themes:
            continue
        if featured and f["dashboard_featured"] != "true":
            continue
        if investigation and investigation.lower() not in f["investigation"].lower():
            continue
        result.append(f)
    return result


class Scenario(BaseModel):
    o2: float
    psi: float
    need: str = "prevention"


def closeness(value, target, width):
    return max(0, min(1, 1 - abs(value - target) / width))


@app.post("/rank")
def rank(scenario: Scenario):
    fastest = max(t["rate"] for t in SAFFIRE)
    slowest_alarm = max(t["alarm"] for t in SAFFIRE)
    ranked = []
    for t in SAFFIRE:
        if scenario.need == "detection":
            hazard = t["alarm"] / slowest_alarm
        else:
            hazard = t["rate"] / fastest
        parts = {
            "oxygen": closeness(t["o2"], scenario.o2, 12) * 45,
            "pressure": closeness(t["psi"], scenario.psi, 7) * 35,
            "hazard": hazard * 20,
        }
        ranked.append({**t, "parts": parts, "score": round(sum(parts.values()))})
    ranked.sort(key=lambda t: t["score"], reverse=True)
    return ranked


class Question(BaseModel):
    question: str


def write_answer(question, passages):
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        text = passages[0]["text"]
        if text.startswith("Finding (") and "finding: " in text:
            text = text.split("finding: ", 1)[1].split("; ")[0]
        first = text.split(". ")
        return ". ".join(first[:2]).rstrip(".") + ". [1]"

    sources = "\n\n".join(f"[{i}] {p['text']}" for i, p in enumerate(passages, 1))
    prompt = (
        "Answer the question using only the passages below. "
        "Put the passage number in brackets after each fact, like [1]. "
        "Keep it to 2 or 3 sentences. If the passages don't answer it, say you don't know.\n\n"
        f"{sources}\n\nQuestion: {question}"
    )
    response = requests.post(
        GROQ_URL,
        headers={"Authorization": f"Bearer {key}"},
        json={"model": GROQ_MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2},
        timeout=30,
    )
    return response.json()["choices"][0]["message"]["content"]


@app.on_event("startup")
def load_index():
    rag.get_index()


def has_keywords(question):
    return max(rag.get_index().bm25.scores(question)) > 0


@app.post("/ask")
def ask(q: Question):
    passages = rag.search(q.question, k=5)
    if not passages or not has_keywords(q.question):
        return {"answer": "I couldn't find that in the papers we have.", "citations": []}
    citations = [{"doc": p["document"], "pages": p["pages"]} for p in passages]
    return {"answer": write_answer(q.question, passages), "citations": citations}
