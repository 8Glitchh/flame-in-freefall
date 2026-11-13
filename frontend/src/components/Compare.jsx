import { X } from "lucide-react";
import { tests } from "../data/tests.js";

const rows = [
  { label: "Material", key: "material" },
  { label: "Oxygen", key: "o2", unit: "%" },
  { label: "Pressure", key: "psi", unit: " psi" },
  { label: "Growth / spread", key: "rate", unit: " mm/s", worst: true },
  { label: "Peak heat", key: "heat", unit: " W", worst: true },
  { label: "Max CO", key: "co", unit: " ppm", worst: true },
  { label: "Smoke alarm", key: "alarm", unit: " s", worst: true },
];

function showValue(test, row) {
  const value = test[row.key];
  if (value === null || value === undefined) return "—";
  if (typeof value === "number") return value.toLocaleString() + (row.unit || "");
  return value;
}

export default function Compare({ ids, toggleCompare, goRanking }) {
  const items = ids.map((id) => tests.find((t) => t.id === id));

  if (items.length < 2) {
    return (
      <div className="card grid h-full place-items-center text-center">
        <div>
          <p className="text-[17px] font-semibold">Pick at least two tests</p>
          <p className="mt-1 text-[14px] text-[var(--fg-2)]">Open a test in Ranking and tap Compare.</p>
          <button onClick={goRanking} className="press mt-4 rounded-full bg-[var(--blue)] px-4 py-2 text-[14px] font-medium">
            Go to Ranking
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col">
      <p className="section">Side by side</p>
      <div className="card overflow-hidden">
        <div className="grid" style={{ gridTemplateColumns: "180px repeat(" + items.length + ", minmax(0, 1fr))" }}>
          <div />
          {items.map((test) => (
            <div key={test.id} className="flex items-center justify-between px-4 py-4">
              <span className="text-[17px] font-semibold">Saffire {test.id}</span>
              <button
                onClick={() => toggleCompare(test.id)}
                className="press grid h-6 w-6 place-items-center rounded-full bg-[var(--card-2)] text-[var(--fg-2)]"
                aria-label="Remove"
              >
                <X size={13} />
              </button>
            </div>
          ))}

          {rows.map((row) => {
            const highest = Math.max(...items.map((t) => t[row.key] || 0));
            return (
              <div key={row.label} className="contents">
                <div className="border-t border-[var(--sep)] px-4 py-3 text-[14px] text-[var(--fg-2)]">{row.label}</div>
                {items.map((test) => {
                  const isWorst = row.worst && test[row.key] === highest;
                  return (
                    <div
                      key={test.id}
                      className="border-t border-[var(--sep)] px-4 py-3 text-[15px]"
                      style={{ color: isWorst ? "var(--orange)" : undefined }}
                    >
                      {showValue(test, row)}
                    </div>
                  );
                })}
              </div>
            );
          })}
        </div>
      </div>
      <p className="mt-3 px-1 text-[13px] text-[var(--fg-2)]">Orange marks the worst value in each row.</p>
    </div>
  );
}
