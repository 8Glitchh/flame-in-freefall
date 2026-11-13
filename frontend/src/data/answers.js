import { DOC, habitats, rank, tests } from "./tests.js";

const name = `Saffire IV–VI paper (${DOC})`;
const table = { name, ref: "Table 1" };
const summary = { name, ref: "Results" };

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

export function ask(q) {
  const s = q.toLowerCase();

  if (s.includes("mars") || s.includes("partial") || s.includes("gravity")) {
    return {
      text: "There is no partial-gravity fire data in PSI yet. Every Saffire test ran in microgravity, so 0 g and Earth's 1 g are the only bounds we can give for Mars or the Moon [1].",
      citations: [summary],
      card: { type: "nodata" },
    };
  }

  if (s.includes("smoke") || s.includes("alarm") || s.includes("co") || s.includes("detect")) {
    return {
      text: "Not always. A 2 mg/m³ smoke alarm triggered after CO had already passed the 100 ppm 24-hour limit in some tests [1]. PMMA was the worst case: VI-3 reached 338 ppm CO and the alarm only fired at 1037 s [2].",
      citations: [summary, table],
      card: { type: "alarm", rows: tests.map((t) => ({ id: t.id, alarm: t.alarm, co: t.co })) },
    };
  }

  const moon = habitats[1];
  return {
    text: "Higher. Fires in low gravity grew linearly instead of accelerating, but 8 points more oxygen made 2-sided PMMA grow 73% faster, even at 45% lower pressure [1]. Here are the tests closest to Moon-base air, ranked by how well they match [2].",
    citations: [summary, table],
    card: { type: "rank", scenario: moon, rows: rank(moon.o2, moon.psi, "prevention").slice(0, 3) },
  };
}
