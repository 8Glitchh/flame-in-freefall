# Burning and Suppression of Solids - II (BASS-II) Experiment Summary

## Executive Summary
The Burning and Suppression of Solids - II (BASS-II) investigation evaluates solid fuel ignition, flame spread, extinction limits, and burning behaviors under microgravity conditions. Utilizing the Microgravity Science Glovebox (MSG) aboard spacecraft, the research examines various fuels (including PMMA sheets, rods, and spheres, as well as SIBAL and Nomex fabrics) across multiple oxygen concentrations, ventilation flow velocities, sample thicknesses, and widths. The primary objective is to test hypotheses regarding microgravity material flammability compared to terrestrial upward-burning screening standards, determine whether flames reach finite sizes or grow indefinitely, and establish rigorous safety boundaries for spacecraft materials and atmospheric compositions.

## Research Overview
BASS-II explores fundamental combustion processes in reduced gravity to improve spaceflight safety. 
- **Ignition Hardware & Methods:** Solid fuel ignition is achieved using Kanthal hot wires [f94c09c6fd8b]. The hardware manifest includes 27 custom ignitors across three different design specifications [121069d31829]. In cases of initial non-ignition at low oxygen concentrations, opposed ignition protocols are attempted, followed by ambient air tests [ab9fce9d2db5]. Solid fuel assemblies are installed and removed by crew members via a magnetic interface [920349586132].
- **Atmospheric & Environmental Controls:** Testing is scheduled around planned thruster firings, spacecraft dockings, or undockings, with acceleration environments monitored via nearby Space Acceleration Measurement System (SAMS) units [3a658cb36dea]. Working volume oxygen and carbon dioxide concentrations inside the MSG are verified before and after each burn using Compound Specific Analyzer for Combustion Products (CSA-CP) and Carbon Dioxide Monitor (CDM) sensors [c33c4981ee09].
- **Success Criteria:** Minimal success requires successful testing of 10 samples per Principal Investigator (PI) at desired oxygen and flow conditions with verified ignition and acquired video data [da4d78a86069]. Complete success requires testing all 100 PI samples, acquiring video for all tests, achieving ignition in 90+ tests, observing extinction during flammability limit evaluations, and obtaining still camera data for 90+ tests [cd34736088ad].

## Key Experimental Findings

### Material Manifest and Geometries
The BASS-II test matrix incorporates a wide variety of fuel materials, shapes, and configurations:
- **Fabrics:** 15 SIBAL samples (2 cm wide), 4 SIBAL samples (1 cm wide), and 3 NOMEX samples (2 cm wide) based on previously flown designs [594e5ba78aa7, c50e32e8d45c]. Sheet testing also incorporates SIBAL and Nomex-III fabrics with 1 or 2-sided burns [834d3e526e3a].
- **Flat PMMA Sheets:** 
  - 2 cm wide samples in thicknesses of 0.1 mm, 0.2 mm, 0.3 mm, 0.4 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm, and 5.0 mm [e82dfeda0eb8].
  - 1 cm wide samples in thicknesses of 0.2 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm, and 5.0 mm [e2a6992b418c].
  - One-sided exposed 2 cm samples in thicknesses from 1.0 mm to 5.0 mm [e960a2d5e104].
  - A specialized configuration utilizing a 15 cm width, 2 mm thickness, mica backing, and one-sided burning [e527bb7a2b4e].
