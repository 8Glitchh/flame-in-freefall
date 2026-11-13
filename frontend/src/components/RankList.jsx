import { motion } from "motion/react";
import ScoreBar, { partColors } from "./ScoreBar.jsx";

export default function RankList({ ranked, current, onSelect }) {
  return (
    <div className="flex min-h-0 flex-col">
      <div className="flex items-center justify-between">
        <p className="section">Most relevant tests</p>
        <div className="flex gap-3 pb-2 text-[12px] text-[var(--fg-2)]">
          {Object.keys(partColors).map((name) => (
            <span key={name} className="flex items-center gap-1.5 capitalize">
              <i className="h-2 w-2 rounded-full" style={{ background: partColors[name] }} />
              {name}
            </span>
          ))}
        </div>
      </div>

      <div className="card min-h-0 flex-1 overflow-y-auto">
        {ranked.map((test, i) => (
          <motion.button
            key={test.id}
            layout="position"
            transition={{ type: "spring", stiffness: 400, damping: 36 }}
            onClick={() => onSelect(test.id)}
            aria-selected={current.id === test.id}
            className="row"
          >
            <span className="w-5 text-[15px] text-[var(--fg-3)]">{i + 1}</span>
            <span className="min-w-0 flex-1">
              <span className="flex items-baseline justify-between gap-3">
                <span className="text-[15px] font-medium">Saffire {test.id}</span>
                <span className="text-[15px] font-semibold">{test.score}</span>
              </span>
              <span className="mb-2 block text-[12px] text-[var(--fg-2)]">
                {test.material} · {test.o2}% O₂ · {test.psi} psi
              </span>
              <ScoreBar parts={test.parts} />
            </span>
          </motion.button>
        ))}
      </div>
    </div>
  );
}
