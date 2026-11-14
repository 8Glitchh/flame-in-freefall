# NASA Spacecraft Fire Safety Research Summary: ACME Combustion Experiments

## Executive Summary
This document synthesizes findings from the Advanced Combustion via Microgravity Experiments (ACME) project, encompassing investigations such as the Coflow Laminar Diffusion Flame (CLD), Flame Design, s-Flame, and Electric Field (E-FIELD) experiments [2c3e1c97205f, d0e7f3cdb41b, fe16bc8fbe7b, 1aa66254e949]. Conducted in microgravity facilities such as the Combustion Integrated Rack (CIR), these experiments evaluate gas-fueled laminar diffusion flames, spherical microgravity flames, soot inception, radiative and convective extinction limits, and active combustion control using high-voltage electric fields [2c3e1c97205f, d0e7f3cdb41b, fe16bc8fbe7b, 1aa66254e949]. The research provides foundational data to refine predictive chemical kinetic models, optimize spacecraft fire detection and suppression systems, and establish rigorous operational parameters for combustion safety in spaceflight and terrestrial environments [2c3e1c97205f, d0e7f3cdb41b].

## Research Overview
The ACME research program examines gaseous combustion dynamics under well-controlled microgravity conditions. The principal investigations include:
*   **ACME-CLD:** Investigates coflow laminar diffusion flames using gaseous fuels (such as methane and ethylene) to extend predictable flame condition ranges and verify chemical kinetic and soot formation submodels [2c3e1c97205f, e943bfe6662b].
*   **ACME-FLAME-DESIGN:** Examines soot inception and extinction limits of spherical microgravity flames using ethylene or methane across various fuel-oxygen concentrations [d0e7f3cdb41b].
*   **ACME-SFLAME:** Utilizes spherical porous burners with hydrogen, methane, or ethylene to identify radiative and convective extinction limits at high and low system Damköhler numbers [fe16bc8fbe7b].
*   **ACME-EFIELD:** Studies the application of high-voltage electric fields (up to 10 kV) between burners and meshes to actively modify flame shape, direct heat transfer, alter soot and flammability limits, and reduce pollutants [1aa66254e949, c7e228c343e7].

## Key Experimental Findings

### Combustion Dynamics, Soot, and Extinction Limits
*   **CLD Extinction and Flow Limits:** Coflow laminar diffusion flame extinction tests start at uplinked ignition conditions (e.g., 40% $\text{CH}_4$ or 20% $\text{C}_2\text{H}_4$ flames) and proceed until extinction is detected by a photomultiplier tube (PMT) or when a coflow velocity of 50 cm/s is reached [e943bfe6662b, 92d822803d9e].
*   **Spherical Flame Preparation and Stabilization:** In Flame Design spherical flame tests, chamber contents require a 5-minute hold time to achieve quiescent, isothermal, and well-mixed initial conditions [3b4c03c3d2b3]. Spherical diffusion flames in s-Flame tests are maintained for 25 seconds or until extinction occurs [dfd9e85feb0e].
*   **Radiative and Kinetic Extinction Protocols:** Radiative extinction is confirmed in Flame Design by reducing the flow rate by an estimated 50% for 5 seconds following initial extinction detection [a587e752d3f2]. Kinetic extinction is evaluated by linearly decreasing fluent flow rate to zero over a 20-second window after ignition [e906f60b62ad].
*   **E-FIELD Velocity Responses:** During electric field flame testing, coflow velocity is progressively stepped from 1 cm/s to 25 cm/s with data collected over 3-second intervals to observe soot and flame behavior [d40cc80c14e5].

### Active Control via Electric Fields
*   **Voltage Range and Alternation:** The electric field can be activated at specified polarities and voltages ranging from -10 kV to +10 kV with an accuracy of $\pm$0.1% of the set point [c7e228c343e7]. The potential can be reset via step changes without deactivating the field [cc80469bc4e3], and polarity can alternate at frequencies up to 100 Hz [0412954cb803]. The field can also be deactivated safely without parameters [ce54b3887ed8].

