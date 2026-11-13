import { useRef, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Edges, Html, Line, OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import { moonZone, tests } from "../data/tests.js";

const SIZE = 10;
const HEIGHT = 6;
const range = { psi: [5, 16], o2: [15, 40], co: [0, 360] };

const materialColor = { PMMA: "#0a84ff", "SIBAL fabric": "#bf5af2", Cotton: "#30d158" };

const scale = (v, [a, b], size) => ((v - a) / (b - a)) * size;
const px = (psi) => scale(psi, range.psi, SIZE) - SIZE / 2;
const pz = (o2) => SIZE / 2 - scale(o2, range.o2, SIZE);
const py = (co) => scale(co, range.co, HEIGHT);

export default function View3D({ active }) {
  return (
    <div className="h-full px-8 pb-24 pt-20">
      <div className="card arrive relative h-full overflow-hidden">
        <Canvas camera={{ position: [11, 8, 12], fov: 38 }} dpr={[1, 2]} frameloop={active ? "always" : "never"}>
          <color attach="background" args={["#2c2c2e"]} />
          <fog attach="fog" args={["#2c2c2e", 22, 40]} />
          <ambientLight intensity={0.7} />
          <directionalLight position={[6, 12, 8]} intensity={1.4} />

          <group position={[0, -2.2, 0]}>
            <Floor />
            <Walls />
            <MoonZone />
            <LimitPlane />
            {tests.map((t, i) => (
              <Point key={t.id} test={t} delay={i * 0.08} />
            ))}
            <AxisLabels />
          </group>

          <OrbitControls enableDamping dampingFactor={0.08} enablePan={false} minDistance={10} maxDistance={28} maxPolarAngle={Math.PI / 2.1} autoRotate autoRotateSpeed={0.35} />
        </Canvas>
      </div>
    </div>
  );
}

function Floor() {
  return (
    <group>
      <mesh rotation-x={-Math.PI / 2} position-y={-0.001}>
        <planeGeometry args={[SIZE, SIZE]} />
        <meshStandardMaterial color="#232325" />
      </mesh>
      <gridHelper args={[SIZE, 10, "#48484a", "#3a3a3c"]} />
    </group>
  );
}

function Walls() {
  return (
    <group>
      <gridHelper args={[SIZE, 10, "#3a3a3c", "#333335"]} rotation-x={Math.PI / 2} position={[0, HEIGHT / 2, -SIZE / 2]} scale={[1, 1, HEIGHT / SIZE]} />
      <gridHelper args={[SIZE, 10, "#3a3a3c", "#333335"]} rotation-z={Math.PI / 2} position={[-SIZE / 2, HEIGHT / 2, 0]} scale={[HEIGHT / SIZE, 1, 1]} />
    </group>
  );
}

function MoonZone() {
  const x0 = px(moonZone.psi[0]);
  const x1 = px(moonZone.psi[1]);
  const z0 = pz(moonZone.o2[1]);
  const z1 = pz(moonZone.o2[0]);
  return (
    <mesh position={[(x0 + x1) / 2, HEIGHT / 2, (z0 + z1) / 2]}>
      <boxGeometry args={[x1 - x0, HEIGHT, z1 - z0]} />
      <meshStandardMaterial color="#ff9f0a" transparent opacity={0.1} depthWrite={false} />
      <Edges color="#ff9f0a" />
    </mesh>
  );
}

function LimitPlane() {
  return (
    <mesh rotation-x={-Math.PI / 2} position-y={py(100)}>
      <planeGeometry args={[SIZE, SIZE]} />
      <meshBasicMaterial color="#ff453a" transparent opacity={0.035} side={THREE.DoubleSide} depthWrite={false} />
      <Edges color="#ff453a" />
    </mesh>
  );
}

function Point({ test, delay }) {
  const group = useRef();
  const [hover, setHover] = useState(false);
  const start = useRef(null);
  const color = materialColor[test.material];
  const target = py(test.co);

  useFrame(({ clock }) => {
    if (start.current === null) start.current = clock.elapsedTime + delay;
    const t = Math.min(1, Math.max(0, (clock.elapsedTime - start.current) / 0.9));
    group.current.position.y = target * (1 - Math.pow(1 - t, 3));
    group.current.scale.setScalar(THREE.MathUtils.lerp(group.current.scale.x, hover ? 1.6 : 1, 0.15));
  });

  return (
    <group position={[px(test.psi), 0, pz(test.o2)]}>
      <Line points={[[0, 0, 0], [0, target, 0]]} color={color} lineWidth={1} transparent opacity={0.35} />
      <mesh rotation-x={-Math.PI / 2} position-y={0.01}>
        <ringGeometry args={[0.12, 0.18, 32]} />
        <meshBasicMaterial color={color} transparent opacity={0.5} />
      </mesh>
      <group ref={group}>
        <mesh
          onPointerOver={(e) => {
            e.stopPropagation();
            setHover(true);
            document.body.style.cursor = "pointer";
          }}
          onPointerOut={() => {
            setHover(false);
            document.body.style.cursor = "";
          }}
        >
          <sphereGeometry args={[0.2, 32, 32]} />
          <meshStandardMaterial color={color} emissive={color} emissiveIntensity={0.6} roughness={0.3} />
        </mesh>
        {hover && (
          <Html center position={[0, 0.7, 0]} style={{ pointerEvents: "none" }}>
            <div className="whitespace-nowrap rounded-[10px] bg-[#3a3a3c] px-3 py-2 text-[12px] shadow-xl">
              <p className="font-semibold">Saffire {test.id} · {test.material}</p>
              <p className="text-[var(--fg-2)]">{test.o2}% O₂ · {test.psi} psi · CO {test.co} ppm</p>
            </div>
          </Html>
        )}
      </group>
    </group>
  );
}

function Label({ position, children }) {
  return (
    <Html center position={position} style={{ pointerEvents: "none" }}>
      <span className="whitespace-nowrap text-[12px] font-medium text-[var(--fg-2)]">{children}</span>
    </Html>
  );
}

function AxisLabels() {
  return (
    <group>
      <Label position={[0, 0, SIZE / 2 + 0.9]}>Pressure (psi)</Label>
      <Label position={[SIZE / 2 + 1.1, 0, 0]}>Oxygen (%)</Label>
      <Label position={[-SIZE / 2, HEIGHT + 0.5, -SIZE / 2]}>Peak CO (ppm)</Label>
      <Label position={[-SIZE / 2, 0, SIZE / 2 + 0.5]}>{range.psi[0]}</Label>
      <Label position={[SIZE / 2, 0, SIZE / 2 + 0.5]}>{range.psi[1]}</Label>
      <Label position={[SIZE / 2 + 0.5, 0, -SIZE / 2]}>{range.o2[1]}</Label>
      <Label position={[SIZE / 2 + 0.5, 0, SIZE / 2]}>{range.o2[0]}</Label>
      <Label position={[-SIZE / 2 - 0.4, py(100), -SIZE / 2]}>100</Label>
      <Label position={[-SIZE / 2 - 0.4, HEIGHT, -SIZE / 2]}>{range.co[1]}</Label>
    </group>
  );
}
