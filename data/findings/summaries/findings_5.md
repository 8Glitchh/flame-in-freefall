# Advanced Combustion via Microgravity Experiments (ACME) Project Summary

## Executive Summary
The Advanced Combustion via Microgravity Experiments (ACME) project is a comprehensive research initiative comprising five independent investigations focused on advancing combustion technology through fundamental microgravity experimentation [d782e6b8ee20]. The project utilizes gaseous fuels and simulated material burning to investigate flame structure, soot formation, electric field effects, extinction limits, and heat flux dynamics [d782e6b8ee20, 25d5bd80a933]. Findings from the ACME project provide critical baseline data and computational model verifications to enhance spacecraft fire prevention, optimize suppression strategies, and improve the reliability of aerospace instrumentation.

---

## Research Overview
The ACME project encompasses five primary investigations:
1. **Coflow Laminar Diffusion Flame (CLD Flame):** Develops and verifies chemical kinetic and soot formation submodels under diluted and sooty fuel conditions [bd74671b5ad8].
2. **Electric-Field Effects on Flames (E-FIELD):** Examines the influence of electric fields on ion transport, flame shape, soot limits, heat transfer, and pollutant reduction [8ac8d7896144].
3. **Flame Design:** Investigates soot inception and radiative extinction limits of spherical microgravity flames to design robust, soot-free combustion systems [dc2356ac6f5d].
4. **Structure and Response of Spherical Flames (s-Flame / SPICE):** Advances the prediction of structure, dynamics, and radiative/convective extinction in soot-free and sooty spherical flames [ba7ce814488d].
5. **Burning Rate Emulator (BRE):** Emulates material burning behavior using gaseous fuel mixtures to study flammability limits and heat release characteristics for spacecraft fire prevention [25d5bd80a933].

---

## Key Experimental Findings

### Burner Design, Hardware Specifications, and Tolerances
- **Spherical Burners:** Used in Flame Design and s-Flame, these burners feature fixed outer diameters of 6.4 mm, 9.5 mm, and 12.7 mm (within ±0.3 mm tolerance and known to ±0.1 mm) [4ba8f03762e5]. Sintered porous metal is optimal for spherical burners compared to porous ceramic or electric discharge machined (EDM) hollow spheres, though commercial sphere acceptance rates range from 30% down to 1 in 10 [f49c94c7510b, 418d7d38f3ad]. Flame Design spherical burners specifically utilize 10-micron sintered stainless steel with a 6.35 mm outside diameter and 1.59 mm hole diameter [61efedc90d43].
- **Thermal Endurance of Burners:** Spherical burner assemblies and supply tubes must withstand temperatures from 0 to 450 °C within 75 mm of their center [4455a0475eaa]. Gas-jet burner tips must withstand 0 to 1000 °C within 50 mm of their tips [e51960dd3423]. BRE burner top plates must maintain an emissivity of at least 0.85 across 0.6–15 µm to minimize heating transients and soot deposition dependencies [db1739021b7a].
- **Nozzle and Coflow Flow Quality:** Gas-jet burner tubes require a length at least 40 times their inner diameter to establish a parabolic velocity profile at the nozzle tip [68001e7f1fc7]. Nozzles must be internally and externally smooth (average roughness $\le 100$ µm), with tips smoothed to $\le 20$ µm [29261dc44dcd]. Coflow burner inner tubes must maintain a constant 2.1 mm inner diameter for a length of $\ge 40$ times the inner diameter [fa1cef492036], with axial velocity variations across angular positions held under 10% of mean velocity across 0 to 10 mm radial positions [8c1d7d54f3df]. Burners functioning as electrodes must maintain electrical resistance under 1 Ohm along their length and across outlet surfaces [57f53e4b809c].

### Gas Delivery and Ignition Systems
- **Mixture Precision:** Gas delivery systems must control reactant mixture compositions to within ±0.01 mole fraction [2a2fc2e11190]. Microgravity flames exhibit high sensitivity to small shifts (e.g., 0.01 mole fraction) in oxygen concentration near soot, stability, and extinction limits [05de52a6fcbe].
- **Ignition Hardware:** Elevated oxygen testing for Flame Design results in high flame temperatures that can shorten hot-wire igniter lifespans, suggesting Hot Surface Ignition (HSI) is preferable [8f308848f14c].

### Electrical and High-Voltage Constraints
- **Leakage Currents:** At 1 bar absolute, applying -10 kV and +10 kV electric fields across a 35 mm axial gap between an electrode mesh and burner must result in leakage currents under 100 nA [299dc340bb61]. An effective insulation resistance of 200 Giga-ohms between the mesh electrode and chamber limits leakage current to 0.05 mA at 10 kV, which is negligible compared to estimated ~1 mA flame currents [91856c2b4437].
- **Sensor Ranges:** Ion current measurement amplitudes must span at least 0 to 25 µa [d4d63ece96d0].

