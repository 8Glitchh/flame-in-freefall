import { useEffect, useMemo, useState } from "react";
import { motion, useMotionValue, useSpring } from "motion/react";
import { fire } from "./Flame.jsx";

function makeDots() {
  const dots = [];
  for (let i = 0; i < 45; i++) {
    const angle = Math.random() * Math.PI * 2;
    const far = 100 + Math.random() * 300;
    dots.push({
      x: Math.cos(angle) * far,
      y: Math.sin(angle) * far,
      dx: (Math.random() - 0.5) * 100,
      dy: (Math.random() - 0.5) * 100,
      size: 1.5 + Math.random() * 3.5,
      time: 5 + Math.random() * 7,
      delay: Math.random() * 6,
    });
  }
  return dots;
}

export default function FlameBall({ o2, psi, space, flare, calm, home }) {
  const [boost, setBoost] = useState(false);
  const dots = useMemo(makeDots, []);
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const x = useSpring(mouseX, { stiffness: 30, damping: 20 });
  const y = useSpring(mouseY, { stiffness: 30, damping: 20 });

  const f = fire(o2, psi);
  const size = Math.round(260 + f.glow * 160);

  useEffect(() => {
    if (!flare) return;
    setBoost(true);
    const timer = setTimeout(() => setBoost(false), 500);
    return () => clearTimeout(timer);
  }, [flare]);

  useEffect(() => {
    function onMove(e) {
      if (!home) {
        mouseX.set(0);
        mouseY.set(0);
        return;
      }
      mouseX.set((e.clientX - window.innerWidth / 2) * 0.06);
      mouseY.set((e.clientY - window.innerHeight / 2) * 0.06);
    }
    window.addEventListener("mousemove", onMove);
    return () => window.removeEventListener("mousemove", onMove);
  }, [home]);

  let opacity = 1;
  if (!home) opacity = 0.45;
  if (calm) opacity = 0.25;

  return (
    <div className="flame-bg">
      <motion.div className="flame-center" style={{ x, y }} animate={{ opacity }} transition={{ duration: 1.2 }}>
        <motion.div animate={{ scale: boost ? 1.18 : 1 }} transition={{ type: "spring", stiffness: 200, damping: 14 }}>
          <motion.div
            className="flame-sphere"
            style={{ width: size, height: size, "--soot": f.soot * 0.35 }}
            animate={space ? { opacity: 1, scale: [1, 1.04, 1] } : { opacity: 0, scale: 0.6 }}
            transition={space ? { opacity: { duration: 0.8 }, scale: { duration: calm ? 8 : 4, repeat: Infinity, ease: "easeInOut" } } : { duration: 0.6 }}
          />
          <motion.div
            className="flame-drop"
            style={{ width: size * 0.5, height: size * 1.1 }}
            animate={space ? { opacity: 0, scaleY: 0.5 } : { opacity: 1, scaleY: [1, 1.06, 0.97, 1], skewX: [0, 1.5, -1.5, 0] }}
            transition={space ? { duration: 0.6 } : { opacity: { duration: 0.8 }, default: { duration: 0.9, repeat: Infinity } }}
          />
        </motion.div>

        {dots.map((d, i) => (
          <motion.span
            key={i + (space ? "s" : "e")}
            className={space ? "flame-dot" : "flame-dot earth"}
            style={{ left: d.x, top: d.y, width: d.size, height: d.size }}
            initial={{ opacity: 0 }}
            animate={
              space
                ? { opacity: [0, 0.9, 0.5, 0.9, 0], x: [0, d.dx], y: [0, d.dy] }
                : { opacity: [0, 0.9, 0.9, 0], x: [0, d.dx * 0.2], y: [0, -220] }
            }
            transition={{ duration: space ? d.time : d.time / 3, delay: d.delay, repeat: Infinity, ease: "easeInOut" }}
          />
        ))}
      </motion.div>
    </div>
  );
}
