# Flammability Aspects of Fabric in Microgravity Combustion Experiments

## Executive Summary
This document summarizes experimental research investigating the flammability, flame spread, and extinction characteristics of thin solid materials—specifically custom cotton-fiberglass composite fabrics (SIBAL) and paper—under microgravity and normal gravity conditions. Conducted using apparatuses such as the SPICE small flow duct (cross-sectional area 76 mm × 76 mm), the research evaluates the influence of forced air flow speeds (ranging from 0 to 44 cm/s) in both concurrent-flow and opposed-flow configurations. Key findings demonstrate that microgravity environments support continuous flame propagation (such as opposed-flow burning) that self-extinguishes in normal gravity due to buoyancy-induced blowoff. Furthermore, the results verify theoretical U-shaped flammability boundaries, identify critical low-velocity quenching extinction thresholds around 1 cm/s, and characterize linear flame spread dependencies on ventilation speeds.

---

## Research Overview
- **Investigational Apparatus:** SPICE apparatus featuring a 76 mm × 76 mm flow duct and a variable-speed fan generating air flow speeds from 0 to 40 cm/s (extended up to 44 cm/s in specific tests) [3a5c1a0dae09].
- **Fuel Materials:** 
  - Custom-made SIBAL fabric composed of a cotton-fiberglass blend (75% cotton, remainder fiberglass by mass; area density of 18.0 mg/cm², simple weave pattern of 60 by 40 threads per inch) [52dcd82c9126]. The inert fiberglass matrix retains structural integrity without curling or cracking after cotton pyrolysis [52dcd82c9126].
  - Thin paper samples (noted to be prone to cracking and unpredictable flame response in earlier microgravity studies) [514ff759684d].
- **Test Configurations:** 
  - **Opposed-Flow:** Air flow opposes flame propagation; samples reach steady state rapidly (within ~5 seconds) [e822cd6f25c4, 171c92d4e76d].
  - **Concurrent-Flow:** Air flow assists flame propagation; requires longer fuel lengths and greater response times (~10 to 20 seconds to reach steady-state conditions) [ffc92a617a15, 6c4493998bec, 79edac3206ce].
- **Diagnostics:** Digital still cameras, video cameras, hot-wire anemometers, and radiometers [b050ab38e0f3].

---

## Key Experimental Findings

### 1. Opposed-Flow Flame Spread and Extinction
- **Spread Rate Behavior:** In opposed flow, the flame quickly achieves steady spread at each flow speed [e085dc25a287], with spread rates reaching a maximum at intermediate flow speeds (around 10 to 15 cm/s) and decreasing at higher speeds [15ed6e413546]. Under a 10 cm/s air flow speed in 0-g, the steady opposed flame spread rate is measured at 1.21 mm/s [db4d90fe40a8].
- **Response Time:** Opposed-flow flames respond rapidly to step-wise changes in air speed because fuel preheating is governed by a small region near the stabilization zone [171c92d4e76d].
- **Extinction and Quenching:** High forced-flow increases up to 44 cm/s do not achieve blowoff extinction in opposed-flow configurations [bac0863ed2d4]. Conversely, reducing opposed flow down to 1 cm/s does not inherently cause quenching extinction [2fbffa88539f], though extrapolations suggest an opposed-flow quenching limit exists below 1 cm/s [0c7508aaaf14]. At near-zero flow speeds (< 1 cm/s), opposed flames assume a nearly circular shape due to multi-directional oxygen diffusion [345d6975596b].

### 2. Concurrent-Flow Flame Spread and Extinction
- **Flame Growth and Steady State:** Flame size grows with time during concurrent-flow tests [0f8a34fa0998]. Limiting lengths and steady spread rates are achieved only at low flow speeds ($\le 10$ cm/s) for short-length samples [0f8a34fa0998, 352da2339307]. For a 1-cm wide sample in 11 cm/s airflow, steady state is reached after approximately 10 to 20 seconds [6c4493998bec, 79edac3206ce].
- **Spread Rates:** Concurrent-flow flame spread rates increase linearly with increasing flow speed [c5f63b9cbe18, 0931ae733666]. For 2-cm wide samples at 10 cm/s, the steady flame base spread rate is 2.55 mm/s [b89b4e4f5c9c]. At ~10 cm/s, concurrent-flow flames are longer and spread twice as fast as opposed-flow flames [db962709007c].
- **Extinction Limits:** Decreasing concurrent-flow speed to very low values (less than 1 cm/s) results in quenching extinction [1902a5abd4a6, ccf11cb32c89, 4986907d9c1c], verifying theoretically predicted U-shaped flammability boundaries for thin fuels [7607f32dd8f4]. High flow increases up to 44 cm/s do not attain blowoff extinction [f586aa082fce].

