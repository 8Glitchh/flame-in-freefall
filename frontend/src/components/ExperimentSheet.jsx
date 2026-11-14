import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { X } from "lucide-react";
import { getExperiment } from "../api.js";

export default function ExperimentSheet({ id, onClose, showData }) {
  const [exp, setExp] = useState(null);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    if (!id) return;
    setExp(null);
    setFailed(false);
    getExperiment(id).then(setExp).catch(() => setFailed(true));
  }, [id]);

  const fields = exp
    ? [
        { label: "Objective", text: exp.objective },
        { label: "Approach", text: exp.approach },
        { label: "Hypothesis", text: exp.hypothesis },
        { label: "Why it matters", text: exp.impacts },
      ].filter((f) => f.text)
    : [];

  return (
    <AnimatePresence>
      {id && (
        <motion.div key="sheet" className="sheet-backdrop" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={onClose}>
          <motion.div
            className="sheet"
            initial={{ x: 40, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: 40, opacity: 0 }}
            transition={{ type: "spring", stiffness: 320, damping: 32 }}
            onClick={(e) => e.stopPropagation()}
          >
            <button className="sheet-close" onClick={onClose} aria-label="Close">
              <X size={16} />
            </button>

            {failed && <p className="label">Couldn't load this experiment.</p>}
            {!exp && !failed && <p className="label">Loading…</p>}

            {exp && (
              <>
                <p className="label">
                  {exp.psi_id} · {exp.research_area} · {exp.sub_area}
                </p>
                <h2 className="mt-1 text-[24px] font-bold leading-[1.2] tracking-[-0.4px]">{exp.acronym || exp.psi_id}</h2>
                <p className="mt-1 text-[15px] text-[var(--fg-2)]">{exp.title}</p>

                <div className="mt-4 grid grid-cols-3 gap-2">
                  <div className="stat">
                    <p className="label">Tests</p>
                    <p className="text-[20px] font-semibold">{exp.tests.length}</p>
                  </div>
                  <div className="stat">
                    <p className="label">Findings</p>
                    <p className="text-[20px] font-semibold">{exp.findings.length}</p>
                  </div>
                  <div className="stat">
                    <p className="label">Ran</p>
                    <p className="text-[15px] font-semibold">
                      {exp.start ? exp.start.slice(-4) : "?"}–{exp.end ? exp.end.slice(-4) : "?"}
                    </p>
                  </div>
                </div>

                <div className="mt-3 flex gap-2">
                  {exp.tests.length > 0 && (
                    <button className="pill" onClick={() => showData(exp.tests[0].experiment)}>
                      See all tests in Data
                    </button>
                  )}
                  {exp.doi && (
                    <a className="pill" href={exp.doi.startsWith("http") ? exp.doi : "https://doi.org/" + exp.doi} target="_blank" rel="noreferrer">
                      Open data (DOI)
                    </a>
                  )}
                </div>

                {fields.map((f) => (
                  <div key={f.label} className="mt-5">
                    <p className="section px-0">{f.label}</p>
                    <p className="text-[14px] leading-[1.6]">{f.text}</p>
                  </div>
                ))}

                {exp.findings.length > 0 && (
                  <div className="mt-5">
                    <p className="section px-0">Findings</p>
                    <div className="flex flex-col gap-2">
                      {exp.findings.slice(0, 8).map((f) => (
                        <div key={f.finding_id} className="stat">
                          <p className="text-[14px] leading-[1.5]">{f.finding}</p>
                          <p className="source mt-1">
                            {f.document_name}
                            {f.page_numbers && ", p. " + f.page_numbers}
                          </p>
                        </div>
                      ))}
                    </div>
                    {exp.findings.length > 8 && <p className="label mt-2">See the Findings tab for all {exp.findings.length}.</p>}
                  </div>
                )}
              </>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
