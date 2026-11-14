# Advanced Combustion via Microgravity Experiments (ACME) Fire Safety and Combustion Research Summary

## Executive Summary
The Advanced Combustion via Microgravity Experiments (ACME) project, along with precursor investigations like the Structure & Liftoff In Combustion Experiment (SLICE), investigates laminar, gaseous, non-premixed flames in microgravity [89425709f7b0, 7dd47a35d7b5, f0aff49c0151]. The primary objectives are to improve terrestrial combustion efficiency, minimize pollutant emissions, and advance spacecraft fire safety by studying material flammability, soot inception, extinction limits, flame stability, and electric field combustion control [89425709f7b0, a030fe4f42f2, 34a182bbbb48]. Because microgravity eliminates buoyancy-driven flow and flicker, combustion behavior differs fundamentally from normal gravity, yielding unique challenges and requirements for spacecraft hazard prevention, detection, and suppression [48f18420f875, 43e6369efbad].

---

## Research Overview
ACME encompasses six independent gaseous combustion experiments and specialized investigations (such as ACME-BRE, ACME-CLD, ACME-EFIELD, ACME-FLAME-DESIGN, ACME-SFLAME, and CFI-G) conducted inside the Combustion Integration Rack (CIR) [f0aff49c0151, a29a4d081858, c08babc8a3f3, 83a1b1da629f, 58458db5cd98, 82b49398b341, ab366d62a395]. These tests examine gaseous fuels—including methane, ethylene, hydrogen, and gas mixtures simulating paper, plastics, and alcohol—where fuel and oxygen reside on opposite sides of the flame sheet [a29a4d081858, f0aff49c0151, 48f18420f875, 82b49398b341]. Tests are performed as constant volume studies within a ~90-liter chamber free volume, with individual test durations lasting 0.5 to 2 minutes [3aa2dff538cc].

---

## Key Experimental Findings

### Flame Structure, Stability, and Gravity Comparisons
* **Buoyancy Elimination & Quasisteady Flames:** The absence of gravity eliminates buoyancy-driven flicker, producing quasisteady flames with increased spatial length scales that facilitate detailed structural analysis [43e6369efbad, 9b4a8fb9183c].
* **Soot Concentration:** Due to long residence times and the lack of buoyant entrainment, sooty microgravity flames (e.g., pure methane and ethylene coflow diffusion flames) are wider, taller, cooler, and exhibit soot volume fractions five to eight times (and up to a factor of ten) higher than equivalent normal-gravity flames [48f18420f875, 22792a1c378c, e26d854b5468, 4e96d609af55]. However, many microgravity flames remain soot-free [4e96d609af55].
* **Dilution and Extinction Limits:** Highly diluted weak flames (such as fuels heavily diluted with nitrogen) display greater stability in microgravity than in normal gravity, persisting at lower fuel concentrations and enabling lifted flames beyond terrestrial limits [22089645dd90, 89237ceebf25]. Conversely, current predictive modeling capabilities remain significantly lacking for flames at the extremes of fuel dilution, including sooty pure-fuel flames and near-extinction dilute flames [c08babc8a3f3].
* **Momentum-Dominance:** Momentum-dominated flames can be investigated at low velocities in microgravity, simplifying the analysis of forced-flow ventilation effects [7007979ac120].

### Combustion Control via Electric Fields
* **Ion Transport and Ion Winds:** High voltage differentials (up to 10 kV) applied between a burner and a downstream circular mesh generate direct ion transport and induced ion winds that modify flame shapes, alter soot and flammability limits, direct heat transfer, and reduce pollutant emissions [83a1b1da629f, 60c93f4e3396].

