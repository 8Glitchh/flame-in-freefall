import { useState } from "react";

const themes = ["all", "prevention", "detection", "suppression", "products", "comparison", "gap"];

export default function Findings({ findings, openExperiment }) {
  const [theme, setTheme] = useState("all");
  const [text, setText] = useState("");
  const [experiment, setExperiment] = useState("");
  const [featured, setFeatured] = useState(false);
  const [limit, setLimit] = useState(40);

  const names = [...new Set(findings.map((f) => f.investigation))].sort();
  const q = text.toLowerCase();

  const shown = findings.filter((f) => {
    const list = f.safety_theme.split(",").map((t) => t.trim());
    if (theme !== "all" && !list.includes(theme)) return false;
    if (experiment && f.investigation !== experiment) return false;
    if (featured && f.dashboard_featured !== "true") return false;
    if (q && !(f.finding + " " + f.safety_implication).toLowerCase().includes(q)) return false;
    return true;
  });

  return (
    <div className="flex h-full min-h-0 flex-col gap-3">
      <div className="flex flex-wrap items-center gap-2">
        {themes.map((t) => (
          <button key={t} className={theme === t ? "chip on" : "chip"} onClick={() => setTheme(t)}>
            {t}
          </button>
        ))}
      </div>
      <div className="flex flex-wrap items-center gap-2">
        <input className="field w-[220px]" placeholder="Search findings" value={text} onChange={(e) => setText(e.target.value)} />
        <select className="field" value={experiment} onChange={(e) => setExperiment(e.target.value)}>
          <option value="">All experiments</option>
          {names.map((n) => (
            <option key={n}>{n}</option>
          ))}
        </select>
        <label className="label flex items-center gap-2">
          <input type="checkbox" checked={featured} onChange={(e) => setFeatured(e.target.checked)} />
          Key findings only
        </label>
        <span className="label ml-auto">
          {shown.length} of {findings.length} findings, each checked against its source
        </span>
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto pr-1">
        <div className="flex flex-col gap-2">
          {shown.slice(0, limit).map((f) => (
            <div key={f.finding_id} className="card px-4 py-3">
              <p className="text-[14px] leading-[1.5]">{f.finding}</p>
              {f.safety_implication && <p className="mt-1 text-[13px] leading-[1.5] text-[var(--fg-2)]">{f.safety_implication}</p>}
              <div className="mt-2 flex flex-wrap items-center gap-2 text-[12px]">
                {f.psi_id ? (
                  <button className="link" onClick={() => openExperiment(f.psi_id)}>
                    {f.investigation}
                  </button>
                ) : (
                  <span className="font-medium">{f.investigation}</span>
                )}
                <span className="tag">{f.safety_theme}</span>
                <span className={f.confidence === "high" ? "tag good" : "tag"}>{f.confidence} confidence</span>
                {f.is_inferred === "true" && <span className="tag warn">inferred</span>}
                <span className="source ml-auto">
                  {f.document_name}
                  {f.page_numbers && ", p. " + f.page_numbers}
                </span>
              </div>
            </div>
          ))}
        </div>
        {shown.length > limit && (
          <button className="pill my-3" onClick={() => setLimit(limit + 60)}>
            Show more
          </button>
        )}
      </div>
    </div>
  );
}