### Optical Diagnostics and Instrumentation
- **Camera Configurations and Filters:** Dual-camera arrangements verify flame axisymmetry and allow independent optical filtering—one camera images dim blue chemiluminescence (saturating in hot soot regions), while the second images hot soot without saturation for pyrometry [c7817f3450f4]. Schott glass BG7 filters reduce blackbody red soot emission relative to blue chemiluminescent emission to prevent detector saturation [e2ea757640b5].
- **Photomultiplier Sensitivity:** Ground testing at 1g demonstrated that the Hamamatsu H5784-06 photomultiplier tube is 1 to 2 orders of magnitude more sensitive than the human eye when viewing blue and yellow ethylene Santoro burner flames at a 120 mm distance [69a551d370a8].
- **Heat Flux Transducers:** BRE burners use Schmidt-Boelter thermopile heat flux transducers (rather than Gardon types) to minimize surface temperature variations that distort heat transfer analysis [f1761de3c7d4]. The measurement range is 0 to 50 kW/m² [1b5b2dad1632]. Medtherm flight-qualified sensors support linear over-ranging up to 150%, but sensor body temperatures must not exceed 600 °F (316 °C) [cd4d3301ceff, a4614657c346]. Drop tests indicate initial ignition heat fluxes of ~50 kW/m², dropping to ~5 kW/m² during steady testing [e30d2511124f].

---

## Fire Safety Analysis

### Prevention
- **Thermal Management & Burner Integrity:** Heavily sooting ethylene flames generate moderate heat transfer to burner surfaces under microgravity, elevating hardware thermal risk due to enhanced soot propensity and reduced lift-off heights [e1eaef851c95]. A 50% $\text{C}_2\text{H}_4$ / 50% $\text{N}_2$ dilution level ensures a stable room-temperature boundary condition at the burner [fa633eb36996]. Methane and non-sooting ethylene flames experience a 2-fold decrease in lift-off height due to higher laminar flame speeds, though without causing burner heating [8d39f3fd4f5c].
- **Probe Disturbance Minimization:** Physical probes for gas-jet and spherical burners must be smaller than 250 µm [7f0377df9ea3]. Spherical burner surface temperature probes placed between 20° and 90° from the burner tube are verified via 2.2-second drop tower tests to ensure they do not disrupt visible flame symmetry [3b21a5bb13a9].

### Detection and Automated Control
- **Extinction Triggers:** Flame extinction is automatically detected using combined photomultiplier tube (PMT) measurements and color imaging to initiate operational sequence steps [0752379b50f3]. Spherical Flame Design radiative extinction tests utilize PMT or real-time video detection followed by flow reductions [051aed61010b].
- **Safety Cutoffs:** BRE operational tests automatically halt reactant flow immediately if flames extinguish or if heat flux sensors exceed a critical temperature of 300 °C (burner surface limit: 250 °C) [84b03e326207].

### Suppression and Control via Electric Fields
- Electric fields interact with combustion-generated ions and induced ion winds to modify flame shapes, alter soot and flammability limits, direct heat transfer, reduce pollutant emissions [8ac8d7896144], and provide open-loop sensing/control via ion current and luminosity fluctuation monitoring [6499b340418e].

---

## Gravity and Mission Applicability
- **Microgravity Environment:** Experiments rely heavily on microgravity to eliminate buoyancy-induced flows, allowing observation of spherical diffusion flames [ba7ce814488d, c7817f3450f4], pure radiative extinction [051aed61010b], and enhanced soot propensity [e1eaef851c95]. 
- **Spacecraft Operations & Vibration Isolation:** Based on SPICE findings, combustion testing must not occur during thruster firings or spacecraft dockings/undockings [457efbf5a2dd]. Normal International Space Station (ISS) operations provide adequate acceleration environments, particularly when utilizing the Combustion Integration Rack (CIR) equipped with a Passive Rack Isolation System (PaRIS) [457efbf5a2dd]. Maximum test durations for s-Flame are constrained to 25 seconds [32d17d515dae]. Normal-gravity baseline coflow flames are comparatively small (<2.5 cm tall, ~0.6 cm diameter) [c58b5c9ba701].

---

## Earth Applications
Findings from the ACME project support terrestrial combustion applications, including:
- Improving efficiency and reducing emissions in practical combustion processes through enhanced computational fluid dynamics (CFD) models [d782e6b8ee20].
- Assessing and improving existing flammability test methods and standardized burner designs [25d5bd80a933, 4ba8f03762e5, 73682526b2ad].
- Minimizing electrical breakdown/arcing risks in high-voltage electrostatic apparatuses and industrial burners [29261dc44dcd, 57f53e4b809c].
- Advancing optical flame sensing sensitivity specifications, non-intrusive probe placement, and thermal protection/automated shutoff controls for industrial furnaces [3b21a5bb13a9, 69a551d370a8, a4614657c346].