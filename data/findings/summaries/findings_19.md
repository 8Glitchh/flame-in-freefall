# Research Summary: Burning and Suppression of Solids (BASS) and Spacecraft Materials Flammability Investigations

## Executive Summary
This document summarizes findings from the Burning and Suppression of Solids (BASS) and SPICE investigations, extracted from NASA technical documentation (`PSI-26_SRD_BASS.pdf`). The research focuses on evaluating material flammability, flame spread, wake flames, and gaseous fire suppression mechanisms in microgravity environments under forced flow conditions. Key observations indicate that materials in microgravity with adequate ventilation can burn as well as or better than in normal gravity, potentially challenging standard ground test margins (such as NASA-STD-6001 Test #1) [984be84a1180]. The findings also highlight critical operational and design considerations for spacecraft fire detection, containment, gaseous suppression systems, and emergency protocols.

---

## Research Overview
The BASS and SPICE investigations examine solid combustion behavior across diverse fuel types, geometries, and operational configurations in microgravity. 

- **Investigations:** BASS and SPICE [a872b7e0a26d, b9f9ffb8c3e5].
- **Experimental Hardware & Control Variables:** 
  - Airflow speeds in test ducts are adjustable from 5 to 50 cm/s via fans and monitored using anemometers [65acbc5c439a].
  - Gaseous nitrogen for suppression is delivered from pressurized bottles via mass flow controllers at rates ranging from 0 to 500 cc/min [24c5082ff504].
  - Testing is restricted to oxygen concentrations at or above 21% $\text{O}_2$ [5935be002809].
- **Sample Categories and Materials:**
  - Flat sheets, solid spheres, and candles within tubes [a872b7e0a26d].
  - Specific materials include the cotton-fiberglass fabric blend SIBAL (the leading candidate material) [1fbae6157519], PMMA (one-sided flat samples, 1-cm and 2-cm solid spheres, and 2-cm diameter spheres) [8b560013724c, 05bf0728514d, c81ae5bb28a7], wax-saturated fiberglass fabric flat slabs [8b560013724c], wax candles [ff78f6c8ce5f], Nomex III (blend) [8dd62c04c796], and WSTF Nomex Natural (HT90-40) [9c550121e174].
- **Success Criteria:** 
  - Minimal success requires 20 total tests (including 8 flat sample tests across 4 materials and 2 flow speeds, 4 spherical PMMA tests, 4 candle tests, and 4 PMMA wake flame tests with nitrogen extinguishment) [d31158182971].
  - Complete success requires achieving 60 flames as specified in the test matrix [674e21184ed0].

---

## Key Experimental Findings

### Material Flammability and Burning Behavior in Microgravity
- **Comparison to Normal Gravity:** Evidence suggests that materials in microgravity subjected to adequate ventilation can burn as well as or better than the same materials in normal gravity under identical conditions (pressure, oxygen concentration, temperature) [984be84a1180].
- **Specific Test Points and Fuel Consumption:**
  - SIBAL fuel (thin flat, 2-cm width) demonstrated an estimated fuel burned of 216 mg at airflow speeds of 5 cm/s and 10 cm/s [b9f9ffb8c3e5, b39fa5645a47].
  - Nomex III (blend) demonstrated an estimated fuel burned of 132 mg at 50 cm/s flow speed [8dd62c04c796].
  - WSTF Nomex Natural (HT90-40) demonstrated an estimated fuel burned of 252 mg at 50 cm/s flow speed [9c550121e174].
  - PMMA spheres (2-cm diameter) demonstrated an estimated fuel burned of 1,200 mg [c81ae5bb28a7].

### Flame Spread, Geometry, and Wake Flames
- For flat sheet samples (such as SIBAL), concurrent-flow spread rate and limiting flame length are primary combustion properties of interest [4d2566cd376d].
- For solid PMMA spheres (1 and 2-cm width), flame growth rate, flame shape, and luminosity are evaluated [05bf0728514d].
- Solid sphere samples equipped with inert hemispheres prevent flames from spreading into the forward stagnation region, allowing researchers to isolate and study wake flames [b73de5d1ff09].
- Flat slab configurations (wax-saturated fiberglass and one-sided PMMA) study flame extinction under increasing flow levels [8b560013724c].
- Candles within tubes investigate suppression structure effects across varying flow speeds [ff78f6c8ce5f].

---

## Fire Safety Analysis

### Prevention
- **Material Selection Margins:** If standard ground flammability tests underpredict microgravity burning performance, materials selected via NASA-STD-6001 Test #1 may possess inadequate safety margins [984be84a1180].
- **Ventilation and Flow Control:** Regulating airflow speeds between 5 and 50 cm/s helps establish operational velocity limits to prevent unintended fire spread within spacecraft ventilation networks [65acbc5c439a].
- **Hidden Hazards:** Wake flames behind obstacles (evaluated using inert-hemisphere spheres) represent hidden fire risks in tight spacecraft geometries [b73de5d1ff09].

### Suppression
- **Extinguisher Limitations:** Suppressant application techniques that target the base of a flame on Earth can be ineffective or exacerbate microgravity fires due to unwanted oxygen entrainment, depending on flame geometry, extinguisher distance, and dispersion angle [93c159f1da24].
- **Gaseous Suppression Protocols:** Nitrogen injection rates ranging from 0 to 500 cc/min via mass flow controllers [24c5082ff504] or gradual step increments after approximately one minute of burning [8a97cd55034f, a7f70afa69af] provide controlled gaseous extinguishment options inside gloveboxes or test chambers [e9a4934df292].
- **Failsafe Mechanisms:** Complete flow shut-off serves as an essential secondary safety mechanism to starve and extinguish flames when active suppression is required [774b5b11966c, a4c9b4f134b9].

---

## Gravity and Mission Applicability
- **Microgravity Environment:** The experiments are designed specifically for microgravity test operations (such as onboard spacecraft facilities and gloveboxes) where natural convection is absent, requiring forced flow and active gaseous suppression or complete flow shut-off to achieve flame extinction [774b5b11966c, e9a4934df292].
- **Partial-G Applicability:** Specific partial-gravity applicability (Lunar or Martian environments) was not detailed in the extracted findings.

---

## Earth Applications
The findings support terrestrial applications in several enclosed and specialized environments:
- Optimizing fire containment and ventilation safety in confined terrestrial environments like submarines or cleanrooms [65acbc5c439a].
- Designing fixed gaseous fire suppression systems for industrial or aviation use [24c5082ff504].
- Standardizing fabric flammability testing for industrial and consumer textiles using dedicated blends like SIBAL [1fbae6157519].
- Improving fire safety guidelines and wind-assisted flame spread limits for solid combustible materials in confined building spaces, ducts, pipes, and narrow gaps [8b560013724c, ff78f6c8ce5f, b39fa5645a47].
- Assessing protective clothing fabric safety against high-velocity flames or winds, as well as fire suppression designs for spherical or irregularly shaped solid combustibles [8dd62c04c796, 05bf0728514d, 9c550121e174].

---

## Research Gaps and Limitations
- **Testing Constraints:** Testing parameters documented are explicitly restricted to oxygen concentrations at or above 21% $\text{O}_2$ [5935be002809].
- **Ground-to-Space Discrepancies:** Potential underprediction of microgravity flammability by standard ground tests (NASA-STD-6001 Test #1) highlights an ongoing safety and validation gap regarding material flammability margins [984be84a1180].

---

## Key Conclusions
1. Microgravity ventilation can cause certain materials to burn as well as or better than in normal gravity, necessitating careful re-evaluation of material safety margins [984be84a1180].
2. Conventional terrestrial fire suppression tactics that rely on base-application can entrain oxygen and worsen microgravity fires, requiring redesigned suppression delivery methods [93c159f1da24].
3. Rigorous testing matrices encompassing flat sheets, spheres, wake flames, and tubular geometries provide comprehensive performance baselines for spacecraft materials (e.g., SIBAL, Nomex III, PMMA) and gaseous nitrogen suppression thresholds [d31158182971, 674e21184ed0].
4. Complete airflow shut-off and controlled nitrogen injection remain vital operational safeguards for extinguishing microgravity combustion experiments [774b5b11966c, e9a4934df292, a7f70afa69af].