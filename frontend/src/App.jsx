import { useCallback, useEffect, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { ChevronRight, ChevronLeft, ChevronUp, ChevronDown } from "lucide-react";
import Chat from "./pages/Chat.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import View3D from "./pages/View3D.jsx";
import { habitats } from "./data/tests.js";

const rooms = {
  chat: { x: 0, y: 0 },
  dashboard: { x: -100, y: 0 },
  space: { x: 0, y: 100 },
};

const arrows = {
  chat: [
    { to: "dashboard", side: "right", label: "Dashboard", Icon: ChevronRight },
    { to: "space", side: "top", label: "3D view", Icon: ChevronUp },
  ],
  dashboard: [{ to: "chat", side: "left", label: "Chat", Icon: ChevronLeft }],
  space: [{ to: "chat", side: "bottom", label: "Chat", Icon: ChevronDown }],
};

const travel = {
  space: { to: "dashboard", label: "Go to Dashboard" },
  dashboard: { to: "space", label: "Go to 3D view" },
};

export default function App() {
  const [room, setRoom] = useState("chat");
  const [scenario, setScenario] = useState({ ...habitats[1], need: "prevention" });
  const [seen3d, setSeen3d] = useState(false);

  const go = useCallback((next) => {
    if (next === "space") setSeen3d(true);
    setRoom(next);
  }, []);

  const applyScenario = useCallback((patch) => setScenario((old) => ({ ...old, ...patch })), []);

  const openScenario = useCallback((s) => {
    setScenario((old) => ({ ...old, ...s }));
    go("dashboard");
  }, [go]);

  useEffect(() => {
    function onKey(e) {
      if (e.target.tagName === "INPUT") return;
      if (room === "chat" && e.key === "ArrowRight") go("dashboard");
      if (room === "chat" && e.key === "ArrowUp") go("space");
      if (room === "dashboard" && e.key === "ArrowLeft") go("chat");
      if (room === "space" && e.key === "ArrowDown") go("chat");
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [room, go]);

  return (
    <div className="relative h-full w-full overflow-hidden">
      <motion.div
        className="absolute inset-0"
        animate={{ x: `${rooms[room].x}vw`, y: `${rooms[room].y}vh` }}
        transition={{ type: "spring", stiffness: 240, damping: 34, mass: 0.9 }}
      >
        <section className="absolute inset-0">
          <Chat openScenario={openScenario} scenario={scenario} applyScenario={applyScenario} />
        </section>
        <section className="absolute inset-0" style={{ transform: "translateX(100vw)" }}>
          <Dashboard scenario={scenario} setScenario={setScenario} />
        </section>
        <section className="absolute inset-0" style={{ transform: "translateY(-100vh)" }}>
          {seen3d && <View3D active={room === "space"} />}
        </section>
      </motion.div>

      <AnimatePresence>
        {travel[room] && (
          <motion.button
            key={"travel-" + room}
            initial={{ opacity: 0, y: -6 }}
            animate={{ opacity: 1, y: 0, transition: { delay: 0.5, type: "spring", stiffness: 300, damping: 26 } }}
            exit={{ opacity: 0, transition: { duration: 0.1 } }}
            className="travel"
            onClick={() => go(travel[room].to)}
          >
            {travel[room].label}
          </motion.button>
        )}
      </AnimatePresence>

      <AnimatePresence>
        {arrows[room].map(({ to, side, label, Icon }) => (
          <motion.button
            key={room + to}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1, transition: { delay: 0.35 } }}
            exit={{ opacity: 0, transition: { duration: 0.1 } }}
            className={`edge edge-${side}`}
            onClick={() => go(to)}
          >
            <span className="edge-icon"><Icon size={18} /></span>
            <span className="edge-label">{label}</span>
          </motion.button>
        ))}
      </AnimatePresence>
    </div>
  );
}
