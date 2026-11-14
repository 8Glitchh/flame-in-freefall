import { useState } from "react";
import { Download } from "lucide-react";

const columns = [
  { key: "experiment", label: "Experiment" },
  { key: "test", label: "Test" },
  { key: "fuel", label: "Fuel" },
  { key: "flame", label: "Flame" },
  { key: "o2", label: "O₂ %", approx: "o2_approx" },
  { key: "psi", label: "psi", approx: "psi_approx" },
  { key: "flow", label: "Flow cm/s" },
  { key: "burn", label: "Burn s" },
  { key: "temp", label: "T ad K" },
];

function toCsv(rows) {
  const keys = [...columns.map((c) => c.key), "kpa", "o2_approx", "psi_approx", "flags", "source", "row"];
  const lines = rows.map((r) => keys.map((k) => '"' + String(r[k] ?? "").replace(/"/g, '""') + '"').join(","));
  return [keys.join(","), ...lines].join("\n");
}

export function filterRows(rows, filters) {
  const q = filters.text.toLowerCase();
  return rows.filter((r) => {
    if (filters.experiment && r.experiment !== filters.experiment) return false;
    if (q && !(r.experiment + " " + r.test + " " + r.fuel).toLowerCase().includes(q)) return false;
    if (filters.o2min !== "" && !(r.o2 >= Number(filters.o2min))) return false;
    if (filters.o2max !== "" && !(r.o2 <= Number(filters.o2max))) return false;
    if (filters.psimin !== "" && !(r.psi >= Number(filters.psimin))) return false;
    if (filters.psimax !== "" && !(r.psi <= Number(filters.psimax))) return false;
    return true;
  });
}

export function Filters({ rows, filters, setFilters }) {
  const names = [...new Set(rows.map((r) => r.experiment))].sort();

  function set(changes) {
    setFilters({ ...filters, ...changes });
  }

  return (
    <div className="flex flex-wrap items-center gap-2">
      <input className="field w-[180px]" placeholder="Filter by test or fuel" value={filters.text} onChange={(e) => set({ text: e.target.value })} />
      <select className="field" value={filters.experiment} onChange={(e) => set({ experiment: e.target.value })}>
        <option value="">All experiments</option>
        {names.map((n) => (
          <option key={n}>{n}</option>
        ))}
      </select>
      <span className="label ml-1">O₂</span>
      <input className="field w-[58px]" placeholder="min" value={filters.o2min} onChange={(e) => set({ o2min: e.target.value })} />
      <input className="field w-[58px]" placeholder="max" value={filters.o2max} onChange={(e) => set({ o2max: e.target.value })} />
      <span className="label ml-1">psi</span>
      <input className="field w-[58px]" placeholder="min" value={filters.psimin} onChange={(e) => set({ psimin: e.target.value })} />
      <input className="field w-[58px]" placeholder="max" value={filters.psimax} onChange={(e) => set({ psimax: e.target.value })} />
    </div>
  );
}

export default function DataTable({ rows, filters, setFilters, openExperiment }) {
  const [sort, setSort] = useState({ key: "experiment", up: true });
  const [limit, setLimit] = useState(150);

  const shown = filterRows(rows, filters).sort((a, b) => {
    const x = a[sort.key] ?? "";
    const y = b[sort.key] ?? "";
    const order = typeof x === "number" && typeof y === "number" ? x - y : String(x).localeCompare(String(y), undefined, { numeric: true });
    return sort.up ? order : -order;
  });

  function download() {
    const blob = new Blob([toCsv(shown)], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "flame-in-freefall-tests.csv";
    link.click();
  }

  return (
    <div className="flex h-full min-h-0 flex-col gap-3">
      <div className="flex items-center justify-between gap-3">
        <Filters rows={rows} filters={filters} setFilters={setFilters} />
        <button className="pill" onClick={download}>
          <Download size={14} /> CSV
        </button>
      </div>
      <p className="label">
        {shown.length} of {rows.length} tests · ≈ means the value is approximate · click an experiment to open it
      </p>

      <div className="card min-h-0 flex-1 overflow-auto">
        <table className="data">
          <thead>
            <tr>
              {columns.map((c) => (
                <th key={c.key} onClick={() => setSort({ key: c.key, up: sort.key === c.key ? !sort.up : true })}>
                  {c.label}
                  {sort.key === c.key && (sort.up ? " ↑" : " ↓")}
                </th>
              ))}
              <th>Source</th>
            </tr>
          </thead>
          <tbody>
            {shown.slice(0, limit).map((r) => (
              <tr key={r.id}>
                {columns.map((c) => (
                  <td key={c.key}>
                    {c.key === "experiment" ? (
                      <button className="link" onClick={() => openExperiment(r.psi_id)}>
                        {r.experiment}
                      </button>
                    ) : (
                      <>
                        {c.approx && r[c.approx] && "≈"}
                        {r[c.key] ?? "–"}
                      </>
                    )}
                  </td>
                ))}
                <td className="text-[var(--fg-3)]" title={r.flags ? "Flag: " + r.flags : ""}>
                  {r.flags && <span className="text-[var(--orange)]">● </span>}
                  {r.source.split("/").pop()} r{r.row}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {shown.length > limit && (
          <button className="pill m-3" onClick={() => setLimit(limit + 300)}>
            Show more
          </button>
        )}
      </div>
    </div>
  );
}