- **Cylindrical Rods:** Black and clear PMMA rods in diameters of 0.25 inches (1/4"), 0.375 inches (3/8"), and 0.500 inches (1/2") [c129cf02a4e8, 41d61e005a19].
- **Spherical Geometries:** A 4 cm PMMA sphere sample [dbedb86f4c57] and 4 cm PMMA spherical sections utilized to study forward stagnation region ignition, flame growth, and spread rates [06676d519340, 5776a9954da5].

### Core Hypotheses and Test Matrix Variables
- **Ventilation and Gravity Hypothesis:** BASS-II tests the hypothesis that materials in microgravity, under adequate ventilation, burn as well as or better than identical materials in normal gravity (at matched pressure, oxygen concentration, and temperature) [6cc959cf11a1].
- **Parametric Test Design:** Tests systematically evaluate the influence of ambient oxygen concentration (ranging from low O2 limits up to 50%), forced-flow velocity (ranging from low flows, 10 mm/s, 20 mm/s, 50 mm/s, up to 10 cm/s ramp-downs), sample thickness, sheet width, burn sides (1-sided vs. 2-sided), and material pigmentation (black vs. clear PMMA) [6cc959cf11a1, 06676d519340, 834d3e526e3a, 5c9dc9f82016, 94a8e784e379, abb673bf0952, e527bb7a2b4e].
- **Priority Test Categories:** Specific test protocols target steady opposed- and concurrent-flow spread, solid response times, diameter effects, low-velocity extinction limits, and blowoff limits [5c9dc9f82016, a086d3f30c68, e3d062af7ccd, 3fb5cb7a3cba, 617a3cf2e7b2, 94d66037d5e0, d24983ea772a].

## Fire Safety Analysis

### Prevention
- **Ignition and Material Screening:** Evaluating Kanthal hot wire ignition sources and various polymer thicknesses, widths, and geometries aids in establishing rigorous material selection standards [f94c09c6fd8b, e82dfeda0eb8, e2a6992b418c].
- **High-Oxygen Environments:** Testing at elevated oxygen levels (e.g., 50% $O_2$) defines critical safety margins for systems operating in oxygen-enriched atmospheres [abb673bf0952].
- **Operational Safety:** Ambient gas verification via CSA-CP and CDM sensors, coupled with acceleration tracking via SAMS during thruster or docking activities, prevents unintended atmospheric hazards and experimental corruption [3a658cb36dea, c33c4981ee09].

### Detection and Suppression
- **Fire Growth and Flame Sizing:** Determining whether microgravity flames reach a finite size or continue to grow indefinitely directly impacts spacecraft firefighting strategies and active suppression system deployment [6a2de96f9b53].
- **Extinction Limits:** Identifying low-velocity extinction limits and blowoff thresholds provides clear boundaries on ventilation velocities capable of extinguishing or sustaining unwanted combustion [e3d062af7ccd, 3fb5cb7a3cba].

## Gravity and Mission Applicability
- **Microgravity Relevance:** The data directly characterize spacecraft cabin material flammability under microgravity forced convective flows, accounting for complex geometries like rods, spherical sections, and constrained panels [e82dfeda0eb8, e960a2d5e104, 06676d519340].
- **Lunar and Martian Environments:** Certain findings (such as spherical stagnation-region ignition and forced-flow interactions) apply to reduced-gravity spacecraft and habitat fire safety where convective flows interact with blunt or rounded hardware [06676d519340].
- **Earth Applications:** Findings improve terrestrial compartment fire modeling, forced-flow flammability limit understanding, industrial polymer safety standards, hyperbaric chamber rules, and size-dependent flammability test methods [e82dfeda0eb8, 6cc959cf11a1, e3d062af7ccd, 94a8e784e379].

## Research Gaps and Limitations
- **Screening Validation:** The investigation specifically notes a gap in determining how worst-case microgravity flammability compares directly to standard terrestrial upward-burning screening methods used to qualify spacecraft materials [af6d174525ac].
- **Extinction Thresholds:** Precise low-velocity extinction boundaries require waiting for solid-phase timescales at specific reduced flows to fully resolve inhibition mechanisms [e3d062af7ccd].

## Earth Applications
Results support improved material safety regulations for protective clothing, electrical cabling, narrow polymer components, industrial ventilation ducts, and oxygen-rich medical or industrial facilities [834d3e526e3a, a086d3f30c68, abb673bf0952, 298b5164b9a0].

## Key Conclusions
BASS-II provides essential empirical evidence regarding solid material flammability in space. By systematically evaluating the roles of oxygen concentration, forced-flow velocity, material composition, and geometry, the research ensures that spacecraft material screening protocols, ventilation fire safety boundaries, and crew firefighting strategies are grounded in rigorous microgravity combustion science.