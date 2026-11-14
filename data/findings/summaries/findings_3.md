# Smoke Aerosol Measurement Experiment (SAME) Baseline Concept and Fire Safety Summary

### Executive Summary

Microgravity combustion and thermal degradation behave fundamentally differently than in normal Earth gravity, necessitating specialized fire safety, prevention, detection, and suppression strategies for crewed spacecraft [54172d80e912]. The Smoke Aerosol Measurement Experiment (SAME), along with risk-mitigation precursor evaluations such as the Dust and Aerosol Measurement Feasibility Test (DAFT), addresses critical knowledge gaps regarding smoke generation, particulate sizing, and aerosol transport under microgravity conditions [0f92bf32e36e, c96fc7d26e0b]. By evaluating standard spacecraft materials (Teflon, Kapton, silicone rubber, cellulose/lamp wick, and dibutyl phthalate) across controlled airflow velocities, weight loss rates, and aging durations, the SAME investigation generates benchmark aerosol data [df531a90a823, 5ccf6d897c19]. These findings directly inform the performance and reliability of existing and next-generation spacecraft fire detection systems [d88741a733b4].

---

### Research Overview

Spacecraft fire detection relies on understanding how diverse materials pyrolyze and generate smoke in reduced-gravity environments. Previous flight work, such as the Comparative Soot Diagnostics (CSD) experiment on STS-75, demonstrated that particulate smokes formed in microgravity aggregate into longer chains and larger particles compared to normal gravity equivalents [1fa0cdf58981]. This difference is attributed to increased residence times within high-concentration smoke regions [00f5d36e5272]. 

The SAME investigation expands on these observations by quantifying droplet sizes, particle counts, and mass concentrations of smokes produced from multiple spacecraft materials [0f92bf32e36e, 50e969a248c3]. The experimental hardware architecture includes:
* **Sample Carousel Assemblies:** Housing five test materials (Teflon, Kapton, silicone rubber, lamp wick, and dibutyl phthalate) wrapped in resistive wire coils that serve as both heating elements and resistance temperature detectors [df531a90a823].
* **Aging Chamber Assembly:** Utilizing a Rulon piston, mass flow controller, and internal Mixing Fan to ensure homogeneous sample distribution before disbursal [8bdab672e4cc].
* **Dynamic Diagnostics Assembly (DDA):** Integrating International Space Station (ISS) and Space Transportation System (STS) smoke detectors alongside sampling ports [23b124b41261].
* **Commercial Diagnostics Enclosure (CDE) & P-Trak Enclosure:** Housing flight-hardened TSI DustTrak, TSI P-Trak ultrafine particle counters, and modified First Alert ionization smoke detectors [4a62ee36e458, e1bed4b32b4e].
* **Dynamic Diluter:** Utilizing a laminar flow element and differential pressure transducer to adjust sample dilution setpoints within approximately 5 seconds [4146fe039b57].

---

### Key Experimental Findings and Test Matrix

Different fuels produce distinct smoke types: hydrocarbon fuels form soot, overheated plastics yield recondensed polymer fragment droplets, and paper and silicone rubber produce liquid droplets of recondensed pyrolysis products [4a051b107146]. To establish comprehensive baseline data, the SAME test matrix evaluates each material across specific air flows, weight loss rates, and aging durations [5ccf6d897c19]:

| Test ID | Material | Air Flow (cm/s) | Weight Loss Rate (mg/min) | Aging Duration (min) | Supporting Finding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Teflon | 5 | 2 | 1 | [5ccf6d897c19] |
| 2 | Teflon | 5 | 1 | 1 | [54ac8920f4e9] |
| 3 | Teflon | 5 | 2 | 20 | [21e1c60fe8c9] |
| 4 | Teflon | 10 | 2 | 1 | [37416cb23604] |
| 5 | Kapton | 5 | 2 | 1 | [67ebf0af7fdb] |
| 6 | Kapton | 5 | 1 | 1 | [b05a7b051c49] |
| 7 | Kapton | 5 | 2 | 20 | [6be71273f3df] |
| 8 | Kapton | 10 | 2 | 1 | [c0e962110155] |
| 9 | Silicone Rubber | 5 | 2 | 1 | [7870d63c5c24] |
| 10 | Silicone Rubber | 5 | 1 | 1 | [b6f24fa014c9] |
| 11 | Silicone Rubber | 5 | 2 | 20 | [9b6f8b0e9e31] |
| 12 | Silicone Rubber | 10 | 2 | 1 | [5d931c35d4e3] |
| 13 | Lamp Wick | 5 | 2 | 1 | [1ae280f43a15] |
| 14 | Lamp Wick | 5 | 1 | 1 | [047f58265b26] |
| 15 | Lamp Wick | 5 | 2 | 20 | [4390ceca7591] |
| 16 | Lamp Wick | 10 | 2 | 1 | [e66217a2aec9] |
| 17 | Dibutyl Phthalate | 5 | 2 | 1 | [bdfd1b5cf76b] |
| 18 | Dibutyl Phthalate | 5 | 1 | 1 | [52492da16e7d] |
| 19 | Dibutyl Phthalate | 5 | 2 | 20 | [6dd6dd5af1dc] |
| 20 | Dibutyl Phthalate | 10 | 2 | 1 | [8771cfda7f28] |

