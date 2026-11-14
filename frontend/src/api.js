const API = "http://localhost:8000";

async function post(path, body) {
  const res = await fetch(API + path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    throw new Error(`Request failed (${res.status})`);
  }
  return res.json();
}

export function askBackend(question, shown) {
  return post("/ask", { question, shown });
}

export function getRanking(scenario) {
  return post("/rank", { o2: scenario.o2, psi: scenario.psi, need: scenario.need });
}

export async function getTests() {
  const res = await fetch(API + "/tests?o2_min=15&o2_max=40&psi_min=5&psi_max=16");
  return res.json();
}
