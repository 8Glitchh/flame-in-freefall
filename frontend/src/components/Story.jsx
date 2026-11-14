import { motion } from "motion/react";

export default function Story({ story }) {
  return (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="story card">
      <p className="label">Story</p>
      <h3 className="text-[18px] font-semibold leading-[1.3]">{story.title}</h3>
      <p>{story.story}</p>
      <p className="label">What changed</p>
      <p>{story.lesson}</p>
      <p className="label">What our data says</p>
      <p>{story.data_says}</p>
      <a className="source" href={story.source.url} target="_blank" rel="noreferrer">
        {story.source.name}
      </a>
    </motion.div>
  );
}
