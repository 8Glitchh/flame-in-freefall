import { motion } from "motion/react";

export default function Segmented({ options, value, onChange }) {
  const index = options.indexOf(value);
  return (
    <div className="segmented">
      <motion.span
        className="thumb"
        style={{ width: `calc((100% - 4px) / ${options.length})` }}
        initial={false}
        animate={{ x: `${index * 100}%` }}
        transition={{ type: "spring", stiffness: 500, damping: 40 }}
      />
      {options.map((o) => (
        <button key={o} onClick={() => onChange(o)} className="capitalize">
          <span>{o}</span>
        </button>
      ))}
    </div>
  );
}
