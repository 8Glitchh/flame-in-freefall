import { motion } from "motion/react";
import { Check, Plus } from "lucide-react";
import { partColors } from "./ScoreBar.jsx";
import { DOC } from "../data/tests.js";

function getFindings(test) {
  const findings = [];
  if (test.co > 100) {
    findings.push("Carbon monoxide reached " + test.co + " ppm, above the 100 ppm 24-hour limit.");
  }
  if (test.alarm > 600) {
    findings.push("The smoke alarm took " + Math.round(test.alarm / 60) + " minutes to trigger.");
  }
  if (test.kind === "spread") {
    findings.push("Flame spread fast across the fabric at " + test.rate + " mm/s.");
  }
  findings.push("Run in microgravity. No partial-gravity data exists yet.");
  return findings;
}

function Facts({ rows }) {
  return (
    <div className="mt-2 overflow-hidden rounded-[10px] bg-[var(--card-2)]">
      {rows.map((row) => (
        <div key={row.label} className="row min-h-[40px] py-2 text-[14px]">
          <span className="flex-1 text-[var(--fg-2)]">{row.label}</span>
          <span style={{ color: row.warn ? "var(--orange)" : undefined }}>{row.value}</span>
        </div>
      ))}
    </div>
  );
}

export default function TestDetail({ test, inCompare, toggleCompare }) {
  const conditions = [
    { label: "Oxygen", value: test.o2 + "%" },
    { label: "Pressure", value: test.mbar + " mbar · " + test.psi + " psi" },
  ];

  const results = [
    { label: test.kind === "spread" ? "Spread rate" : "Growth rate", value: test.rate + " mm/s" },
    { label: "Peak heat", value: test.heat ? test.heat.toLocaleString() + " W" : "Not measured" },
    { label: "Max CO", value: test.co + " ppm", warn: test.co > 100 },
    { label: "Smoke alarm", value: test.alarm.toLocaleString() + " s", warn: test.alarm > 600 },
  ];

  return (
    <div className="flex min-h-0 flex-col">
      <p className="section">Experiment</p>
      <motion.div key={test.id} initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="card min-h-0 flex-1 overflow-y-auto p-5">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h3 className="text-[22px] font-bold tracking-[-0.4px]">Saffire {test.id}</h3>
            <p className="mt-1 text-[13px] text-[var(--fg-2)]">
              {test.material} · {test.sides}-sided sample
            </p>
          </div>
          <button
            onClick={() => toggleCompare(test.id)}
            className="press flex items-center gap-1.5 rounded-full bg-[rgba(10,132,255,0.16)] px-3 py-1.5 text-[13px] font-medium text-[var(--blue)]"
          >
            {inCompare ? <Check size={14} /> : <Plus size={14} />}
            {inCompare ? "In Compare" : "Compare"}
          </button>
        </div>

        <div className="mt-5 grid grid-cols-3 gap-2">
          {Object.keys(test.parts).map((name) => (
            <div key={name} className="rounded-[10px] bg-[var(--card-2)] px-3 py-2.5">
              <p className="text-[12px] capitalize text-[var(--fg-2)]">{name}</p>
              <p className="mt-0.5 text-[20px] font-semibold" style={{ color: partColors[name] }}>
                {Math.round(test.parts[name])}
              </p>
            </div>
          ))}
        </div>

        <p className="mt-6 text-[13px] font-semibold text-[var(--fg-2)]">Conditions</p>
        <Facts rows={conditions} />

        <p className="mt-5 text-[13px] font-semibold text-[var(--fg-2)]">Results</p>
        <Facts rows={results} />

        <p className="mt-5 text-[13px] font-semibold text-[var(--fg-2)]">Findings</p>
        <ul className="mt-2 flex flex-col gap-2 text-[14px] leading-[1.5]">
          {getFindings(test).map((text) => (
            <li key={text} className="flex gap-2.5">
              <span className="mt-[7px] h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--fg-3)]" />
              {text}
            </li>
          ))}
        </ul>

        <p className="source mt-5">Source: Saffire IV–VI paper ({DOC}), Table 1</p>
      </motion.div>
    </div>
  );
}
