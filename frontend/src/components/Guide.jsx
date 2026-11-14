import { useState } from "react";
import { AnimatePresence, motion } from "motion/react";

const steps = [
  {
    title: "Welcome to Flame in Freefall",
    text: "We ranked and explained NASA's real fire tests in space. Here is a quick tour so you know where everything is.",
  },
  {
    title: "Chat",
    text: "Ask anything about fire in space. Answers come from NASA papers, and the small numbers show which paper and page each fact is from. You can also type a scenario like \"32% oxygen at 9 psi\".",
  },
  {
    title: "Stories",
    text: "When your question links to a real event, like Apollo 1 or the Mir fire, a card asks if you want to hear the story. Tap Tell me or Not now.",
  },
  {
    title: "The flame in the background",
    text: "Switch between In space and On Earth to see how gravity changes a flame. It grows or fades with the oxygen and pressure you set in the Dashboard, and leans toward your mouse.",
  },
  {
    title: "Dashboard",
    text: "On the right. Pick a habitat or move the oxygen and pressure sliders, and see which NASA tests are closest to your scenario and why.",
  },
  {
    title: "3D view",
    text: "Up top. Every test placed by oxygen, pressure and heat so you can explore them in 3D.",
  },
  {
    title: "Getting around",
    text: "Rest your mouse at the edge of the screen, click the arrows, or use the arrow keys. Saved chats are under Chats, and you can open this guide again with the ? button.",
  },
];

export default function Guide({ open, onClose }) {
  const [step, setStep] = useState(0);
  const last = step === steps.length - 1;

  function close() {
    onClose();
    setStep(0);
  }

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          key="guide"
          className="guide-backdrop"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={close}
        >
          <motion.div
            className="guide"
            initial={{ opacity: 0, y: 16, scale: 0.97 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 8, scale: 0.98 }}
            transition={{ type: "spring", stiffness: 300, damping: 28 }}
            onClick={(e) => e.stopPropagation()}
          >
            <p className="label">
              {step + 1} of {steps.length}
            </p>
            <AnimatePresence mode="wait">
              <motion.div
                key={step}
                initial={{ opacity: 0, x: 12 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -12 }}
                transition={{ duration: 0.18 }}
              >
                <h2 className="text-[22px] font-semibold leading-[1.25]">{steps[step].title}</h2>
                <p className="mt-2 text-[15px] leading-[1.55] text-[var(--fg-2)]">{steps[step].text}</p>
              </motion.div>
            </AnimatePresence>

            <div className="guide-dots">
              {steps.map((s, i) => (
                <span key={i} className={i === step ? "on" : ""} />
              ))}
            </div>

            <div className="flex items-center gap-2">
              <button className="story-no" onClick={close}>
                Skip
              </button>
              <div className="flex-1" />
              {step > 0 && (
                <button className="story-no" onClick={() => setStep(step - 1)}>
                  Back
                </button>
              )}
              <button className="story-yes" onClick={() => (last ? close() : setStep(step + 1))}>
                {last ? "Get started" : "Next"}
              </button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
