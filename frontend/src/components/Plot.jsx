import { useState } from "react";
import { CartesianGrid, ResponsiveContainer, Scatter, ScatterChart, Tooltip, XAxis, YAxis } from "recharts";
import { Filters, filterRows } from "./DataTable.jsx";

const axes = {
  o2: "Oxygen (%)",
  psi: "Pressure (psi)",
  kpa: "Pressure (kPa)",
  flow: "Flow (cm/s)",
  burn: "Burn time (s)",
  temp: "Adiabatic flame temp (K)",
};

const colors = ["#0a84ff", "#ff9f0a", "#30d158", "#bf5af2", "#64d2ff", "#ff453a", "#ffd60a", "#5e5ce6"];
const axisText = { fill: "rgba(235,235,245,.6)", fontSize: 12 };

function PlotTooltip({ active, payload, x, y }) {
  if (!active || !payload || payload.length === 0) return null;
  const p = payload[0].payload;
  return (
    <div className="rounded-[10px] bg-[var(--card-2)] px-3 py-2 text-[12px] shadow-xl">
      <p className="font-semibold">
        {p.experiment} {p.test}
      </p>
      {p.fuel && <p className="text-[var(--fg-2)]">{p.fuel}</p>}
      <p className="text-[var(--fg-2)]">
        {axes[x]}: {p[x]} · {axes[y]}: {p[y]}
      </p>
    </div>
  );
}

export default function Plot({ rows, filters, setFilters }) {
  const [x, setX] = useState("o2");
  const [y, setY] = useState("burn");

  const points = filterRows(rows, filters).filter((r) => r[x] != null && r[y] != null);
  const groups = {};
  for (const p of points) {
    if (!groups[p.experiment]) groups[p.experiment] = [];
    groups[p.experiment].push(p);
  }
  const names = Object.keys(groups).sort((a, b) => groups[b].length - groups[a].length);

  return (
    <div className="flex h-full min-h-0 flex-col gap-3">
      <div className="flex flex-wrap items-center gap-2">
        <span className="label">Y</span>
        <select className="field" value={y} onChange={(e) => setY(e.target.value)}>
          {Object.keys(axes).map((k) => (
            <option key={k} value={k}>
              {axes[k]}
            </option>
          ))}
        </select>
        <span className="label ml-1">X</span>
        <select className="field" value={x} onChange={(e) => setX(e.target.value)}>
          {Object.keys(axes).map((k) => (
            <option key={k} value={k}>
              {axes[k]}
            </option>
          ))}
        </select>
        <span className="label ml-auto">{points.length} tests have both values</span>
      </div>
      <Filters rows={rows} filters={filters} setFilters={setFilters} />

      <div className="card min-h-0 flex-1 p-4">
        {points.length === 0 ? (
          <p className="label m-auto p-10 text-center">No tests have both of these values. Try another pair.</p>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <ScatterChart margin={{ top: 10, right: 20, bottom: 24, left: 10 }}>
              <CartesianGrid stroke="rgba(84,84,88,.4)" />
              <XAxis type="number" dataKey={x} name={axes[x]} tick={axisText} domain={["auto", "auto"]} label={{ value: axes[x], position: "bottom", fill: "rgba(235,235,245,.6)", fontSize: 12 }} />
              <YAxis type="number" dataKey={y} name={axes[y]} tick={axisText} domain={["auto", "auto"]} label={{ value: axes[y], angle: -90, position: "insideLeft", fill: "rgba(235,235,245,.6)", fontSize: 12 }} />
              <Tooltip content={<PlotTooltip x={x} y={y} />} cursor={{ stroke: "rgba(255,255,255,.2)" }} />
              {names.map((n, i) => (
                <Scatter key={n} name={n} data={groups[n]} fill={colors[i] || "rgba(235,235,245,.35)"} isAnimationActive={false} />
              ))}
            </ScatterChart>
          </ResponsiveContainer>
        )}
      </div>
      <div className="flex flex-wrap gap-3 text-[12px] text-[var(--fg-2)]">
        {names.map((n, i) => (
          <span key={n} className="flex items-center gap-1.5">
            <i className="h-2 w-2 rounded-full" style={{ background: colors[i] || "rgba(235,235,245,.35)" }} />
            {n} ({groups[n].length})
          </span>
        ))}
      </div>
    </div>
  );
}
