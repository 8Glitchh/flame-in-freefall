# Advanced Combustion via Microgravity Experiments (ACME) Integrated Science Requirements Summary

## Executive Summary
The Advanced Combustion via Microgravity Experiments (ACME) project encompasses independent fundamental combustion investigations conducted inside the Combustion Integrated Rack (CIR) [a290cad3d77b]. The research program focuses on gas-fueled laminar diffusion flames [a290cad3d77b], materials flammability, extinction behavior, electric-field flame control [f3132df89f31], and soot formation pathways [0bfe62a4e02e, 47f6ef8b9f65]. The findings establish rigorous hardware, operational, and sensor specifications to ensure high-fidelity data collection, equipment survivability in elevated oxygen and high-voltage environments, and enhanced spacecraft fire prevention and suppression capabilities.

---

## Research Overview
The ACME project comprises multiple specialized experimental investigations designed to advance fundamental combustion science and improve spacecraft fire safety:
* **Coflow Laminar Diffusion Flame (CLD Flame):** Extends predictive capabilities for flames at fuel dilution extremes, including sooty pure-fuel flames and near-extinction dilute flames [5bb91f1eac82].
* **Electric-Field Effects on Flames (E-FIELD Flames):** Investigates flame ion production and high-voltage DC electric fields (up to 10 kV) to control non-premixed flames, alter flame shape, modify soot and flammability limits, and manage heat transfer [f3132df89f31].
* **Flame Design (s-Flame / Flame Design):** Explores soot inception and extinction limits of spherical microgravity flames to optimize oxygen-enriched combustion and design robust, soot-free non-premixed flames [0bfe62a4e02e, 47f6ef8b9f65].
* **Burning Rate Emulator (BRE):** Focuses specifically on spacecraft fire prevention by assessing solid and liquid fuel burning behaviors, flammability limits, extinction behavior, and sustained combustion conditions using gaseous flat porous burners [38a029cff20d].

---

## Key Experimental Findings

### Burner Design, Fabrication, and Material Specifications
* **Spherical Burners:** Fabricated from sintered porous metal (with sintered bronze working best for s-Flame [f5365ba4a740] and 10-micron sintered stainless steel for Flame Design [ac503db10e8d]) and designed with outer diameters ranging from 1/8 to 1/2 inch [f5365ba4a740] (specifically 6.35 mm with a 1.59 mm hole diameter for Flame Design [ac503db10e8d]) to match ground-based testing thermal and catalytic properties [f18974c858c3].
* **Gas-Jet Burners:** Must feature straight tubes with an internal length at least 40 times greater than the inner diameter to establish a fully developed parabolic velocity profile at the nozzle tip [d922abba3225]. Burner tips must be free of burrs and sharp edges, smoothed to an average surface roughness $\le 20\,\mu\text{m}$ to prevent turbulence and corona discharges during high-voltage operations [9795d9ecbed9].
* **Electrical Conductivity:** Gas-jet and coflow burners must exhibit a resistance of $<1\,\Omega$ along their length and across outlet surfaces to function uniformly as ion current collection pathways [a71923ec5061].

### Thermal and Environmental Operating Limits
* **Oxygen Compatibility:** All CIR chamber contents must remain compatible with oxygen concentrations up to 40% by volume [64dfe51fabeb].
* **Temperature Thresholds:** Spherical burners and supply tubes must withstand temperatures from 0 to 450\,°C within 75 mm of their center [55c7156563d7]. Operational safety cutoffs dictate that if heat flux sensors exceed 300\,°C during BRE testing [3ea48c3c2b6f] or if burner surface temperature reaches 250\,°C [511d048772cb], gas flow is halted immediately.
* **Heat Flux Ranges and Transducers:** Schmidt-Boelter thermopile-type heat flux transducers are mandated over Gardon types due to minimal temperature variation across their surfaces [83dbd02fae90]. Measurement ranges span 0 to $50\,\text{kW/m}^2$ [247c04e00424], with drop tests indicating an initial ignition heat flux of approximately $50\,\text{kW/m}^2$ dropping to $5\,\text{kW/m}^2$ [ca1e0feb1e18]. Sensor body temperatures must not exceed Space Shuttle flight-qualification limits of 600\,°F (316\,°C) [e2cec28b7f06].

### Electrical Field Specifications
* **Power Supply:** The high-voltage DC electric field generator must deliver $-10\text{ kV}$ to $+10\text{ kV}$ with an accuracy of $\pm 0.1\%$ of the set point [854117e5ff2f].
* **Current Leakage and Resistance:** With $\pm 10\text{ kV}$ applied across a $35\text{ mm}$ electrode-to-burner gap at 1 bar absolute, leakage current in air must remain $<100\text{ nA}$ [893e6d02bf4c]. An insulation resistance of $200\text{ G}\Omega$ between the mesh electrode and chamber limits leakage to $0.05\text{ mA}$ at $10\text{ kV}$, maintaining negligible leakage compared to estimated flame currents of $\sim 1\text{ mA}$ [c117050d06bd]. Ion current measurement amplitudes must span 0 to $25\,\mu\text{A}$ [50a6cde3c55f].

