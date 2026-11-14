# NASA Spacecraft Fire Safety and Combustion Research Summary

## Executive Summary
Research into combustion and fire behavior in reduced gravity reveals fundamental differences in ignition, flame propagation, extinction, and soot formation compared to normal terrestrial gravity. Gravity-driven buoyancy strongly alters flame structure, dynamics, and flammability limits [962d321a49e8]. Empirical evidence from spaceflight investigations—such as the Burning and Suppression of Solids (BASS), Flame Extinction (FLEX), Smoke Aerosol Measurement Experiment (SAME), and associated drop-tower tests—indicates that standard ground-based screening protocols (e.g., NASA-STD-6001 Test 1) and inert-gas suppressant margins are frequently non-conservative for spacecraft environments [cb9418a6f0f7, f62c0de767d6]. Furthermore, the discovery of persistent, low-temperature cool flames and unexpected upstream flame spreading under slow ventilation flows introduces unique hazards regarding invisible fire sources, unburned fuel vapor clouds, and spontaneous re-ignition [4c6db282715d, c87d5b41d7ef, 032bff7a2553].

---

## Research Overview
The compiled findings synthesize results from multiple microgravity combustion investigations conducted in drop towers, parabolic flights, the Russian Mir space station, and the International Space Station (ISS) Microgravity Science Glovebox (MSG). These investigations span gaseous, liquid droplet, and solid fuel configurations:
* **ACME (Advanced Combustion via Microgravity Experiments):** Encompassing sub-projects like FLAME-DESIGN, BRE, CLD, EFIELD, and SFLAME, investigating gas-jet diffusion flames, porous burner simulations, chemical kinetics, soot formation, and electric field interactions [cfb0af1a96ab, aac12699705d, d8a1252c6cad, 5361c595720c, 992eadbb8d1f].
* **BASS (Burning and Suppression of Solids):** Examining solid fuel flammability, spherical polymer burning, extinction limits, and opposed-flow fabric burning across varying oxygen and ventilation velocities [563ce4a98295, 990bdedc01ba, 57714876031d, 1921b9f732d6].
* **FLEX / FLEX-2 (Flame Extinction):** Studying spherically symmetric droplet combustion (heptane and methanol) to identify radiative and diffusive extinction limits, limiting oxygen indices, and cool-flame phenomena [cb9418a6f0f7, 08a82894a466, 68c007d1faff].
* **Other Investigations:** SOFBALL (spherical premixed flame balls), SAME (smoke aerosol measurement), water mist suppression tests, Super-Critical Water Oxidation (SCWO) studies, and candle/surrogate material flammability tests [8e12fc814aa5, eb0676751601, 9970c7b83ac1, a3801d5e38e9, 21a738fb8dfd].

---

## Key Experimental Findings

### Gaseous Combustion, Soot, and Structure
* **Spherical Diffusion Flames:** Ethylene flowing from a porous sphere into quiescent microgravity air produces spherical flames featuring glowing soot trapped within the blue hydrocarbon flame, accompanied by a bright foreground arc of large soot particles [cfb0af1a96ab]. Drop-tower tests with 100% ethylene issuing at 1.51 mg/s into atmospheric air established baseline soot-inception and spherical diffusion limits [99a2aae51d86].
* **Partially Premixed and Premixed Flames:** SFLAME drop-tower tests utilizing porous burners with gas mixtures of 25% propane, 2% oxygen, 49% argon, and 24% nitrogen provided insights into partial premixing and inert diluent effects [992eadbb8d1f]. The SOFBALL experiment demonstrated that stationary, spherical premixed flame balls ("flame balls") can exist in microgravity, generating the weakest known steady flames (approximately 1 Watt) lasting over 40 minutes [21a738fb8dfd].
* **Smoke-Point and Pollutant Control:** The smoke-point serves as a reliable indicator of a fuel's light-emission and soot-production tendencies under specific fuel chemistry and flow conditions [bc0dfea2bb5c]. Advanced configurations like SLICE investigate lifted flames detaching and stabilizing downstream to improve fuel efficiency and reduce pollutants [b3eeeae09fa4]. ACME-CLD evaluates diluted methane and ethylene coflow flames across varying injection velocities and fuel dilutions [d8a1252c6cad]. Additionally, ACME-EFIELD demonstrated that high-voltage electric fields (up to 10 kV) can actively modify non-premixed flame shape, soot limits, flammability boundaries, and heat transfer [5361c595720c].

