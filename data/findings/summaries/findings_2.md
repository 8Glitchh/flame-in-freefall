# Synthesis of Spacecraft Materials and Combustion Experiment Operations (SAME Investigation)

## Executive Summary
This document provides a comprehensive technical summary of operational procedures, safety boundaries, and hardware constraints for the Spacecraft Autofire Material Evaluation (SAME) investigation (Document ID: `ac00e24b0f9a0388`). The findings encompass autonomous thermal control protocols, chamber pressurization and flow dynamics, material-specific setpoint multipliers, sensor memory and diagnostic limitations, and software operational boundaries identified during ground support and microgravity testing.

---

## Research Overview
The SAME investigation examines material flammability, thermal degradation, and gaseous combustion dynamics under controlled experimental configurations. Operations require precise calibration of thermal inputs, automated safety aborts, gas-flow velocities, and diagnostic sensor configurations to maintain experimental validity and hardware safety.

---

## Key Experimental Findings

### Material Thermal Setpoints
Material testing protocols utilize specific resistance setpoint multipliers ($Rt/R_0$) to regulate sample temperatures during heating and flammability assessments:
* **Kapton:** $Rt/R_0$ setpoint multiplier is 1.380 [0fe3d9894f55].
* **Lampwick:** $Rt/R_0$ setpoint multiplier is 1.245 [0ddb44e4d3bd].
* **Silicone:** $Rt/R_0$ setpoint multiplier is 1.327 [995d4c955fef].
* **Teflon:** $Rt/R_0$ setpoint multiplier is 1.440 [5c9974d1a1ff].

### Fluid Flow and Chamber Dynamics
* **Inlet Velocity Calculation:** Actual inlet velocity is a derived function of piston bottom-to-top travel time, chamber volume, and inlet tube diameter rather than a direct measurement [f5de6ad95d3a]. Actual inlet velocity must match the desired inlet velocity within $\pm 0.5\text{ cm/sec}$ [f5de6ad95d3a].
* **Piston Evacuation:** Piston chamber fill movement initiates by evacuating the drive side of the piston at a rate of $3.0\text{ LPM}$ until the drive side pressure reaches $13.2\text{ psia}$ [772e6d647ea3].

---

## Fire Safety Analysis

### Prevention and Thermal Control
* **Heater Offset Correction:** If the automatic heater offset correction yields a value greater than $50\ \mu\text{V}$, the test must be immediately aborted and restarted to prevent uncontrolled heating hazards [8299a00d1e18].
* **Automated Thermal Cutouts:** Software continuously monitors sample resistance against desired setpoints and maximum resistance limits (`MaxRt`), automatically terminating heating if resistance or temperature exceeds safe thresholds to protect against thermal runaway [a54e42838dfe].
* **Diagnostic Duct Overpressure:** Ground support testing revealed that simultaneous operation of the STS detector and both DustTraks results in insufficient fluid flow during chamber exhaust, failing to maintain the required overpressure in the diagnostic duct [16ec8f940940].

### Detection and Monitoring
* **Sensor Memory Limitations:** The P-Trak aerosol and smoke detector memory holds approximately sixty 20-minute tests [94732b81d006]. When capacity is reached, the unit stops responding with serial measurements, indicated by continuous `-999` readings [94732b81d006].

---

## Gravity and Mission Applicability

* **Microgravity Operations (ISS):** Automated heater offset limits, thermal abort logic, and material screening protocols apply directly to microgravity operations aboard the International Space Station [8299a00d1e18, a54e42838dfe, 0fe3d9894f55, 0ddb44e4d3bd, 995d4c955fef, 5c9974d1a1ff].
* **Terrestrial Applications:** Procedures and safety constraints inform laboratory combustion test automation safety shutdowns, automated thermal cutout mechanisms for laboratory furnaces, and standardized material flammability testing [8299a00d1e18, a54e42838dfe, 0fe3d9894f55, 0ddb44e4d3bd, 995d4c955fef, 5c9974d1a1ff].

---

## Research Gaps and Limitations

* **Software Velocity Thresholds:** When using a `FillLeakRateLPM` registry value of $0.30$, the maximum supported inlet velocity is $9.8\text{ cm/sec}$ [d9a786802454]. Exceeding this value causes the software to improperly utilize `FillWait` registry values, mis-timing chamber fill operations and sample heating start times [d9a786802454].
* **High-Velocity Workarounds:** An inlet velocity of $10.0\text{ cm/sec}$ is achievable if `FillLeakRateLPM` is set to $0.25\text{ LPM}$ or lower, but secondary timing side effects require caution, prompting recommendations for ground testing or flight testing without sample heating [9f9bf9a66a55].
* **Low-Velocity Timing Adjustments:** For inlet velocities below $2\text{ cm/sec}$, `FillWait` registry values may become inaccurate [32fc05fd5db1]. Correct heater timing requires adjusting the `BackEndCleanAirOffset` registry value (e.g., set to $170\text{ seconds}$ for a $1\text{ cm/sec}$ flow rate) [32fc05fd5db1].

---

## Earth Applications
The findings from this investigation are directly applicable to terrestrial material flammability testing, thermal degradation control standards, automated laboratory furnace safety cutoffs, and combustion test automation safety shutdowns [8299a00d1e18, a54e42838dfe, 0fe3d9894f55, 0ddb44e4d3bd, 995d4c955fef, 5c9974d1a1ff].

---

## Key Conclusions
1. Strict automated thermal and electrical offset boundaries (e.g., $<50\ \mu\text{V}$ heater offset and real-time resistance monitoring) are necessary to prevent spacecraft thermal hazards [8299a00d1e18, a54e42838dfe].
2. Material-specific resistance multipliers ensure accurate thermal application across varied polymer and textile samples (Kapton, Lampwick, Silicone, Teflon) [0fe3d9894f55, 0ddb44e4d3bd, 995d4c955fef, 5c9974d1a1ff].
3. Fluid flow parameters, piston dynamics, and software registry values (such as `FillLeakRateLPM` and `BackEndCleanAirOffset`) require precise configuration to maintain valid experimental timing and system containment [f5de6ad95d3a, 772e6d647ea3, d9a786802454, 9f9bf9a66a55, 32fc05fd5db1].
4. Diagnostic sensor memory limits and exhaust duct overpressure constraints must be actively monitored to prevent data loss or containment compromise [94732b81d006, 16ec8f940940].