import { habitats, rank, tests } from "./tests.js";

export function readScenario(text) {
  const s = text.toLowerCase();
  const o2 = s.match(/(\d{2}(?:\.\d)?)\s*%?\s*(?:o2|o₂|oxygen)/) || s.match(/(?:o2|o₂|oxygen)\D{0,8}(\d{2}(?:\.\d)?)/);
  const psi = s.match(/(\d{1,2}(?:\.\d)?)\s*psi/);
  const patch = {};
  if (o2) patch.o2 = Math.min(40, Math.max(15, Math.round(Number(o2[1]))));
  if (psi) patch.psi = Math.min(15, Math.max(5, Number(psi[1])));
  if (!o2 && !psi) return null;
  return { ...patch, id: "custom", name: "Custom" };
}

export function setReply(next) {
  return {
    text: `Done. The scenario is now ${next.o2}% oxygen at ${next.psi} psi. The flame and the Dashboard follow it, and these are the closest tests.`,
    citations: [],
    card: { type: "rank", scenario: next, rows: rank(next.o2, next.psi, next.need || "prevention").slice(0, 3) },
  };
}

export function pickCard(q) {
  const s = q.toLowerCase();
  if (s.includes("mars") || s.includes("partial") || s.includes("gravity")) return { type: "nodata" };
  if (s.includes("smoke") || s.includes("alarm") || s.includes("co") || s.includes("detect")) {
    return { type: "alarm", rows: tests.map((t) => ({ id: t.id, alarm: t.alarm, co: t.co })) };
  }
  if (s.includes("moon") || s.includes("oxygen") || s.includes("risk")) {
    const moon = habitats[1];
    return { type: "rank", scenario: moon, rows: rank(moon.o2, moon.psi, "prevention").slice(0, 3) };
  }
  return null;
}