### Liquid Droplet Combustion and Cool Flames
* **Extinction Limits and Limiting Oxygen Indices (LOIs):** FLEX and FLEX-2 experiments on spherical heptane and methanol droplet combustion identified radiative and diffusive extinction limits [08a82894a466]. Measured LOIs are significantly lower than normal-gravity values and below previous theoretical predictions [9685606ca18f].
* **Cool Flame Transitions:** Following the radiative extinction of visible hot flames in single alkane droplet tests (e.g., heptane), the droplet continues to vaporize at a constant rate before stopping abruptly at a finite size [c87d5b41d7ef, 68c007d1faff]. This vaporization is sustained by a stable, quasi-steady, lower-temperature cool flame that forms post-extinction, creating hidden fuel vapor clouds [c87d5b41d7ef, 68c007d1faff]. COOL-FLAME-TRANSITIONS research further confirmed that reduced-gravity environments foster persistent, invisible cool flames capable of spontaneous re-ignition long after visible extinction [032bff7a2553].

### Solid Fuel Flammability and Burning Dynamics
* **Candle and Polymer Combustion:** Long-duration Mir space station tests showed that candle flames burn for over 45 minutes to lower ambient oxygen mole fractions than on Earth, disproving the assumption that steady diffusion flames cannot exist without buoyancy [a3801d5e38e9]. BASS experiments burning 2-cm acrylic spheres at 17% oxygen and 10–12 cm/s flow demonstrated that reduced oxygen delays soot formation, keeping flames bluer longer [563ce4a98295, 57714876031d]. However, internal boiling and bubble formation in acrylic spheres can cause explosive bursts of burning vapor, creating intermittent flickering or accelerated burning [563ce4a98295]. BASS evaluated diverse solid geometries including flat samples, PMMA spheres, porous wax slabs, and wax candles down to 17% oxygen using nitrogen dilution [990bdedc01ba].
* **Flow Velocity and Upstream Propagation:** Cotton-fiberglass fabric samples (2-cm wide) tested in opposed flow under stepped velocities (10 cm/s down to < 1 cm/s) exhibited rapid flame responses and dramatic spread rate changes [1921b9f732d6]. Under slow convective flows below buoyancy-induced speeds, solid fuels can preferentially spread upstream into oncoming airflow—behavior opposite to normal gravity [4c6db282715d].
* **Ignition Behavior:** At airflow velocities below natural buoyancy thresholds, ignition times decrease significantly below normal-gravity values because reduced surface heat loss outweighs oxygen transport limitations [7d3c3b680bfe]. Theoretical modeling indicates that the critical heat flux for ignition in microgravity can be as short as half the normal-gravity value [e558ae5a000c].

---

## Fire Safety Analysis

### Prevention and Flammability Limits
* **Non-Conservative Standards:** Evidence from drop-tower and ISS BASS/FLEX investigations indicates that NASA-STD-6001 Test 1 is not conservative [69295e5009e8, f62c0de767d6]. Materials and liquid droplets can ignite and sustain combustion at lower oxygen concentrations and reduced convective flows than predicted by ground tests due to decreased surface heat loss and altered radiative feedback [86d7c38d1216, 7d3c3b680bfe, e558ae5a000c, 08a82894a466, 9685606ca18f].
* **Flame Spread Hazards:** Upstream flame propagation against ventilation flows and rapid flame sensitivity to minor cabin airflow shifts require updated crew response protocols and ventilation interlock strategies [4c6db282715d, 1921b9f732d6].

### Detection and Products
* **Smoke Aerosols and Cool Flames:** SAME aerosol measurements established particle-size distributions for spacecraft materials to guide smoke detector development [eb0676751601]. However, the presence of invisible cool flames and post-extinction vapor clouds represents a critical detection challenge, as standard optical detectors may fail to identify low-temperature, non-luminous combustion [68c007d1faff, 032bff7a2553].
* **Soot Characterization:** Understanding trapped interior soot and particulate generation helps predict toxic combustion products and atmospheric degradation in closed habitats [cfb0af1a96ab, bc0dfea2bb5c].

