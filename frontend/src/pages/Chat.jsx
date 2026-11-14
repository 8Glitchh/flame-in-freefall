import { memo, useEffect, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import Answer from "../components/Answer.jsx";
import Story from "../components/Story.jsx";
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

async function getReply(text, changes, scenario, shown) {
  if (changes && !isQuestion(text)) return setReply({ ...scenario, ...changes });
  try {
    const data = await askBackend(text, shown);
    const citations = data.citations.map((c) => ({
      name: c.doc.replace(/\.\w+$/, ""),
      ref: c.pages.length ? "p. " + c.pages.join(", ") : "data table",
    }));
    return { text: data.answer, citations, card: pickCard(text), story: data.story };
  } catch {
    return { text: "Chat couldn’t load an answer. Please try again.", citations: [] };
  }
}

function loadChats() {
  try {
    return JSON.parse(localStorage.getItem("chats")) || [];
  } catch {
    return [];
  }
}

function when(time) {
  const date = new Date(time);
  if (date.toDateString() === new Date().toDateString()) {
    return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }
  return date.toLocaleDateString([], { month: "short", day: "numeric" });
}

function Chat({ openScenario, scenario, applyScenario }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [flare, setFlare] = useState(0);
  const [chats, setChats] = useState(loadChats);
  const [chatId, setChatId] = useState(null);
  const [showChats, setShowChats] = useState(false);
  const [offer, setOffer] = useState(null);

  const scroller = useRef(null);
  const content = useRef(null);
  const followBottom = useRef(true);
  const lastTop = useRef(0);
  const unsaved = useRef(false);

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

  useEffect(() => {
    if (!unsaved.current || busy) return;
    unsaved.current = false;
    const chat = { id: chatId, title: messages[0].text, time: Date.now(), messages };
    saveChats([chat, ...chats.filter((c) => c.id !== chatId)]);
  }, [messages, busy]);

  function saveChats(list) {
    setChats(list);
    localStorage.setItem("chats", JSON.stringify(list));
  }

  function openChat(chat) {
    if (busy) return;
    setMessages(chat.messages.map((m) => ({ ...m, old: true })));
    setChatId(chat.id);
    setShowChats(false);
    setOffer(null);
    followBottom.current = true;
  }

  function newChat() {
    if (busy) return;
    setMessages([]);
    setChatId(null);
    setShowChats(false);
    setOffer(null);
  }

  function deleteChat(id) {
    saveChats(chats.filter((c) => c.id !== id));
    if (id === chatId) newChat();
  }

  function tellStory() {
    unsaved.current = true;
    followBottom.current = true;
    setMessages((old) => [...old, { role: "story", story: offer }]);
    setOffer(null);
  }

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
    setOffer(null);
    followBottom.current = true;
    unsaved.current = true;
    if (!chatId) setChatId(Date.now());
    setMessages((old) => [...old, { role: "user", text }]);
    if (changes) applyScenario(changes);

    const shown = messages.filter((m) => m.story).map((m) => m.story.id);
    getReply(text, changes, scenario, shown).then((reply) => {
      setMessages((old) => [...old, { role: "ai", ...reply }]);
      setBusy(false);
      if (reply.story) setTimeout(() => setOffer(reply.story), 1500);
    });
  }

  const size = buttonSize(o2, psi);

  return (
    <div className="relative flex h-full flex-col items-center px-6 pb-7 pt-20">
      <button className="travel" onClick={() => setShowChats(!showChats)}>
        Chats
      </button>

      <AnimatePresence>
        {showChats && (
          <motion.div
            key="backdrop"
            className="chats-backdrop"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setShowChats(false)}
          />
        )}
        {showChats && (
          <motion.div
            key="chats"
            className="chats"
            initial={{ opacity: 0, x: -12, scale: 0.98 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            exit={{ opacity: 0, x: -12, scale: 0.98, transition: { duration: 0.15 } }}
            transition={{ type: "spring", stiffness: 320, damping: 30 }}
          >
            <button className="chats-new" onClick={newChat}>
              New chat
            </button>
            {chats.length === 0 && <p className="chats-empty">No saved chats yet</p>}
            {chats.map((c) => (
              <div key={c.id} className={c.id === chatId ? "chats-item active" : "chats-item"} onClick={() => openChat(c)}>
                <span className="chats-title">{c.title}</span>
                <span className="chats-time">{when(c.time)}</span>
                <button
                  className="chats-delete"
                  onClick={(e) => {
                    e.stopPropagation();
                    deleteChat(c.id);
                  }}
                >
                  Delete
                </button>
              </div>
            ))}
          </motion.div>
        )}
      </AnimatePresence>

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
                ) : m.role === "story" ? (
                  <Story key={i} story={m.story} />
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

      <div className="relative w-full max-w-[760px]">
        <AnimatePresence>
          {offer && (
            <motion.div
              className="story-offer"
              initial={{ opacity: 0, y: 12, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 8, transition: { duration: 0.15 } }}
              transition={{ type: "spring", stiffness: 320, damping: 28 }}
            >
              <div className="flex-1">
                <p className="label">Want to hear a story?</p>
                <p className="text-[14px] font-medium">{offer.title}</p>
              </div>
              <button className="story-no" onClick={() => setOffer(null)}>
                Not now
              </button>
              <button className="story-yes" onClick={tellStory}>
                Tell me
              </button>
            </motion.div>
          )}
        </AnimatePresence>
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
