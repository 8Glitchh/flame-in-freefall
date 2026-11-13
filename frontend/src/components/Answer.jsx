import { useEffect, useState } from "react";
import { motion } from "motion/react";
import { AlarmCard, NoDataCard, RankCard } from "./ChatCards.jsx";

export default function Answer({ msg, openScenario }) {
  const words = msg.text.split(" ");
  const [shown, setShown] = useState(0);
  const done = shown >= words.length;

  useEffect(() => {
    if (done) return;
    const timer = setTimeout(() => setShown(shown + 1), 28);
    return () => clearTimeout(timer);
  }, [shown, done]);

  return (
    <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="flex flex-col gap-4">
      <p className="text-[16px] leading-[1.6]">
        {words.slice(0, shown).map((word, i) => {
          const match = word.match(/^\[(\d)\](.*)$/);
          const source = match ? msg.citations[Number(match[1]) - 1] : null;
          if (!source) {
            return (
              <span key={i}>
                {i > 0 && " "}
                {word}
              </span>
            );
          }
          return (
            <span key={i}>
              <sup className="cite" data-tip={source.name + ", " + source.ref}>{match[1]}</sup>
              {match[2]}
            </span>
          );
        })}
      </p>

      {done && msg.card && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ type: "spring", stiffness: 220, damping: 26 }}
          className="flex flex-col gap-3"
        >
          {msg.card.type === "rank" && <RankCard card={msg.card} openScenario={openScenario} />}
          {msg.card.type === "alarm" && <AlarmCard rows={msg.card.rows} />}
          {msg.card.type === "nodata" && <NoDataCard />}
        </motion.div>
      )}
    </motion.div>
  );
}
