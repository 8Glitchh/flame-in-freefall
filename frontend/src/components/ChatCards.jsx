import { ChevronRight, CircleSlash } from "lucide-react";
import { Bar, BarChart, ReferenceLine, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import ScoreBar from "./ScoreBar.jsx";

const axisText = { fill: "rgba(235,235,245,.6)", fontSize: 11 };

export function RankCard({ card, openScenario }) {
  return (
    <div className="card overflow-hidden">
      <div className="flex items-center justify-between px-4 pb-2 pt-4">
        <span className="text-[15px] font-semibold">Closest tests · {card.scenario.name}</span>
        <button onClick={() => openScenario(card.scenario)} className="press flex items-center gap-1 text-[14px] text-[var(--blue)]">
          Open in Dashboard <ChevronRight size={15} />
        </button>
      </div>
      {card.rows.map((test, i) => (
        <div key={test.id} className="row">
          <span className="w-4 text-[15px] text-[var(--fg-3)]">{i + 1}</span>
          <span className="w-[150px] shrink-0">
            <span className="block text-[15px]">Saffire {test.id}</span>
            <span className="block text-[12px] text-[var(--fg-2)]">{test.material}</span>
          </span>
          <ScoreBar parts={test.parts} />
          <span className="w-8 text-right text-[15px] font-semibold">{test.score}</span>
        </div>
      ))}
    </div>
  );
}

export function AlarmCard({ rows }) {
  return (
    <div className="card p-4">
      <div className="mb-3 flex items-center justify-between">
        <span className="text-[15px] font-semibold">Peak CO per test</span>
        <span className="text-[12px] text-[var(--fg-2)]">ppm · dashed line is the 100 ppm limit</span>
      </div>
      <div className="h-[170px]">
        <ResponsiveContainer>
          <BarChart data={rows} margin={{ left: -18, right: 6, top: 6 }}>
            <XAxis dataKey="id" tick={axisText} axisLine={false} tickLine={false} />
            <YAxis tick={axisText} axisLine={false} tickLine={false} />
            <Tooltip
              cursor={{ fill: "rgba(255,255,255,.04)" }}
              contentStyle={{ background: "#3a3a3c", border: "none", borderRadius: 10, fontSize: 12 }}
            />
            <ReferenceLine y={100} stroke="var(--orange)" strokeDasharray="4 4" />
            <Bar dataKey="co" radius={[4, 4, 0, 0]} fill="var(--blue)" activeBar={{ fill: "var(--cyan)" }} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export function NoDataCard() {
  return (
    <div className="card flex items-center gap-4 p-4">
      <CircleSlash size={22} className="shrink-0 text-[var(--fg-2)]" />
      <div>
        <p className="text-[15px] font-semibold">No partial-gravity data in PSI</p>
        <p className="mt-1 text-[13px] leading-[1.5] text-[var(--fg-2)]">
          The dashboard marks this as a gap on the parameter map. We're ready for Moon and Mars data when it's published.
        </p>
      </div>
    </div>
  );
}
