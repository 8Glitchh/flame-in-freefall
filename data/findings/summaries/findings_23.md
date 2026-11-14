# SAFFIRE Objectives, Development, and Status: Spacecraft Fire Safety Research Summary

## Executive Summary
The Spacecraft Fire Experiment (SAFFIRE) series investigates large-scale flame growth, material flammability limits, combustion product generation, and post-fire atmospheric recovery in microgravity and exploration environments [42164085ccc0, 4875013971e3, 0c595c91168d, eebbafd29382]. Because normal-gravity flammability standards (such as NASA-STD-6001 Test 1) do not fully account for gravity-induced buoyancy effects on extinction limits and material behavior in long-duration spaceflight, the SAFFIRE program provides critical empirical data to validate computational fire growth, transport, and detection models [4875013971e3, 0c595c91168d, 76aa9d0acd01]. 

---

## Research Overview
The SAFFIRE investigations span multiple mission increments (SAFFIRE-I through VI) utilizing automated payloads integrated within the Cygnus Pressurized Cargo Module (PCM) following its departure from the International Space Station (ISS) [40ab29fb659b, 8fb150f1ebba, 0c595c91168d]. The research program addresses two primary scales and configurations:
* **Large-Scale Planar and Complex Geometries:** Large material samples (approximately 0.94 meters long and 0.4 meters wide) evaluate extensive flame spread, steady-state spread rates, and fire growth over realistic clothing/fabric materials (e.g., SIBAL cloth) and structural configurations [42164085ccc0, 588e9be1ce1d, e7b07ce1c765, 3ea2fcc38c62, 9fb95d1874df].
* **Material Flammability Test Cards:** Multi-sample cards assess specific material thicknesses, ignition locations, boundary transitions, and atmospheric conditions (including elevated oxygen and reduced pressure exploration atmospheres) [7fc29101b10f, eebbafd29382].

---

## Key Experimental Findings

### Material Configurations and Flow Conditions
* **SAFFIRE-I & III:** Utilize large composite fabric samples consisting of 75% cotton and 25% fiberglass by weight (SIBAL cloth) under forced air flow velocities of 20 cm/s (SAFFIRE-I) and 30 cm/s (SAFFIRE-III) [588e9be1ce1d, e7b07ce1c765].
* **SAFFIRE-II Sample Card:** Contains 9 distinct material samples measuring 5 cm x 29 cm to evaluate flammability limits across various thicknesses, ignition positions, and material boundaries [7fc29101b10f]:
  * **Silicone:** Tested at thicknesses of 0.25 mm (Sample S1, 20 cm/s flow, upstream igniter), 0.61 mm (Sample S2, 20 cm/s flow, upstream igniter), 1.02 mm (Sample S3, 20 cm/s flow, upstream igniter), and 0.36 mm (Sample S4, 20 cm/s flow, downstream igniter) [00ae78cd1f42, 05cc3901b810, 5e3ad7366dec, 713937a6b2ce].
  * **SIBAL Fabric:** Tested at 0.33 mm thickness under 20 cm/s flow (Sample S5, upstream igniter) and 30 cm/s flow (Sample S6, upstream igniter) [223f361f461a, d3cc23c71745].
  * **Material Transitions:** PMMA-to-Nomex transition at 0.33 mm thickness (Sample S7, 20 cm/s flow, upstream igniter) [02d1c4ae675d].
  * **Polymers (PMMA):** Structured PMMA at 10 mm thickness with tapered ignition edge (Sample S8, 20 cm/s flow, upstream igniter) and flat PMMA at 10 mm thickness with tapered ignition edge (Sample S9, 30 cm/s flow, upstream igniter) [caecd7d3e54c, ac9a0b9d3a3a].

