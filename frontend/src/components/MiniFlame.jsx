import { useEffect, useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import Flame from "./Flame.jsx";

function Ball({ o2, psi, fuel, flare }) {
  const gain = useRef(1);
  const flash = useRef(0);
  const radius = useRef(15);

  useEffect(() => {
    if (flare) flash.current = 1;
  }, [flare]);

  useFrame((state, delta) => {
    radius.current = state.size.width * 0.4;
    flash.current = Math.max(0, flash.current - delta * 1.5);
    const target = 1 + fuel * 0.25 + flash.current * 0.6;
    gain.current = gain.current + (target - gain.current) * 0.1;
  });

  return (
    <group>
      <Flame o2={o2} psi={psi} size={1.25} rim={1.6} bright={0.35} radius={radius} gain={gain} />
      <Flame o2={o2} psi={psi} size={1} rim={2.2} bright={1.15} radius={radius} gain={gain} />
    </group>
  );
}

export default function MiniFlame({ o2, psi, fuel = 0, flare = 0, size }) {
  const box = size ? size : "100%";

  return (
    <div style={{ width: box, height: box }} className="pointer-events-none">
      <Canvas orthographic camera={{ zoom: 1, position: [0, 0, 100], near: 1, far: 200 }} dpr={[1, 2]} gl={{ alpha: true }}>
        <Ball o2={o2} psi={psi} fuel={fuel} flare={flare} />
      </Canvas>
    </div>
  );
}
