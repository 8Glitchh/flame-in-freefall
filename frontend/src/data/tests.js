const MBAR_TO_PSI = 0.0145038;

const raw = [
  { id: "VI-2", material: "SIBAL fabric", sides: 2, mbar: 541, o2: 31, rate: 4.05, kind: "spread", heat: 3376, co: 122, alarm: 201 },
  { id: "VI-3", material: "PMMA", sides: 2, mbar: 544, o2: 30, rate: 0.38, kind: "growth", heat: 3240, co: 338, alarm: 1037 },
  { id: "VI-4", material: "PMMA", sides: 1, mbar: 550, o2: 29, rate: 0.27, kind: "growth", heat: 1487, co: 309, alarm: 1603 },
  { id: "V-2", material: "Cotton", sides: 2, mbar: 741, o2: 28, rate: 3.4, kind: "spread", heat: null, co: 74, alarm: 146 },
  { id: "V-3", material: "PMMA", sides: 1, mbar: 745, o2: 26, rate: 0.26, kind: "growth", heat: null, co: 56, alarm: 1117 },
  { id: "IV-1", material: "SIBAL fabric", sides: 2, mbar: 980, o2: 23, rate: 3.6, kind: "spread", heat: null, co: 77, alarm: 92 },
  { id: "IV-2", material: "PMMA", sides: 2, mbar: 1000, o2: 22, rate: 0.22, kind: "growth", heat: null, co: 110, alarm: 1083 },
];

export const tests = raw.map((t) => ({ ...t, psi: +(t.mbar * MBAR_TO_PSI).toFixed(1) }));

export const DOC = "ICES-2026-577";

export const habitats = [
  { id: "iss", name: "ISS", o2: 21, psi: 14.7 },
  { id: "moon", name: "Moon base", o2: 30, psi: 10.2 },
  { id: "rover", name: "Pressurized rover", o2: 34, psi: 8.2 },
  { id: "mars", name: "Mars transit", o2: 26, psi: 10.2 },
];

export const moonZone = { o2: [28, 34], psi: [7.5, 10.2] };

const clamp = (v) => Math.max(0, Math.min(1, v));

export function rank(o2, psi, need) {
  const maxRate = Math.max(...tests.map((t) => t.rate));
  const maxAlarm = Math.max(...tests.map((t) => t.alarm));
  return tests
    .map((t) => {
      const oxygen = clamp(1 - Math.abs(o2 - t.o2) / 12);
      const pressure = clamp(1 - Math.abs(psi - t.psi) / 7);
      const hazard = need === "detection" ? t.alarm / maxAlarm : t.rate / maxRate;
      const parts = { oxygen: oxygen * 45, pressure: pressure * 35, hazard: hazard * 20 };
      return { ...t, parts, score: Math.round(parts.oxygen + parts.pressure + parts.hazard) };
    })
    .sort((a, b) => b.score - a.score);
}
