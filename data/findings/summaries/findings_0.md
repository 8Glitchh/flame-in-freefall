# Spacecraft Fire Safety Research Summary: SAFFIRE-IV, V, and VI

## Executive Summary
This report synthesizes results from the SAFFIRE-IV, V, and VI experiments conducted in low-Earth orbit aboard Cygnus spacecraft. The research investigated the fire behavior of solid materials (PMMA, cotton, and cotton/fiberglass blends) under varied atmospheric pressures and oxygen concentrations. Findings indicate that smoke and toxic gas generation represent a more immediate hazard than temperature or pressure increases. While particulate-based smoke detection can provide early warning, the effectiveness of these thresholds varies based on material orientation and environmental conditions, necessitating potential adjustments for future spacecraft safety systems.

## Research Overview
The SAFFIRE series utilized controlled, long-duration microgravity fire tests to evaluate combustion in simulated exploration atmospheres. Experiments involved various fuel geometries, including 1-sided (0.5 cm thick) and 2-sided (1.0 cm thick) PMMA slabs, as well as cotton and cotton/fiberglass blend fabrics [11fe9e8916c4, bcc778309552, e77a714facd0, 2d69da1a9d2a]. The test platform utilized a controlled duct flow, maintained by a fan and rotary anemometer, to ensure consistent environmental boundary conditions [73cca9c514f2]. Diagnostics included the Far Field Diagnostics (FFD) package, featuring CO, CO2, and O2 sensors, an ionization smoke detector, and a TSI DustTrak DRX 8533 aerosol mass sensor [76391b348fab].

## Key Experimental Findings

### Combustion Behavior and Flame Spread
*   **Linear Growth:** Unlike 1-g environments, flat materials in microgravity exhibit linear flame growth without acceleration [12539903deb7].
*   **Geometry Constraints:** 1-sided PMMA samples demonstrated a "limiting size" for flame growth, which provides a predictable bound for fire scenarios [1e53a32367bf]. In one instance, a 1-sided sample failed to ignite due to the excessive burning of a nearby 2-sided sample [c765b1145f9f].
*   **Fabric Flammability:** Thin materials like SIBAL and cotton exhibited rapid flame spread rates (up to 4.05 mm/s for SIBAL) and faster time-to-alarm compared to thick PMMA samples [1dec50f50fdf, 95b9c459c5f7, ab0be9742a4e].

### Combustion Products and Detection
*   **Hazard Priority:** Pressure and temperature rises were found to be minimal during tests, whereas smoke particulate and toxic gas concentrations reached hazardous levels, highlighting the critical need for robust smoke detection and air filtration [96473b56d2c0].
*   **Sensor Response:** Smoke aerosol detection at the FFD tracked flame length with a minor delay, aided by the direct flow path in the Cygnus module, as opposed to the more extensive mixing typically found in ISS geometries [6a08ae53760c].
*   **Safety Thresholds:** For several tests, CO2 and CO concentrations exceeded 1-hour and 24-hour Spacecraft Maximum Allowable Concentrations (SMAC), particularly at higher oxygen concentrations [8de17f1fee07, 6dee7912ca0d].

## Fire Safety Analysis

### Prevention and Suppression
*   **Material Configuration:** Single-sided versus double-sided configurations significantly alter burning behavior and hazard production [bcc778309552]. Back-side heat loss in 1-sided configurations mitigates peak heat release rates (HRR) and delays detection times compared to 2-sided burns [dfc8955c7ef8].
*   **HRR Dynamics:** Peak HRRs reached up to 3376 W (for SIBAL) and 3240 W (for PMMA), demonstrating substantial energy release capable of impacting the cabin environment [f1d0c773c2d3, ab0be9742a4e, 2845a73f903b].

### Detection
*   **Alarm Efficacy:** A particulate threshold of 2 mg/m³ effectively detected fires before hazardous CO levels were reached in some cases [e551f6b455bf]. However, this threshold was insufficient in all configurations, as seen in SAFFIRE-VI PMMA tests where toxic gas levels exceeded safety limits before the alarm [af85928494b8].

## Gravity and Mission Applicability
*   **Spacecraft Habitability:** The volumetric calculation method, using CO2 release and pressure tracking, is essential for determining gas dispersion in closed-loop Environmental Control and Life Support Systems (ECLSS) [88f43e4dea0d].
*   **Exploration Environments:** These findings are critical for designing fire safety protocols for lunar and Martian habitats, where atmospheric composition and pressure variations may differ from current Earth-orbiting standards [11fe9e8916c4].

## Research Gaps and Limitations
*   **Detection Thresholds:** The SAFFIRE-VI results indicate that the current 2 mg/m³ smoke alarm threshold may not be sufficiently sensitive for all potential fuel orientations, suggesting a need for lower thresholds or additional, redundant detection strategies [af85928494b8].
*   **System Differences:** The observed delay in smoke detection is specific to the direct flow geometry of the test vehicle and may not represent the more complex, mixed-flow environments of larger habitats like the ISS [6a08ae53760c].

## Earth Applications
*   **Indoor Air Quality:** The findings confirm that in enclosed spaces, toxic gas and smoke toxicity are often more critical than thermal effects, informing early fire detection system design [96473b56d2c0, 76391b348fab].
*   **Engineering Standards:** The data supports standardized flammability testing for polymer materials and provides benchmarks for wind tunnel/HVAC flow control systems [73cca9c514f2, 2d69da1a9d2a].

## Key Conclusions
The SAFFIRE program has successfully quantified the combustion risks of various solid materials in microgravity. While flame growth is linear and predictable for flat materials, the production of toxic byproducts remains a primary threat to crew safety. Future fire safety designs must account for the specific configuration of materials and the limitations of current particulate-based detection thresholds, especially as missions transition to exploration environments with varying atmospheric compositions.