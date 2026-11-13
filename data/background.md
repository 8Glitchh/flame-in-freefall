# NASA data for Flame in Freefall (pulled 13 Nov 2026)

## What's here (from psi.nasa.gov, search "combustion")
- investigations.csv   : 24 combustion investigations. Objective, approach, hypothesis, impacts, DOI, dates, size
- experimental_tables/ : 22 test-condition tables (one row per test: fuel, O2, pressure, flow, burn time...). ~2,000 test rows
- publications.csv     : papers linked to each investigation (title + DOI)
- file_inventory.csv   : what raw data exists per investigation (videos/images/sensor data, sizes). NOT downloaded: ~13 TB total
- psi_combustion_raw.json : everything above in one file

Raw files: open https://psi.nasa.gov/physci/repo/data/investigations/PSI-<id> -> "Data files and documents"
Cite each investigation by its DOI (PSI rule).

## Other challenge resources
- Fact sheets (PDF): https://www.nasa.gov/wp-content/uploads/2025/07/<name>.pdf
  advanced-combustion-via-microgravity-experiments-acme, burning-and-suppression-of-solids-bass,
  dust-and-aerosol-measurement-feasibility-test-daft, flame-extinguishment-experiment-flex,
  spacecraft-fire-safety-demonstration-saffire, smoke-aerosol-measurement-experiment-same,
  structure-liftoff-in-combustion-experiment-slice, smoke-point-in-co-flow-experiment-spice
- Researcher's Guide (Combustion in Reduced Gravity): https://www.nasa.gov/wp-content/uploads/2016/05/np-2015-10-034-jsc_combustion_in_reduced_gravity-iss-mini-book-011116-508.pdf

## History (for the "why it matters" part)
- Apollo 1 (27 Jan 1967): 100% O2 cabin, wire arc, crew lost to fire/CO. Hatch redesigned to open in ~3 s.
- Apollo 13 (1970): O2 tank 2, heater switches not updated for 65 V, ~1000 F. Third O2 tank added.
- Mir (24 Feb 1997): oxygen-generator canister fire, ~3 ft flame, foam extinguishers, smoke filled station.
- Spinoffs: lighter firefighter air tanks (1976), smoke-vs-dust fire detector (1978), better fire suits / Project FIRES (1982).

## papers/ (downloaded 13 Nov)
- 34 PSI science documents: requirement docs (SRD = what each experiment set out to measure), readmes, test matrices,
  Saffire I/III MergeResult spreadsheets (frame-by-frame results), CFI data summary, BASS fabric flammability paper
- fact_sheets/: 8 NASA fact sheets + Combustion in Reduced Gravity Researcher's Guide
- Missing: "SAFFIRE Objectives, Development and Status" (PSI blocks it from the browser, download it by hand from PSI-98)
