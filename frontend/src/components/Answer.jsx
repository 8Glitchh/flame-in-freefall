import { useEffect, useState } from "react";
import { motion } from "motion/react";
import { AlarmCard, NoDataCard, RankCard } from "./ChatCards.jsx";

function toBlocks(text) {
  return text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const bullet = /^[•*-]\s+/.test(line);
      const body = bullet ? line.replace(/^[•*-]\s+/, "") : line;
      const heading = !bullet && body.endsWith(":") && body.length < 90;
      const words = body.split(" ").filter(Boolean);
      const label = bullet ? words.findIndex((w, i) => i < 6 && w.endsWith(":")) : -1;
      return { bullet, heading, words, label };
    });
}

function Word({ word, first, citations }) {
  const match = word.match(/^\[(\d)\](.*)$/);
  const source = match ? citations[Number(match[1]) - 1] : null;
  if (!source) {
    return (
      <span>
        {!first && " "}
        {word}
      </span>
    );
  }
  return (
    <span>
      <sup className="cite" data-tip={source.name + ", " + source.ref}>{match[1]}</sup>
      {match[2]}
    </span>
  );
}

export default function Answer({ msg, openScenario }) {
  const blocks = toBlocks(msg.text);
  const total = blocks.reduce((sum, b) => sum + b.words.length, 0);
  const [shown, setShown] = useState(msg.old ? total : 0);
  const done = shown >= total;

  useEffect(() => {
    if (done) return;
    const timer = setTimeout(() => setShown(shown + 1), 28);
    return () => clearTimeout(timer);
  }, [shown, done]);

  let start = 0;

  return (
    <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="flex flex-col gap-4">
      <div className="flex flex-col gap-2.5 text-[16px] leading-[1.65]">
        {blocks.map((b, bi) => {
          const from = start;
          start += b.words.length;
          const visible = b.words.slice(0, Math.max(0, shown - from));
          if (!visible.length) return null;
          const words = visible.map((word, i) => {
            const w = <Word key={i} word={word} first={i === 0} citations={msg.citations} />;
            return i <= b.label ? <strong key={i} className="font-semibold">{w}</strong> : w;
          });
          if (b.heading) {
            return (
              <p key={bi} className="mt-2 text-[13px] font-semibold uppercase tracking-[0.6px] text-[var(--fg-2)]">
                {words}
              </p>
            );
          }
          if (b.bullet) {
            return (
              <div key={bi} className="flex gap-2.5 pl-1">
                <span className="mt-[11px] h-[5px] w-[5px] shrink-0 rounded-full bg-[var(--fg-2)]" />
                <p>{words}</p>
              </div>
            );
          }
          return <p key={bi}>{words}</p>;
        })}
      </div>

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
