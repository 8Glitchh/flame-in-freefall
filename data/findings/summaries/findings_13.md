# NASA Spacecraft Fire Safety and Combustion Research Summary: ACME Science Operation Requirements

## Executive Summary
This document summarizes the operational requirements, experimental procedures, and safety protocols for the Advanced Combustion Microgravity Experiment (ACME) facility, drawing from NASA technical documentation (`PSI-23_ACME_Science_Operation_Requirements_revA_20111018.pdf`). The ACME facility investigates fundamental gaseous combustion behaviors under microgravity conditions across multiple targeted investigations, including Coflow Laminar Diffusion Flames (ACME-CLD), Electric Field Effects on Flames (ACME-EFIELD), Flame Design, and Structure and Response of Spherical Flames (s-Flame / COOL-FLAME-TRANSITIONS) [2f3c91291d24, 0bc41cba62c7, 891b12b7265e, d34c723cab38]. The research establishes critical operational boundaries, automated detection and suppression responses, and diagnostic precisions necessary to advance predictive combustion models and spacecraft fire safety.

---

## Research Overview
The ACME project uses specialized gaseous fuel burners (such as coflow burners, gas-jet burners, and porous spherical burners) operating primarily in micro-g environments at pressures around 1 bar [6103d9c7cc6b, 387db1df4892]. Gaseous fuels investigated include methane ($\text{CH}_4$), ethylene ($\text{C}_2\text{H}_4$), and hydrogen ($\text{H}_2$) [2f3c91291d24, 891b12b7265e, d34c723cab38]. 

The primary investigations comprise:
- **ACME-CLD:** Examines coflow laminar non-premixed diffusion flames using gaseous fuels to extend predictive capabilities for chemical kinetics and soot formation under dilute and sooty conditions [2f3c91291d24].
- **ACME-EFIELD:** Studies the influence of high-voltage electric fields (-10 kV to +10 kV, AC/DC up to 100 Hz) on combustion ions, flame shape, soot, flammability limits, heat transfer, and pollutant emissions [0bc41cba62c7, 8e63e81d7135, ac9b132ad858].
- **ACME-DESIGN / s-Flame:** Explores soot inception, extinction limits (radiative and convective), and structure and dynamics of spherical microgravity flames using varied fuel and oxygen concentrations [891b12b7265e, d34c723cab38].

---

## Key Experimental Findings

### Prevention and Material Safety
- **Ignition Controls:** ACME igniters operate with precise voltage control (50% to 100% of maximum power with $\le 2\%$ precision) and duration control ($\le 0.1\text{ s}$ precision) [c3a753d5ae08]. Operational sequences dictate igniter retraction at $0\text{ s}$, followed by stabilization and data acquisition [e0ff168538f1].
- **Gas Delivery and Flow Precision:** Mass Flow Controllers (MFCs) must be capable of zeroing [b1c9ee3f6281], maintaining steady flows (0 to 100% range with $\le 0.1\%$ precision) [2a636ac9018b], stepping/ramping flows [0b2904bc7817, bdefdf7ae9cf, 77b487df467d, 75014d8e22dc], and venting/purging all gas delivery lines to prevent accidental pre-ignition mixing [077eaa83f435]. Solenoid valves manage complete isolation of gas supplies [906727bc7739].
- **High-Voltage and Electrical Safety:** Electric field application requires operational ranges from -10 kV to +10 kV ($\pm 0.1\%$ accuracy) and alternating frequencies up to 100 Hz [8e63e81d7135, ac9b132ad858]. Because soot deposition on gas-jet burners can cause high electrical leakage currents, procedures mandate burner cleaning or test termination if leakage exceeds acceptable thresholds [d8fd8a906eb7, a543c455f6c2, 7813974d7589]. Background leakage measurements without a flame are integrated into test sequences [5eefa603f051, 7813974d7589].
- **Hardware Sealing Verification:** Following any operation where the Combustion Integration Rack (CIR) chamber is opened, system integrity checks must verify that the chamber is gas-tight [7e0ff6cc23b4].