### Diagnostics and Instrumentation
* **Imaging Systems:** ACME employs a comprehensive imaging suite comprising five video cameras and two illumination systems, enabling color imaging, CH* chemiluminescence (430-nm bandpass with 450-nm subtraction), OH* ultraviolet chemiluminescence (310-nm bandpass via the LLL-UV package), and soot extinction measurements [5e87e0fabfc3, 0637285d23fc, 825385b54b36, f5bf8ae41a79, 0025b1bce54b].
* **Pyrometry & Radiometry:** Temperature measurements utilize color-ratio pyrometry, High-Bit Depth Multispectral (HiBMs) cameras with Liquid-Crystal Tunable Filters (LCTF), and Thin Filament Pyrometry (TFP) using crew-replaceable silicon carbide or platinum-wired fiber arrays [477476ac94f8, 7fd91ae8a844, c88cbb14975a, 2db1acb20dcc, 63b7a34bf1d3, 9b49eea30766]. Thermal radiation and quenching are monitored using thermopile radiometers (0.2–11 micron spectral range), a wide-view radiometer at 30 degrees, and Photomultiplier Tube (PMT) modules [98dade4d4a8d, baa2c63a00ad, 8962feec0fc7].
* **Thermal and Pressure Sensors:** Burners feature surface thermocouples, internal pressure sensors to monitor outlet differential pressure, and specialized heat flux transducers for Burning Rate Emulator (BRE) tests [80479d105b72, a74374d225de].

---

## Fire Safety Analysis

### Prevention
* **Material Screening and Flammability Limits:** Research on extinction behavior, sustained combustion conditions, and the Burning Rate Emulator (BRE) aids in assessing and refining current flammability test methods for material selection in spacecraft [a29a4d081858, 34a182bbbb48].
* **Hazard Controls:** Restricting reactant bottle volumes to smaller standard sizes (1, 2.25, and 3.8 liters) and constraining burner flows are implemented as critical engineering controls to limit unignited fuel accumulation and chamber over-pressurization [52ef99c0d68b, 3aa2dff538cc].
* **Active Suppression Potential:** Electric field manipulation of ion transport provides a prospective active mechanism to control or suppress combustion in microgravity where buoyancy-driven suppression methods are ineffective [83a1b1da629f].

### Detection
* **Sensor Integration:** Real-time analog downlinks, high-resolution digital cameras, radical emission filters (OH*, CH*), and multi-spectral pyrometry provide robust frameworks for monitoring microgravity ignition, flame progression, and thermal field boundaries [70e0dadffb87, 32639b2657b5, f5bf8ae41a79, 0025b1bce54b, c88cbb14975a].
* **Quenching Detection:** PMT modules and wide-view radiometers enable rapid identification of dim, near-extinction flame quenching events [98dade4d4a8d, 8962feec0fc7].

### Products and Particulates
* **Cabin Contamination Risks:** Microgravity flames produce five to eight times higher soot volume fractions than terrestrial flames, significantly increasing the risk of cabin particulate contamination and optical sensor obstruction [e26d854b5468].

---

## Gravity and Mission Applicability
* **Microgravity Environment:** Findings directly characterize enclosed spacecraft habitats on the International Space Station, where buoyant flows are absent and flammability limits shift [a29a4d081858, 48f18420f875].
* **Partial-Gravity Environments (Moon and Mars):** BRE and flammability investigations specifically assess material extinction behavior and test method relevance for low- and partial-gravity exploration environments [a29a4d081858].
* **Terrestrial Applications:** Results support improvements in terrestrial combustion efficiency, pollutant reduction, industrial burner safety, carbon sequestration, and oxygen-enriched combustion processes [89425709f7b0, a030fe4f42f2, 58458db5cd98, 83a1b1da629f].

---

## Research Gaps and Limitations
* **Predictive Capability Deficits:** Current computer models lack predictive accuracy for extreme fuel dilution, sooty pure-fuel flames, and near-extinction dilute flames [c08babc8a3f3].
* **Sensor and Optical Constraints:** Narrow bandpass filters (such as LCTF and ultraviolet filters) cause optical signal loss, requiring image binning (reducing resolution to 512x512 pixels at 30 fps) [b839ef226f32, de34799740dc]. Upstream thermocouples possess limited utility for non-spherical experiments and are frequently omitted to avoid flow interference or accidental damage [8c0022d69839].

---

## Key Conclusions
ACME and its precursor investigations deliver vital fundamental data regarding gaseous diffusion flames in microgravity. The research demonstrates that microgravity flames are cooler, wider, taller, and substantially sootier, while exhibiting extended dilution and flammability limits compared to terrestrial flames. These insights directly inform spacecraft materials selection, validate flammability test standards for Moon and Mars missions, and advance the design of reliable detection, thermal monitoring, and active fire suppression systems [34a182bbbb48, a29a4d081858, 48f18420f875, 83a1b1da629f, 89237ceebf25].