import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import { fragmentShader, vertexShader } from "./flameShader.js";

const STOICH = 3.5;
const AIR = Math.log(1 + 0.233 / STOICH);

function between0and1(value) {
  return Math.min(1, Math.max(0, value));
}

export function fire(o2, psi) {
  const x = o2 / 100;
  const oxygenMass = (x * 32) / (x * 32 + (1 - x) * 28);
  const standoff = (AIR / Math.log(1 + oxygenMass / STOICH)) * Math.pow(14.7 / psi, 0.15);

  const heat = between0and1((o2 - 15) / 25);
  const press = between0and1((psi - 5) / 10);

  return {
    standoff,
    soot: between0and1(heat * 0.75 + press * 0.5 - 0.4),
    glow: 0.4 + heat * 0.55 + press * 0.25,
  };
}

export default function Flame({ o2, psi, size, rim, bright, radius, gain }) {
  const material = useRef();

  const uniforms = useMemo(
    () => ({
      uTime: { value: 0 },
      uSize: { value: 1 },
      uBright: { value: 1 },
      uRim: { value: rim },
      uSoot: { value: 0 },
    }),
    []
  );

  useFrame(({ clock }) => {
    const u = material.current.uniforms;
    const f = fire(o2, psi);
    u.uTime.value = clock.elapsedTime;
    u.uSize.value = radius.current * size;
    u.uSoot.value = THREE.MathUtils.lerp(u.uSoot.value, f.soot, 0.06);
    u.uBright.value = THREE.MathUtils.lerp(u.uBright.value, bright * f.glow * 1.1 * gain.current, 0.08);
  });

  return (
    <mesh>
      <sphereGeometry args={[1, 64, 64]} />
      <shaderMaterial
        ref={material}
        vertexShader={vertexShader}
        fragmentShader={fragmentShader}
        uniforms={uniforms}
        transparent
        depthWrite={false}
        blending={THREE.AdditiveBlending}
      />
    </mesh>
  );
}