### Optical and Thermal Diagnostics
* **Imaging Systems:** At least one imaging system must capture full-sensor frames at $\ge 20\text{ fps}$ with a bit depth of $3\times12$ [c92eb9649cd3]. Dual-view setups confirm axisymmetry and allow distinct camera configurations (e.g., one optimized for dim blue chemiluminescence without saturation, another for hot soot pyrometry) [e1c1ed37ddc0].
* **Optical Filtering:** Characterized filters (such as BG7 Schott glass, 430-nm, and 450-nm filters) reduce red/blackbody soot emissions relative to blue chemiluminescence to prevent sensor saturation [125388c5f1c1]. High-sensitivity detectors like the Hamamatsu H5784-06 exhibit sensitivity 1 to 2 orders of magnitude greater than the human eye [e3f815e60cbe].
* **Temperature and Flux Sensors:** Surface temperatures measured between 20 and 90 degrees of the burner tube require a precision of $\pm 2\,^\circ\text{C}$ and accuracy of $\pm 5\,^\circ\text{C}$ [25aaae4ff3ab, db929305e9b5]. Far-field temperature ranges must span 700 to 1700\,°C within 40 mm of window axes and 0 to 1250\,°C elsewhere [b043b96e9df5]. Thin filament pyrometry (TFP) utilizes 15-micron oxidized SiC fibers [029bf839abbf]. Radiant emission flux accuracy must be within $\pm 10\%$ [ff38b36a8a3e].

---

## Fire Safety Analysis

### Prevention
* **Material and Hardware Protection:** Elevated oxygen concentrations (up to 40%) elevate flame temperatures [64dfe51fabeb], which shortens the lifespan of traditional hot-wire igniters; Hot Surface Ignition (HSI) is identified as a more durable alternative [eac5e379c2e5]. Smooth burner tips ($\le 20\,\mu\text{m}$ roughness) prevent corona discharges under high-voltage electric fields [9795d9ecbed9]. 
* **Thermal Management:** Understanding that fuel types with higher laminar flame speeds (such as ethylene versus methane) experience halved lift-off heights helps prevent burner overheating [b7d639e32b2b]. Increasing fuel flow rates or dilution levels (e.g., $50\%\,\text{C}_2\text{H}_4 / 50\%\,\text{N}_2$) lifts sooting regions further from the burner surface, protecting hardware from thermal degradation [a55bf1a04726, 9ef8f0a1219b].

### Detection
* **Automated Extinction and Monitoring:** Flame extinction must be automatically detected to trigger operational sequence steps [c6c23e26889c]. High-sensitivity optical detectors (such as Hamamatsu photomultipliers) and high-speed framing ($\ge 20\text{ fps}$) enable early identification of faint combustion emissions, outperforming human visual capabilities [e3f815e60cbe].

### Suppression
* Electric fields (up to 10 kV) provide active ion transport and ion-wind mechanisms to manipulate non-premixed flames, alter flammability limits, and assist in flame control and extinction [f3132df89f31].

---

## Gravity and Mission Applicability

### Microgravity Environment (`micro-g`)
* Microgravity removes buoyancy-induced convection, altering flame shape, lift-off distance, soot distribution, and radiative/convective extinction limits. 
* Axial diffusion effects are exacerbated in microgravity, decreasing flame lift-off heights and increasing thermal risks to burners [b7d639e32b2b, 9ef8f0a1219b].
* S-Flame tests are constrained to a maximum duration of $25\text{ s}$ [d661bc7932e8]. Drop tests effectively simulate reduced-gravity transient burning behavior [ca1e0feb1e18].

### Lunar and Martian Mission Environments (`partial_g_applicability`)
* BRE and Flame Design findings assess the validity of existing terrestrial flammability test methods for low- and partial-gravity environments [38a029cff20d].
* Reliable ignition, burner thermal protection, and combustion predictability are directly applicable to long-duration spaceflight exploration vehicles and habitats operating under varied atmospheric compositions [eac5e379c2e5].

---

## Earth Applications
* Improved chemical kinetic and soot formation submodels enhance combustion efficiency and reduce pollutant emissions in practical terrestrial combustion devices [a290cad3d77b, 5bb91f1eac82, 0bfe62a4e02e].
* Findings support industrial burner design [0bfe62a4e02e, 83dbd02fae90], high-voltage electrostatic precipitators and insulation testing [893e6d02bf4c, c117050d06bd], high-oxygen industrial systems [64dfe51fabeb, eac5e379c2e5], and flare monitoring [e3f815e60cbe].

---

## Research Gaps and Limitations
* Extending predictive capabilities for turbulent combustion, coflow flame stability, and dilution extremes (pure sooty flames vs. near-extinction dilute flames) represents an ongoing area of model development [5bb91f1eac82].
* Predicting structural dynamics, radiative/convective extinction limits, and pulsating instabilities in spherical diffusion flames requires further experimental verification across varied diluents [47f6ef8b9f65].

---

## Key Conclusions
The ACME integrated science requirements successfully establish comprehensive experimental, hardware, and safety protocols for studying gas-fueled laminar diffusion flames in microgravity. By integrating rigorous material specifications, high-voltage electrical insulation standards, precise optical and thermal diagnostics, and automated safety cutoffs, the project ensures both high-fidelity fundamental combustion data collection and robust fire prevention safeguards for spacecraft environments.