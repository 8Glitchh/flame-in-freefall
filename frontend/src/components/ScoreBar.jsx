import { motion } from "motion/react";

export const partColors = { oxygen: "var(--blue)", pressure: "var(--cyan)", hazard: "var(--indigo)" };

export default function ScoreBar({ parts, height = 4 }) {
  return (
    <div className="flex w-full overflow-hidden rounded-full bg-white/[0.08]" style={{ height }}>
      {Object.entries(parts).map(([key, value]) => (
        <motion.div
          key={key}
          initial={{ width: 0 }}
          animate={{ width: `${value}%` }}
          transition={{ type: "spring", stiffness: 200, damping: 30 }}
          style={{ background: partColors[key] }}
        />
      ))}
    </div>
  );
}
