export const vertexShader = `
uniform float uTime;
uniform float uSize;
varying vec3 vNormal;
varying vec3 vView;

void main() {
  vec3 p = position;
  float breathe = sin(uTime * 1.3) * 0.025 + sin(uTime * 0.7 + p.x * 2.0) * 0.012;
  p *= (1.0 + breathe) * uSize;

  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  vNormal = normalize(normalMatrix * normal);
  vView = normalize(-mv.xyz);
  gl_Position = projectionMatrix * mv;
}
`;

export const fragmentShader = `
uniform float uBright;
uniform float uRim;
uniform float uSoot;
varying vec3 vNormal;
varying vec3 vView;

void main() {
  float rim = pow(1.0 - abs(dot(vNormal, vView)), uRim);
  float core = 1.0 - rim;

  vec3 deepBlue = vec3(0.08, 0.18, 0.85);
  vec3 lightBlue = vec3(0.35, 0.6, 1.0);
  vec3 soot = vec3(0.8, 0.44, 0.14);

  vec3 color = mix(deepBlue, lightBlue, rim);
  color = mix(color, soot, uSoot * pow(core, 1.5) * 0.75);
  float alpha = rim * 0.8 + 0.08 + uSoot * core * 0.35;

  gl_FragColor = vec4(color * uBright, alpha * uBright);
}
`;
