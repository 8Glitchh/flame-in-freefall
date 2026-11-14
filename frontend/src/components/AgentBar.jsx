import { useEffect, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { Search } from "lucide-react";
import MiniFlame from "./MiniFlame.jsx";
import { askBackend } from "../api.js";

function has(text, q) {
  return (text || "").toLowerCase().includes(q);
}

export default function AgentBar({ scenario, rows, experiments, findings, openExperiment, askInChat, openGuide }) {
  const [text, setText] = useState("");
  const [open, setOpen] = useState(false);
  const [busy, setBusy] = useState(false);
  const [answer, setAnswer] = useState(null);
  const [flare, setFlare] = useState(0);
  const input = useRef(null);

  useEffect(() => {
    function onKey(e) {
      if ((e.ctrlKey || e.metaKey) && e.key === "k") {
        e.preventDefault();
        input.current.focus();
      }
      if (e.key === "Escape") {
        setOpen(false);
        input.current.blur();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  const q = text.trim().toLowerCase();
  const exps = q ? experiments.filter((e) => has(e.name, q) || has(e.title, q) || has(e.id, q)).slice(0, 4) : [];
  const tests = q ? rows.filter((r) => has(r.experiment + " " + r.test, q) || has(r.fuel, q)).slice(0, 4) : [];
  const finds = q.length > 2 ? findings.filter((f) => has(f.finding, q)).slice(0, 3) : [];

  function ask() {
    if (!q || busy) return;
    setBusy(true);
    setAnswer(null);
    setFlare(flare + 1);
    askBackend(text.trim(), [])
      .then((data) => setAnswer({ question: text.trim(), ...data }))
      .catch(() => setAnswer({ question: text.trim(), answer: "Couldn't reach the agent. Please try again.", citations: [] }))
      .finally(() => setBusy(false));
  }

  function pick(id) {
    setOpen(false);
    openExperiment(id);
  }

  return (
    <div className="agent">
      <div className="agent-icon">
        <MiniFlame o2={scenario.o2} psi={scenario.psi} fuel={busy ? 1 : 0} flare={flare} size={30} />
      </div>
      <form
        className="agent-search"
        onSubmit={(e) => {
          e.preventDefault();
          ask();
        }}
      >
        <Search size={16} className="text-[var(--fg-3)]" />
        <input
          ref={input}
          value={text}
          onChange={(e) => {
            setText(e.target.value);
            setAnswer(null);
            setOpen(true);
          }}
          onFocus={() => setOpen(true)}
          placeholder="Search tests, experiments, findings, or ask the agent"
        />
        <kbd>Ctrl K</kbd>
      </form>
      <button className="agent-help" onClick={openGuide} aria-label="Open guide">
        ?
      </button>

      <AnimatePresence>
        {open && q && (
          <>
            <div className="agent-backdrop" onClick={() => setOpen(false)} />
            <motion.div
              className="agent-results"
              initial={{ opacity: 0, y: -6 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -4, transition: { duration: 0.12 } }}
            >
              <button className="agent-ask" onClick={ask}>
                <span className="text-[var(--blue)]">{busy ? "Thinking…" : "Ask the agent"}</span>
                <span className="truncate text-[var(--fg-2)]">“{text.trim()}”</span>
                <span className="ml-auto text-[12px] text-[var(--fg-3)]">Enter</span>
              </button>

              {answer && (
                <div className="agent-answer">
                  <p className="text-[14px] leading-[1.55]">{answer.answer.replace(/\s*\[\d+\]/g, "")}</p>
                  {answer.citations.length > 0 && (
                    <p className="source mt-2">
                      {[...new Set(answer.citations.map((c) => c.doc))].slice(0, 3).join(" · ")}
                    </p>
                  )}
                  <button
                    className="agent-continue"
                    onClick={() => {
                      setOpen(false);
                      askInChat(answer.question);
                    }}
                  >
                    Continue in chat
                  </button>
                </div>
              )}

              {exps.length > 0 && <p className="agent-group">Experiments</p>}
              {exps.map((e) => (
                <button key={e.id} className="agent-item" onClick={() => pick(e.id)}>
                  <span className="shrink-0 font-medium">{e.name || e.id}</span>
                  <span className="truncate text-[var(--fg-2)]">{e.title}</span>
                  <span className="ml-auto shrink-0 text-[12px] text-[var(--fg-3)]">{e.tests} tests</span>
                </button>
              ))}

              {tests.length > 0 && <p className="agent-group">Tests</p>}
              {tests.map((r) => (
                <button key={r.id} className="agent-item" onClick={() => pick(r.psi_id)}>
                  <span className="shrink-0 font-medium">
                    {r.experiment} {r.test}
                  </span>
                  <span className="truncate text-[var(--fg-2)]">{r.fuel}</span>
                  <span className="ml-auto shrink-0 text-[12px] text-[var(--fg-3)]">
                    {r.o2 ? r.o2 + "% O₂" : ""} {r.psi ? "· " + r.psi + " psi" : ""}
                  </span>
                </button>
              ))}

              {finds.length > 0 && <p className="agent-group">Findings</p>}
              {finds.map((f) => (
                <button key={f.finding_id} className="agent-item" onClick={() => f.psi_id && pick(f.psi_id)}>
                  <span className="shrink-0 font-medium">{f.investigation}</span>
                  <span className="truncate text-[var(--fg-2)]">{f.finding}</span>
                </button>
              ))}
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
