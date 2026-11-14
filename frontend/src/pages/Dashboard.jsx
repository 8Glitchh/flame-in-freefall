import { memo, useEffect, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { Check } from "lucide-react";
import Segmented from "../components/Segmented.jsx";
import Slider from "../components/Slider.jsx";
import MiniFlame from "../components/MiniFlame.jsx";
import RankList from "../components/RankList.jsx";
import TestDetail from "../components/TestDetail.jsx";
import ParamMap from "../components/ParamMap.jsx";
import Compare from "../components/Compare.jsx";
import AgentBar from "../components/AgentBar.jsx";
import DataTable from "../components/DataTable.jsx";
import Findings from "../components/Findings.jsx";
import ExperimentSheet from "../components/ExperimentSheet.jsx";
import Plot from "../components/Plot.jsx";
import { habitats, rank, tests } from "../data/tests.js";
import { getData, getExperiments, getFindings, getRanking } from "../api.js";

const tabs = ["Ranking", "Map", "Plot", "Data", "Findings", "Compare"];
const noFilters = { text: "", experiment: "", o2min: "", o2max: "", psimin: "", psimax: "" };
const defaultWeights = { oxygen: 45, pressure: 35, hazard: 20 };

function reweigh(ranked, w) {
  const total = w.oxygen + w.pressure + w.hazard || 1;
  return ranked
    .map((t) => {
      const parts = {
        oxygen: ((t.parts.oxygen / 45) * w.oxygen * 100) / total,
        pressure: ((t.parts.pressure / 35) * w.pressure * 100) / total,
        hazard: ((t.parts.hazard / 20) * w.hazard * 100) / total,
      };
      return { ...t, parts, score: Math.round(parts.oxygen + parts.pressure + parts.hazard) };
    })
    .sort((a, b) => b.score - a.score);
}

function Dashboard({ scenario, setScenario, openGuide, askInChat }) {
  const [tab, setTab] = useState("Ranking");
  const [selected, setSelected] = useState(null);
  const [compare, setCompare] = useState(["VI-3", "IV-2"]);

  const [ranked, setRanked] = useState(rank(scenario.o2, scenario.psi, scenario.need));
  const [weights, setWeights] = useState(defaultWeights);
  const [rows, setRows] = useState([]);
  const [experiments, setExperiments] = useState([]);
  const [findings, setFindings] = useState([]);
  const [filters, setFilters] = useState(noFilters);
  const [openExp, setOpenExp] = useState(null);

  useEffect(() => {
    getData().then(setRows).catch(() => {});
    getExperiments().then(setExperiments).catch(() => {});
    getFindings().then(setFindings).catch(() => {});
  }, []);

  useEffect(() => {
    getRanking(scenario)
      .then(setRanked)
      .catch(() => setRanked(rank(scenario.o2, scenario.psi, scenario.need)));
  }, [scenario.o2, scenario.psi, scenario.need]);

  const weighted = reweigh(ranked, weights);
  const current = weighted.find((t) => t.id === selected) || weighted[0];

  function showData(experiment) {
    setFilters({ ...noFilters, experiment });
    setOpenExp(null);
    setTab("Data");
  }

  function update(changes) {
    setScenario((old) => ({ ...old, ...changes }));
  }

  function toggleCompare(id) {
    if (compare.includes(id)) {
      setCompare(compare.filter((x) => x !== id));
    } else {
      setCompare([...compare, id].slice(-3));
    }
  }

  return (
    <div className="flex h-full gap-6 pb-6 pt-20 pl-28 pr-6">
      <aside className="w-[270px] shrink-0 overflow-y-auto">
        <h2 className="px-1 pb-5 text-[22px] font-bold tracking-[-0.4px]">Scenario</h2>

        <p className="section">Habitat</p>
        <div className="card mb-6 overflow-hidden">
          {habitats.map((h) => (
            <button key={h.id} onClick={() => update(h)} className="row press">
              <span className="flex-1">
                <span className="block text-[15px]">{h.name}</span>
                <span className="block text-[12px] text-[var(--fg-2)]">{h.o2}% O₂ · {h.psi} psi</span>
              </span>
              {scenario.id === h.id && <Check size={17} className="text-[var(--blue)]" />}
            </button>
          ))}
        </div>

        <p className="section">Atmosphere</p>
        <div className="card mb-6 px-4 py-1">
          <Slider
            icon={<MiniFlame o2={scenario.o2} psi={scenario.psi} size={18} />}
            label="Oxygen"
            unit="%"
            min={15}
            max={40}
            step={1}
            value={scenario.o2}
            onChange={(o2) => update({ o2, id: "custom", name: "Custom" })}
          />
          <div className="h-px bg-[var(--sep)]" />
          <Slider
            label="Pressure"
            unit="psi"
            min={5}
            max={15}
            step={0.1}
            value={scenario.psi}
            onChange={(psi) => update({ psi, id: "custom", name: "Custom" })}
          />
        </div>

        <p className="section">Focus</p>
        <Segmented options={["prevention", "detection"]} value={scenario.need} onChange={(need) => update({ need })} />

        <div className="mt-6 flex items-center justify-between">
          <p className="section">Score weights</p>
          {(weights.oxygen !== 45 || weights.pressure !== 35 || weights.hazard !== 20) && (
            <button className="section text-[var(--blue)]" onClick={() => setWeights(defaultWeights)}>
              Reset
            </button>
          )}
        </div>
        <div className="card px-4 py-1">
          {Object.keys(weights).map((k, i) => (
            <div key={k}>
              {i > 0 && <div className="h-px bg-[var(--sep)]" />}
              <Slider label={k[0].toUpperCase() + k.slice(1) + " match"} unit="" min={0} max={100} step={5} value={weights[k]} onChange={(v) => setWeights({ ...weights, [k]: v })} />
            </div>
          ))}
        </div>
        <p className="label mt-2 px-1 text-[12px] leading-[1.5]">
          Score = oxygen match × {weights.oxygen} + pressure match × {weights.pressure} + hazard × {weights.hazard}, scaled to 100. Hazard is spread rate for prevention, alarm time for detection.
        </p>
      </aside>

      <main className="flex min-w-0 flex-1 flex-col">
        <AgentBar
          scenario={scenario}
          rows={rows}
          experiments={experiments}
          findings={findings}
          openExperiment={setOpenExp}
          askInChat={askInChat}
          openGuide={openGuide}
        />
        <header className="flex items-end justify-between gap-6 pb-5">
          <div>
            <h1 className="text-[34px] font-bold leading-none tracking-[-0.8px]">{scenario.name}</h1>
            <p className="mt-2 text-[15px] text-[var(--fg-2)]">
              {scenario.o2}% oxygen · {scenario.psi} psi · {tests.length} Saffire tests
            </p>
          </div>
          <div className="w-[520px]">
            <Segmented options={tabs} value={tab} onChange={setTab} />
          </div>
        </header>

        <AnimatePresence mode="wait">
          <motion.div
            key={tab}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            transition={{ duration: 0.18 }}
            className="min-h-0 flex-1"
          >
            {tab === "Ranking" && (
              <div className="grid h-full grid-cols-2 gap-5">
                <RankList ranked={weighted} current={current} onSelect={setSelected} />
                <TestDetail test={current} inCompare={compare.includes(current.id)} toggleCompare={toggleCompare} />
              </div>
            )}
            {tab === "Map" && <ParamMap scenario={scenario} />}
            {tab === "Plot" && <Plot rows={rows} filters={filters} setFilters={setFilters} />}
            {tab === "Data" && <DataTable rows={rows} filters={filters} setFilters={setFilters} openExperiment={setOpenExp} />}
            {tab === "Findings" && <Findings findings={findings} openExperiment={setOpenExp} />}
            {tab === "Compare" && <Compare ids={compare} toggleCompare={toggleCompare} goRanking={() => setTab("Ranking")} />}
          </motion.div>
        </AnimatePresence>
      </main>

      <ExperimentSheet id={openExp} onClose={() => setOpenExp(null)} showData={showData} />
    </div>
  );
}

export default memo(Dashboard);