Additionally, idealized liquid aerosol smokes such as dibutyl phthalate (DBT) are measured in both microgravity and 1-g to validate numerical models [9934bb26d7a8].

---

### Fire Safety Analysis

#### Prevention and Mechanical Safety
* **Pressurization & Electrical Controls:** Pressurized lines and fittings are engineered to a factor of safety of 4.0 relative to a Maximum Design Pressure (MDP) of 200 psid (matching ISS $N_2$ limiting pressure), while pressurized system components utilize a factor of safety $\ge 2.5$ [48bededfe39b]. In the event of a power loss, all solenoids and mass flow controllers automatically close to prevent over-pressurization [4aa7e6417142].
* **Laser and Radiation Safety:** Diagnostic instruments incorporate fully contained Class 1 lasers meeting ANSI Z136.1-2000 standards without crew access [10fd92300a69]. Ionization-based smoke detectors house $1\ \mu\text{Ci}$ of Americium-241 safely inside their original housings [1c538322403b].

#### Detection and Sensor Performance
* **Detector Responsiveness:** Microgravity-induced soot aggregation alters particle size distribution, impacting the detection thresholds and reliability of ISS and STS smoke detectors [1fa0cdf58981, 00f5d36e5272]. 
* **Visual vs. Invisible Smoke:** Experience demonstrates that clearly visible smoke streams are not always detected by standard smoke detectors, whereas invisible smoke streams can be readily detected [b28b804f7f09]. Multi-sensor validation (combining optical scattering DustTrak, condensation particle counting P-Trak, ionization alarms, and thermal precipitators) is necessary to ensure reliable early warning [0f92bf32e36e, 50e969a248c3, e1bed4b32b4e].

#### Products, Toxicity, and Containment
* **Toxic Byproducts:** Teflon pyrolysis products initially register a JSC Toxicity level of 3 for 5 minutes after creation before particles coalesce and toxicity drops to level 0 [e26f5c366e7f]. 
* **Multi-Barrier Containment:** Smoke is contained within the smoke tube and aging chamber for 5 minutes before being expelled through HEPA filters into the ISS vent or the Microgravity Science Glovebox (MSG) [7379755f0140]. The MSG operates under negative pressure to provide secondary containment and prevent cabin contamination [7379755f0140].

---

### Gravity and Mission Applicability

* **Microgravity (Spacecraft & ISS):** Altered buoyancy, diffusion rates, and prolonged smoke residence times in weightlessness modify particle aggregation and transport [54172d80e912, 1fa0cdf58981, 00f5d36e5272]. Spacecraft fire safety systems cannot rely exclusively on Earth-derived methods [54172d80e912]. Hardware modifications—such as machining sixty $0.006$-inch capillary grooves inside the P-Trak condenser—are required to allow alcohol droplets to wick back to the reservoir, substituting for gravity-driven drainage and preventing sensor flooding or false high counts [4094cc96b8b6].
* **Universal Applicability:** Safety standards regarding fully enclosed Class 1 lasers and Americium-241 radioactive sources apply universally regardless of gravity level [10fd92300a69, 1c538322403b].

---

### Research Gaps and Limitations

* **Condensation Particle Counter Limitations:** In microgravity, condensed alcohol droplets inside instrumentation like the P-Trak can form films that bridge and block internal nozzles or circulate within optics chambers, creating false high particle counts or sensor failure [6a380816c38c]. 
* **Post-Flight Mass Verification:** Certain physical properties, such as sample mass loss and burn-rate quantification, require retention of sample carousels for post-flight weighing upon return to Earth [34e49ef36c36].

---

### Earth Applications

Insights gained from microgravity combustion and aerosol measurement directly benefit terrestrial applications by:
* Improving general combustion theory and fire safety [54172d80e912].
* Refining smoke detection algorithms and particulate matter sensing for commercial, industrial, and residential building materials [4a051b107146, 0f92bf32e36e].
* Supporting the validation of general aerosol dynamics models used in environmental health, cleanroom monitoring, and industrial hygiene [9934bb26d7a8, 4a62ee36e458].
* Enhancing toxic product generation assessments during thermal degradation of wiring, electrical insulation, and structural polymers [df531a90a823].