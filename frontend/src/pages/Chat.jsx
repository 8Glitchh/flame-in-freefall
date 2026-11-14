import { memo, useEffect, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import Answer from "../components/Answer.jsx";
import MiniFlame from "../components/MiniFlame.jsx";
import { fire } from "../components/Flame.jsx";
import { pickCard, readScenario, setReply } from "../data/answers.js";
import { askBackend } from "../api.js";

function buttonSize(o2, psi) {
  const size = 34 + ((fire(o2, psi).standoff - 0.55) / 1.1) * 32;
  return Math.round(Math.min(66, Math.max(34, size)));
}

function isQuestion(text) {
  return /\?|^(what|how|why|is|was|does|do|can|which|when)\b/i.test(text);
}

async function getReply(text, changes, scenario) {
  if (changes && !isQuestion(text)) return setReply({ ...scenario, ...changes });
  try {
    const data = await askBackend(text);
    const citations = data.citations.map((c) => ({
      name: c.doc.replace(".pdf", ""),
      ref: "p. " + c.pages.join(", "),
    }));
    return { text: data.answer, citations, card: pickCard(text) };
  } catch {
    return { text: "Chat couldn’t load an answer. Please try again.", citations: [] };
  }
}

function Chat({ openScenario, scenario, applyScenario }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [flare, setFlare] = useState(0);

  const scroller = useRef(null);
  const content = useRef(null);
  const followBottom = useRef(true);
  const lastTop = useRef(0);

  const typed = readScenario(input);
  const o2 = typed && typed.o2 ? typed.o2 : scenario.o2;
  const psi = typed && typed.psi ? typed.psi : scenario.psi;

  useEffect(() => {
    if (!content.current) return;
    const observer = new ResizeObserver(() => {
      if (followBottom.current) {
        scroller.current.scrollTo({ top: scroller.current.scrollHeight, behavior: "smooth" });
      }
    });
    observer.observe(content.current);
    return () => observer.disconnect();
  }, [messages.length > 0]);

  function onScroll() {
    const el = scroller.current;
    if (el.scrollTop < lastTop.current - 2) followBottom.current = false;
    if (el.scrollHeight - el.scrollTop - el.clientHeight < 40) followBottom.current = true;
    lastTop.current = el.scrollTop;
  }

  function send() {
    const text = input.trim();
    if (!text || busy) return;

    const changes = readScenario(text);
    setInput("");
    setBusy(true);
    setFlare(flare + 1);
    followBottom.current = true;
    setMessages((old) => [...old, { role: "user", text }]);
    if (changes) applyScenario(changes);

    getReply(text, changes, scenario).then((reply) => {
      setMessages((old) => [...old, { role: "ai", ...reply }]);
      setBusy(false);
    });
  }

  const size = buttonSize(o2, psi);

  return (
    <div className="flex h-full flex-col items-center px-6 pb-7 pt-20">
      <div ref={scroller} onScroll={onScroll} className="chat-scroll flex w-full max-w-[760px] flex-1 flex-col overflow-y-auto">
        <AnimatePresence>
          {messages.length === 0 ? (
            <motion.div key="hello" exit={{ opacity: 0, y: -12 }} className="m-auto text-center">
              <h1 className="arrive text-[40px] font-semibold leading-[1.1] tracking-[-0.8px]">
                How does fire behave <span className="text-[var(--fg-2)]">without gravity?</span>
              </h1>
            </motion.div>
          ) : (
            <div ref={content} className="flex flex-col gap-7 pb-6 pt-6">
              {messages.map((m, i) =>
                m.role === "user" ? (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 10, scale: 0.98 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    transition={{ type: "spring", stiffness: 300, damping: 28 }}
                    className="ml-auto max-w-[75%] rounded-[20px] bg-[var(--blue)] px-4 py-2.5 text-[15px]"
                  >
                    {m.text}
                  </motion.div>
                ) : (
                  <Answer key={i} msg={m} openScenario={openScenario} />
                )
              )}
              {busy && (
                <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex items-center gap-3 text-[13px] text-[var(--fg-2)]">
                  <span className="typing">
                    <span />
                    <span />
                    <span />
                  </span>
                  Searching the papers
                </motion.div>
              )}
            </div>
          )}
        </AnimatePresence>
      </div>

      <div className="w-full max-w-[760px]">
        <form
          className="composer"
          onSubmit={(e) => {
            e.preventDefault();
            send();
          }}
        >
          <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Ask about flammability, smoke, oxygen, a test…" />
          <motion.button
            type="submit"
            disabled={!input.trim() || busy}
            className="flame-send"
            aria-label="Send"
            data-tip={o2 + '% O₂ · ' + psi + ' psi · set it in the Dashboard or type "32% oxygen at 9 psi"'}
            animate={{ width: size, height: size }}
            transition={{ type: "spring", stiffness: 220, damping: 24 }}
          >
            <span className="flame-fire">
              <MiniFlame o2={o2} psi={psi} fuel={Math.min(input.length, 60) / 60} flare={flare} />
            </span>
          </motion.button>
        </form>
      </div>
    </div>
  );
}

export default memo(Chat);
