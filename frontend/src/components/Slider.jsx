export default function Slider({ icon, label, unit, value, onChange, min, max, step }) {
  const fill = ((value - min) / (max - min)) * 100;

  return (
    <div className="py-3">
      <div className="mb-3 flex items-baseline justify-between text-[15px]">
        <span className="flex items-center gap-1.5">
          {icon}
          {label}
        </span>
        <span className="text-[var(--fg-2)]">
          {value} {unit}
        </span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        style={{ "--fill": fill + "%" }}
      />
    </div>
  );
}