### Detection and Monitoring
- **Flame Extinction Sensing:** Non-imaging sensors—including radiometers, photomultiplier tubes (PMTs), and thermopile detectors—continuously monitor flame status [6c7cb0d7bf8e]. Extinction detection functions must operate simultaneously with gas flowing, data acquisition, and electric field activation [26d2eeec3081].
- **Test Logging:** Detailed time logs of commands and events must be maintained to distinguish between natural flame extinction and commanded flow termination [be2e6e985010].
- **Operational Test Limits:**
  - *CLD Extinction Limit Tests:* Methane or ethylene flames are run with fuel concentration reductions or velocity ramps up to $50\text{ cm/s}$ (ramp rate $0.5\text{ cm/s}^2$) until PMT extinction detection occurs [6103d9c7cc6b].
  - *CLD Sooting Limit Tests:* Ethylene flames test concentrations (40%, 45%, 50%) with velocities up to $35\text{ cm/s}$ or pre-determined smoke points [387db1df4892].

### Suppression and Automated Response
- **Automated Fuel Shut-Off:** Upon detecting flame extinction or blowout (including during E-FIELD voltage stepping), ACME systems automatically respond by setting all gas flows to zero after a specified delay ($\le 0.1\text{ s}$ precision, range 0.0 to $99.99\text{ s}$) or transitioning directly to shutdown steps [775092075c83, 65d3abc936ec, c4475eae9f98].
- **Override Capabilities:** Operators retain the ability to deactivate extinction detection parameters when required for specific test sequences [3e1ecab470d2].

---

## Fire Safety Analysis
The experimental requirements directly address primary spacecraft fire safety hazards:
- **Prevention of Unburnt Fuel Accumulation:** Immediate automated zeroing of gas flows upon extinction detection prevents the buildup of unburnt flammable gases, mitigating secondary deflagration or explosion risks [775092075c83].
- **Electrical Hazard Mitigation:** High-voltage electric field testing introduces potential short-circuit risks due to conductive soot buildup. Mandatory baseline leakage checks and soot-cleaning protocols protect flight hardware from electrical damage [d8fd8a906eb7, a543c455f6c2, 5eefa603f051, 7813974d7589].
- **Pressure Boundary Integrity:** Post-maintenance chamber seal verification safeguards pressurized habitats against depressurization or toxic product leakage [7e0ff6cc23b4].

---

## Gravity and Mission Applicability
- **Microgravity Environment (`micro-g`):** All combustion tests (CLD, E-FIELD, Flame Design, s-Flame) rely on microgravity to eliminate natural buoyancy-driven convection, enabling the observation of fundamental chemical kinetic, soot, and extinction behaviors unobscured by gravity [2f3c91291d24, 891b12b7265e, d34c723cab38, 4239d289e382].
- **Lunar and Martian Habitats:** Chamber sealing verification and automated extinction/shut-off protocols are directly applicable to pressurized exploration habitats and spacecraft operating in reduced or microgravity environments [7e0ff6cc23b4, 26d2eeec3081].

---

## Research Gaps and Limitations
- The provided documentation outlines operational requirements and procedures but does not explicitly detail unresolved theoretical combustion gaps beyond noting the need to extend predictive capabilities for chemical kinetics, soot formation under dilute/sooty conditions, and low-convection extinction boundaries [2f3c91291d24, d34c723cab38].

---

## Earth Applications
Findings and technologies developed through ACME translate directly to terrestrial systems:
- **Industrial Combustion & Emission Control:** Improving computational combustion models helps optimize industrial burners, increase fuel efficiency, and reduce pollutant emissions (`$\text{NO}_x$`, smoke) [2f3c91291d24, 0bc41cba62c7, 891b12b7265e].
- **Active Flame Control:** Utilizing DC and AC electric fields provides advanced methods for controlling flame stability, shaping flames, and mitigating soot in industrial systems [0bc41cba62c7, ac9b132ad858].
- **Safety Systems:** Rapid extinction sensing, automated gas shut-off valves, and high-voltage insulation monitoring enhance safety protocols in industrial boilers, domestic appliances, and high-voltage combustion machinery [6c7cb0d7bf8e, 775092075c83, 7813974d7589].

---

## Key Conclusions
- ACME provides a rigorously controlled, automated microgravity combustion facility capable of simultaneous gas flow, imaging, electric field application, and extinction sensing [26d2eeec3081].
- Precise control over ignition, mass flow rates, and high-voltage electric fields ensures repeatable data acquisition while maintaining strict safety boundaries against fuel leaks, blowouts, and electrical shorts [c3a753d5ae08, 2a636ac9018b, 8e63e81d7135, 7813974d7589].
- Automated safety responses—such as immediate gas flow cessation upon extinction detection—provide vital risk mitigation models for crewed spacecraft and habitat fire safety [775092075c83].