### Hardware Operation and Automation
*   **Simultaneous Multi-Function Execution:** ACME hardware is capable of simultaneously carrying out data acquisition, gas flowing, chamber illumination, CIR illumination projection, electric field energization, and flame extinction sensing in a time-constant manner [8496f0362b75].
*   **Flow Control and Valve Management:** Mass flow controllers (MFCs) feature automated zeroing [243e468ab919], steady flow settings (0 to 100% range with $\le$0.1% precision) [3ba3b22b8fc5], step changes [f9986b938b7f], and linear ramping capabilities [f748d01e01ee]. Solenoid valves provide immediate line isolation [43154e57f631], and delivery lines can be vented and purged [9f84726563a9].
*   **Pressure and Chamber Integrity:** The CIR chamber can be vented to specified pressures between 0.01 and 3 bar (with $\le$1% or 0.01 bar uncertainty) [7942fcbb9759], and gas-tight seal verifications are performed after opening the chamber [fc09e2a5e9bd].
*   **Ignition and Diagnostic Positioning:** Igniters operate between 50% and 100% maximum power for specified durations [36d47b4dfc9e]. The Thin Filament Pyrometry (TFP) fiber array translates at speeds up to 100 mm/s ($\pm$0.1 mm/s uncertainty) to operational positions without contacting the burner [e9fb07eacb46].

## Fire Safety Analysis

### Prevention
*   **Baseline Stability:** Enforcing 5-minute chamber stabilization hold times and precise component warm-up durations ensures repeatable, well-characterized initial conditions [2b8dbbbc7892, 3b4c03c3d2b3].
*   **Soot and Electrical Mitigation:** High soot accumulation during electric field tests can cause unacceptable leakage currents; ACME includes capabilities to clean burner tips and measure leakage currents with and without flames present [357083b66878, 0227fe333b89].
*   **Ignition and Flow Safeguards:** Precise control over igniter power, linear flow ramping, and automated valve closure prevents thermal excursions and unstable combustion spikes [36d47b4dfc9e, f748d01e01ee, 43154e57f631].

### Detection
*   **Extinction Sensing:** Flame extinction is detected using non-imaging instruments, including optical sensors, chemiluminescent emission detectors, thermal radiation sensors, or thermopile detectors [7cc8da597453]. 
*   **Test Reconstruction:** Detailed time logs of issued commands distinguish natural flame extinction from commanded flow terminations [56c2cf354f48].

### Suppression and Mitigation
*   **Automated Response:** Upon detecting extinction, ACME can automatically set all gas flows to zero after a specified delay (0.0 to 99.99 s) or adjust flows to designated hold values [97c4c71a3748, 3830bf492f3e].
*   **Emergency Shutdowns:** In the event of flame blowout during voltage sweeps or extinction testing, systems immediately zero voltage, shut off gas flows, and purge lines [9f84726563a9, 89987ae43f3c].

## Gravity and Mission Applicability

### Microgravity Spaceflight Environment
*   **Autonomous Safety Interlocks:** The automated execution of extinction detection, gas shutoffs, pressure venting (0.01 to 3 bar), and seal verifications directly applies to sealed spaceflight facilities (such as the ISS CIR) where human intervention is limited [7942fcbb9759, fc09e2a5e9bd, 8496f0362b75, 7cc8da597453].
*   **Low-Gravity Combustion Physics:** Removing buoyancy-driven convection in microgravity allows the isolation of radiative and kinetic extinction mechanisms, yielding fundamental insights into low-stretch flammability limits relevant to spacecraft habitat safety [fe16bc8fbe7b, a587e752d3f2, e906f60b62ad].

### Lunar and Martian Mission Environments
*   The provided evidence does not independently extrapolate findings to partial-gravity (lunar or Martian) environments; findings are explicitly bounded by microgravity (spaceflight) and 1-g contexts [2c3e1c97205f, d0e7f3cdb41b, fe16bc8fbe7b].

## Earth Applications
The experimental techniques and fundamental insights generated by ACME translate directly to terrestrial applications:
*   Optimization of industrial burner designs for higher efficiency and lower pollutant/soot emissions [d0e7f3cdb41b, 1aa66254e949].
*   Enhancement of industrial combustion research test chambers, automated safety interlock systems, and high-voltage electrostatic burner maintenance protocols [8496f0362b75, 56c2cf354f48, 357083b66878].
*   Improved characterization of flammability limits, blow-off detection, and electrical leakage monitoring in high-voltage experimental equipment [92d822803d9e, 0227fe333b89].

## Research Gaps and Limitations
*   The primary goal of the CLD experiment is explicitly noted as extending predictable flame conditions through the development of kinetic and soot submodels, indicating that existing predictive models have boundaries that require further experimental verification [2c3e1c97205f].
*   The findings highlight the necessity of active management for operational anomalies such as soot-induced electrical leakage currents during high-voltage electric field experiments [357083b66878, 0227fe333b89].

## Key Conclusions
The ACME research program successfully establishes rigorous experimental protocols for investigating gaseous diffusion flames, extinction limits, and electric field combustion control in microgravity. Supported by robust automation, precise flow and pressure controls, and multi-sensor extinction detection, the findings provide vital data for validating chemical kinetic models and ensuring the safety of spacecraft fire detection and suppression systems [2c3e1c97205f, 8496f0362b75, 7cc8da597453].