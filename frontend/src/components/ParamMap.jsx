import { CartesianGrid, ReferenceArea, ResponsiveContainer, Scatter, ScatterChart, Tooltip, XAxis, YAxis, ZAxis } from "recharts";
import { useEffect, useState } from "react";
import { moonZone, tests } from "../data/tests.js";
import { getTests } from "../api.js";

const axisText = { fill: "rgba(235,235,245,.6)", fontSize: 12 };

function pointName(point) {
  if (point.id === "You") return "Your scenario";
  if (point.experiment) return point.experiment + " " + point.test;
  return "Saffire " + point.id;
}

function MapTooltip({ active, payload }) {
  if (!active || !payload || payload.length === 0) return null;
  const point = payload[0].payload;

  return (
    <div className="rounded-[10px] bg-[var(--card-2)] px-3 py-2 text-[12px] shadow-xl">
      <p className="font-semibold">{pointName(point)}</p>
      <p className="text-[var(--fg-2)]">{point.o2}% O₂ · {point.psi} psi</p>
      {point.fuel && <p className="text-[var(--fg-2)]">{point.fuel} · {point.gravity}</p>}
    </div>
  );
}

function ScenarioDot(props) {
  return <circle cx={props.cx} cy={props.cy} r={7} fill="var(--orange)" stroke="#1c1c1e" strokeWidth={2} />;
}

export default function ParamMap({ scenario }) {
  const [points, setPoints] = useState(tests);
  const you = [{ ...scenario, id: "You" }];

  useEffect(() => {
    getTests()
      .then(setPoints)
      .catch(() => setPoints(tests));
  }, []);

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center justify-between">
        <p className="section">Oxygen vs pressure</p>
        <div className="flex gap-4 pb-2 text-[12px] text-[var(--fg-2)]">
          <span className="flex items-center gap-1.5">
            <i className="h-2 w-2 rounded-full bg-[var(--blue)]" />
            PSI test ({points.length})
          </span>
          <span className="flex items-center gap-1.5">
            <i className="h-2 w-2 rounded-full bg-[var(--orange)]" />
            Your scenario
          </span>
          <span className="flex items-center gap-1.5">
            <i className="h-2 w-3 rounded-[3px] bg-[rgba(255,159,10,.25)]" />
            Moon-base air
          </span>
        </div>
      </div>

      <div className="card min-h-0 flex-1 p-5">
        <ResponsiveContainer>
          <ScatterChart margin={{ top: 10, right: 20, bottom: 20, left: 0 }}>
            <CartesianGrid stroke="rgba(84,84,88,.35)" />
            <XAxis
              type="number"
              dataKey="psi"
              domain={[5, 16]}
              tick={axisText}
              axisLine={false}
              tickLine={false}
              label={{ value: "Pressure (psi)", position: "bottom", ...axisText }}
            />
            <YAxis
              type="number"
              dataKey="o2"
              domain={[15, 40]}
              tick={axisText}
              axisLine={false}
              tickLine={false}
              label={{ value: "Oxygen (%)", angle: -90, position: "insideLeft", dx: 12, ...axisText }}
            />
            <ZAxis range={[50, 50]} />
            <ReferenceArea
              x1={moonZone.psi[0]}
              x2={moonZone.psi[1]}
              y1={moonZone.o2[0]}
              y2={moonZone.o2[1]}
              fill="rgba(255,159,10,.14)"
              stroke="none"
              label={{ value: "Moon-base air · tested only in 0 g", fill: "rgba(255,159,10,.9)", fontSize: 11, position: "insideTop", dy: 8 }}
            />
            <Tooltip content={<MapTooltip />} cursor={false} />
            <Scatter data={points} fill="var(--blue)" fillOpacity={0.7} />
            <Scatter data={you} fill="var(--orange)" isAnimationActive={false} shape={<ScenarioDot />} />
          </ScatterChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