### Instrumentation and Diagnostics
The flight hardware integrates comprehensive sensor suites to monitor thermal, optical, and chemical parameters during combustion:
* **Thermal Sensors:** Inlet and outlet flow duct thermocouples monitor flow temperature; embedded sample thermocouples measure flame temperature; individual thermocouples track plume temperature [fe68371f782d, 140eb26bff0b, 823881d343ee]. Four radiometers (two viewing the front, two viewing the back) quantify flame radiation heat transfer [a9709b0c9352].
* **Gas and Environmental Sensors:** Solid-state sensors measure $CO_2$ mole fraction (in the avionics bay), $O_2$ mole fraction (at the avionics bay inlet), and static pressure (in the avionics bay) [0ddc00e017f8, 046d7df64010, e1a1d4274f2f]. Two anemometers (one on each side of the sample) monitor flow velocity, while a leading-edge smoke wire verifies flow uniformity [7b5644cc5360, ab85818d2871].
* **Visual Data:** Dual cameras capture primary flame images of the sample front [78f25f1ddccc].

---

## Fire Safety Analysis

### Prevention and Flammability Limits
Drop tower testing demonstrates that material flammability limits (such as Maximum Oxygen Concentration, MOC) differ significantly in low gravity compared to normal 1-g environments [4875013971e3]. The SAFFIRE experiments address this gap by testing samples of identical size to NASA-STD-6001 Test 1 in long-duration microgravity, ensuring proper material selection and flammability mitigation for spacecraft [c50ea962d5ae].

### Operational Hazards and Electrical Safety
A critical pre-test hazard identified is inadvertent igniter activation prior to Cygnus deberthing from the ISS, which would expose the flight crew to toxic combustion gases upon hatch opening [8fb150f1ebba]. To control this hazard, the Saffire flight unit incorporates four latching relays (one on each power feed side and return) controlled and monitored by Cygnus avionics, requiring explicit, multi-step separate ground commands to close each relay [2356a11989f3].

### Detection and Products
Later missions (SAFFIRE-IV, V, and VI) evaluate prototype Orion and ISS combustion product monitors, validate transport and detection models, quantify post-fire gas species decay rates, and test prototype "smoke-eater" hardware to determine atmospheric cleanup rates [fd4e0d8b2745, 76aa9d0acd01, a8ad873033c4, 905e867ca558].

---

## Gravity and Mission Applicability
* **Microgravity and Exploration Environments:** Findings from SAFFIRE-I, II, and III directly apply to microgravity spacecraft environments [0c595c91168d]. SAFFIRE-IV, V, and VI extend these evaluations to exploration atmospheres characterized by elevated oxygen ($O_2$) concentrations and reduced pressures ($P$), as well as complex geometries that replicate realistic spacecraft cabin layouts [9fb95d1874df, eebbafd29382]. Post-fire species decay data and smoke-eater performance metrics directly impact spacecraft recovery and crew safety protocols [a8ad873033c4, 905e867ca558].
* **Terrestrial (Earth) Applications:** The data improves terrestrial compartment fire modeling, large-scale material flammability standards, duct/HVAC monitoring systems, toxic gas risk assessments, and air purification technologies [42164085ccc0, fe68371f782d, 0c595c91168d, 3ea2fcc38c62, a8ad873033c4, 905e867ca558].

---

## Research Gaps and Limitations
* Standard 1-g flammability testing protocols (e.g., NASA-STD-6001 Test 1) are limited because buoyancy suppression in low-g alters material extinction limits [4875013971e3, c50ea962d5ae].
* Prior to the SAFFIRE series, predictive tools lacked large-scale validation data for realistic fires, complex cabin geometries, and exploration atmospheres (elevated $O_2$ and lower pressure) [0c595c91168d, 9fb95d1874df, eebbafd29382].

---

## Key Conclusions
The SAFFIRE program bridges a vital knowledge gap between standard ground-based flammability tests and actual fire behavior in space. By supplying empirical measurements of large-scale flame spread, material thickness effects, multi-material boundary propagation, and post-fire atmospheric recovery, the investigation provides essential validation data for computational fire growth and detection models, ultimately safeguarding crew health and vehicle habitability during deep space exploration [0c595c91168d, eebbafd29382, fd4e0d8b2745, 76aa9d0acd01].