### 3. Gravity Comparisons and Material Behavior
- **Microgravity vs. Normal Gravity:** Materials in microgravity with adequate ventilation burn more readily than in normal gravity under identical conditions [c08842a25dcd]. Specifically, normal-gravity downward (opposed-flow) burning self-extinguishes due to high buoyancy-induced buoyant flows (minimum buoyant speed ~20 cm/s) [ffdcdb1d1997, 19eb3762bbbd], whereas microgravity successfully supports steady opposed-flow burning [19eb3762bbbd, bdd8eb6b9586].
- **Thermal and Structural Response:** Paper fuel samples tended to crack during microgravity combustion, causing unpredictable flame behavior [514ff759684d]. In contrast, the SIBAL cotton-fiberglass composite maintained symmetric flame halves [ffb4f761469c] and structural integrity without curling or cracking [52dcd82c9126].
- **Combustion Byproducts and Visuals:** Concurrent-flow leading edges exhibit blue regions accompanied by significant yellow soot emission, dark charring, and subsequent bright orange smoldering of cotton remnants [792c37a71bd9, 5514a38173d3]. Conversely, opposed-flow flames exhibit no visible smoldering, indicating more complete fuel pyrolysis [0c53225adcd1].

---

## Fire Safety Analysis
- **Prevention & Ventilation Management:** Spacecraft ventilation velocity must be carefully managed. While low-speed ventilation (< 1 cm/s) can induce quenching extinction [1902a5abd4a6, ccf11cb32c89], intermediate-to-high forced flows accelerate concurrent flame spread linearly [c5f63b9cbe18, 0931ae733666] and maximize opposed-flow spread rates at 10 to 15 cm/s [15ed6e413546]. Emergency ventilation shutdown protocols must account for the fact that high-speed airflow (up to 44 cm/s) does not cause blowoff extinction [f586aa082fce, bac0863ed2d4].
- **Detection & Monitoring:** Post-flame smoldering, observed as bright orange glows beneath the flame matrix in concurrent flows, presents a hidden reignition hazard and produces lingering combustion byproducts that complicate early detection and atmospheric monitoring [792c37a71bd9, 5514a38173d3].
- **Suppression:** Standard 1-g flammability screening is insufficient because buoyant blowoff prevents downward spread testing on materials that remain hazardous in microgravity [19eb3762bbbd]. Fire safety margins must rely on low-velocity extinction boundaries rather than high-speed blowoff limits.

---

## Gravity and Mission Applicability
- **Microgravity (0-g):** Findings directly apply to spacecraft cabin environments, Logistics Carriers, and European Modular Science Lab (MSG) facilities, where forced ventilation and microgravity alter flame geometry (convex bases) and propagation limits [3a5c1a0dae09, bdd8eb6b9586].
- **Partial Gravity (Lunar / Martian):** The provided findings do not explicitly evaluate intermediate partial-g levels (e.g., 0.38-g or 0.16-g) and focus strictly on microgravity versus normal gravity comparisons [c08842a25dcd, 19eb3762bbbd].
- **Earth Applications:** Results improve fire safety design in ventilated indoor environments, building codes, tunnel/corridor fires, and textile flammability standards where low-velocity drafts or forced convective flows are present [0931ae733666, f330380921c5].

---

## Research Gaps and Limitations
- **Normal Gravity Limitations:** Ground-based studies are inherently restricted by natural buoyancy to flow speeds exceeding the minimum buoyant speed (20 cm/s), masking critical low-speed microgravity combustion behaviors [ffdcdb1d1997].
- **Sample Scale:** Experiments utilized short-length sample formats housed in a small wind tunnel duct (76 mm × 76 mm), limiting observations of long-duration transient growth in concurrent flows [0f8a34fa0998, 3a5c1a0dae09].
- **Material Degradation:** Uncontrolled physical breakdown (such as cracking in thin paper) introduces non-predictable flame responses that require structural composites like SIBAL to isolate fundamental combustion kinetics [514ff759684d, 52dcd82c9126].

---

## Key Conclusions
1. Microgravity eliminates buoyant suppression of opposed-flow fires, allowing materials to burn more readily and steadily than in 1-g downward configurations [c08842a25dcd, 19eb3762bbbd, bdd8eb6b9586].
2. Flammability in thin solid fuels follows U-shaped velocity boundaries, with quenching extinction occurring at very low air speeds (< 1 cm/s) in both concurrent and opposed configurations [1902a5abd4a6, ccf11cb32c89, 7607f32dd8f4].
3. Concurrent-flow spread rates increase linearly with forced ventilation speed [c5f63b9cbe18, 0931ae733666], whereas opposed-flow rates peak at intermediate velocities (10–15 cm/s) [15ed6e413546], dictating precise ventilation safety limits for crewed spacecraft habitats.