### Suppression Challenges
* **Inert Suppressant Limitations:** The flammability limit is lower in reduced gravity, meaning terrestrial standards for inert gas suppressants do not provide an equivalent safety margin in spacecraft [cb9418a6f0f7].
* **Air Entrainment Risk:** Localized suppressant application (such as a nitrogen jet) can paradoxically entrain ambient air and strengthen a microgravity flame rather than extinguishing it, even when ambient airflow is ceased [a609dafe51d0, e93df5e55055].
* **Water Mist Extinguishers:** Research into water droplet diameter and concentration dynamics directly supported the design, testing, fabrication, and flight certification of non-toxic water-mist portable fire extinguishers for the ISS, replacing older CO2 units [8e12fc814aa5].

---

## Gravity and Mission Applicability
* **Microgravity (Spacecraft / ISS):** Findings strictly apply to orbital spacecraft where natural buoyancy is absent, altering flame geometry, lowering LOIs, promoting cool-flame persistence, and changing extinction limits [cb9418a6f0f7, 86d7c38d1216, a3801d5e38e9, 08a82894a466].
* **Partial-Gravity (Moon and Mars):** ACME-BRE objectives explicitly assess the relevance of existing flammability test methods for partial-gravity environments [aac12699705d]. Altered convective cooling in lunar or Martian partial gravity creates intermediate flammability behaviors between 1-g and 0-g, directly impacting habitat material selection [86d7c38d1216].

---

## Research Gaps and Limitations
* **Material Screening Gaps:** Current screening protocols (NASA-STD-6001 Test 1) lack adequate conservatism for low-flow, reduced-gravity regimes, risking the selection of flammable engineering materials [69295e5009e8, f62c0de767d6].
* **Thermal Mixing in Life Support:** SCWO microgravity testing revealed severe thermal stratification and a "hot zone" between cooler regions due to the lack of buoyant mixing, exposing limitations in closed-loop waste management reactor designs [9970c7b83ac1].
* **Proposed Test Facilities:** Proposed facilities like the Microgravity Wind Tunnel for the ISS MSG aim to address existing gaps by testing larger solid samples to evaluate fire growth patterns, realistic suppression tactics, and post-fire cleanup [5b87e4bffa70].

---

## Earth Applications
While focused on space safety, the experimental findings and models directly benefit terrestrial applications:
* **Industrial Burners and Engines:** ACME and SPICE findings improve industrial burner designs, soot emission modeling, and droplet combustion understanding for gas turbines and diesel/jet fuel utilization [cfb0af1a96ab, bc0dfea2bb5c, cb9418a6f0f7, 08a82894a466].
* **Polymer and Fabric Fire Safety:** BASS-derived insights enhance fire safety standards for plastics and fabrics in enclosed, variable-flow environments [563ce4a98295, 1921b9f732d6].
* **Advanced Combustion Engines:** Cool-flame and low-temperature combustion findings advance next-generation engine concepts such as Homogeneous Charged Compression Ignition (HCCI) and Reactivity Controlled Compression Ignition (RCCI) [c87d5b41d7ef, 032bff7a2553].
* **Suppression Systems:** Water-mist research contributed to developing terrestrial mist suppression alternatives to banned Halon systems [8e12fc814aa5].

---

## Key Conclusions
1. Spacecraft fire safety cannot rely exclusively on normal-gravity standards because reduced gravity and low-flow environments significantly lower ignition times, reduce limiting oxygen indices, and promote upstream flame spread [cb9418a6f0f7, 86d7c38d1216, 4c6db282715d, e558ae5a000c, 9685606ca18f].
2. Standard local fire suppression methods risk oxygen entrainment and flame invigoration, necessitating specialized suppression strategies such as certified water-mist extinguishers [8e12fc814aa5, a609dafe51d0, e93df5e55055].
3. The existence of persistent, invisible cool flames and spontaneous post-extinction re-ignition introduces hidden toxic and fire hazards that challenge traditional optical detection and extinguishment paradigms [68c007d1faff, 032bff7a2553].