# Non-Imaging Data Acquisition and Instrumentation Summary for the Advanced Combustion Methods Experiment (ACME)

## Executive Summary
This document summarizes non-imaging data file descriptions, sensor configurations, telemetry parameters, and hardware control channels for the Advanced Combustion Methods Experiment (ACME), specifically supporting investigations under ACME-FLAME-DESIGN, ACME-EFIELD, and ACME-BRE. The findings outline the technical specifications for analog input (AIN) and analog output (AO) channels used to monitor combustion diagnostic parameters, chamber pressures, high-voltage electric fields, optical emissions, temperatures, and heat fluxes, as well as critical safety interlocks.

## Research Overview
The ACME project utilizes specialized gaseous combustion hardware in microgravity environments to study fundamental flame behavior, electric field interactions, and burner-stabilized radical extinction. To ensure experimental precision, structural integrity, and personnel/facility safety, various sensors—including pressure transducers, thermocouples, radiometers, heat flux sensors, photomultiplier tubes (PMTs), and ion current sensors—record real-time telemetry. Corresponding analog output channels govern optical gains, diagnostic illumination, and relay-controlled safety interlocks.

## Key Experimental Findings

### Pressure Monitoring and Fluid Delivery
- **Outer Coflow Pressure (PTA1):** Measured via channel AIN-4 using a Measurement Specialties EPRB-2-VR33-10B-/CM1/ATR transducer (0.5 to 4.5 V signal range), converted in flight software to 0 to 145 psia [80a01849cffc].
- **Inner Coflow and Burner Pressure (PTA2):** Measured via channel AIN-5 using the same Measurement Specialties EPRB-2-VR33-10B-/CM1/ATR transducer model (0.5 to 4.5 V), converted to 0 to 145 psia [dd3b99ee8c4f].
- **Chamber Pressure (PTA3):** Measured via channel AIN-6 using the identical Measurement Specialties EPRB-2-VR33-10B-/CM1/ATR transducer (0.5 to 4.5 V), converted to 0 to 145 psia [5cf215c25643].

### Electrical and Ion Diagnostics
- **Ion Current Measurement:** The ion current between the E-Field grid and burner (channel AIN-3) is measured across -1.5 to 1.5 V, corresponding to -25 to 25 µA [4c1cbfa327fa].
- **E-Field High Voltage Supply:** Monitored indirectly via channel AIN-7 (HV_OUT) ranging from -4 to 4 V, mapping to an E-field range of -10000 to +10000 V through an empirical equation [e6ee14c056c7].

### Optical and Radiative Diagnostics
- **Photomultiplier Tube 1 (PMT1):** Channel AIN-8 monitors PMT1 current from 0 to 4 µA using a Hamamatsu H10722-10-MOD2 device observing through a 310 nm bandpass interference filter [ff7521631127].
- **Photomultiplier Tube 2 (PMT2):** Channel AIN-9 measures PMT2 current from 0 to 4 µA using a Hamamatsu H10722-10-MOD2 device configured as broadband with a UV-grade fused silica window and a neutral density coating [aae208b30e02].
- **Radiometer +60:** Utilizes a Dexter Research Center (DRC) XP-0055 thermopile with a 1.25 to 5 V signal range [450f920ebd0b].
- **Photomultiplier Tube 3 (PMT3) Gain Control:** Channel AO-27 manages the gain of a Hamamatsu H10722-10-MOD2 device, providing a gain range of $5 \times 10^3$ to $3.5 \times 10^6$ via a control voltage range of 0.5 to 1.1 V [f158539fdadf].

### Thermal and Heat Flux Sensors
- **BRE Center Thermocouple:** A Type K thermocouple located on the Medtherm sensor (model 8-2.688-10SB-0-0-36-21427KSA) provides a signal range of -6.45 to 55 mV [75606a46f8ca].
- **Rake Thermocouple D:** Operates with a signal range of 0 to 14 mV, corresponding to -200 to 1250 °C [2ba93db94569].
- **Burner Thermocouple:** Type K thermocouple on the burner rated from -200 to 1250 °C, though noted as invalid when the BRE burner configuration is installed [d5fcc9e734bb].
- **BRE Heat Flux Sensor (Center and Offset Channels):** Center and offset heat flux outputs on the Medtherm 8-2.688-10SB-0-0-36-21427KSA sensor operate across 0 to 1.25 V ($1\text{ mV} = 1\text{ Btu/ft}^2$) and are valid exclusively when the BRE burner is installed [9df4459959f1, 99442251c4d9].

### Camera Illumination and Hardware Interlocks
- **Side LED Bank:** Channel AO-28 toggles a bank of 3 white LEDs situated near the analog camera turning mirror (0 V = off, 5 V = on) [61fca95e38dc].
- **End LED Bank:** Channel AO-29 toggles a bank of 3 white LEDs positioned past the end of the analog camera turning mirror (0 V = off, 5 V = on) [54d58da41026].
- **Relay Board Downstream Enable:** Channel AO-30 provides a hardware enable/disable control (0 V = disable, 5 V = signal-dependent state) governing critical safety lines including HV1, HV2, LED1, LED2, TFP_RST, IGN_RST, and IGN_EN [b3d66c522614].

## Fire Safety Analysis
- **Prevention:** Hardware safety interlocks such as the Relay Board Downstream Enable (AO-30) provide direct control to inhibit or enable high-voltage, ignition, and thermal protection signals [b3d66c522614]. Indirect monitoring of high-voltage supplies (AIN-7) prevents electrical breakdown, arcing, and subsequent fire initiation in spacecraft hardware [e6ee14c056c7].
- **Detection:** Monitoring ion currents (AIN-3), chamber/coflow pressures (AIN-4, AIN-5, AIN-6), optical emissions via PMTs (AIN-8, AIN-9), and thermal/radiative loads (BRE center/offset channels, radiometer +60) supplies combustion diagnostics required to track flame front dynamics and stability [4c1cbfa327fa, 80a01849cffc, dd3b99ee8c4f, 5cf215c25643, ff7521631127, aae208b30e02, 450f920ebd0b, 75606a46f8ca, 9df4459959f1, 99442251c4d9].
- **Suppression & Control:** Real-time feedback loops driven by telemetry ensure reactant delivery stability and containment integrity, protecting against abnormal pressure excursions or uncontrolled thermal generation during combustion testing [dd3b99ee8c4f, 5cf215c25643, 75606a46f8ca].

## Gravity and Mission Applicability
- **Partial-G Applicability:** Data acquisition hardware validation and instrumentation reliability directly support microgravity combustion diagnostics tested in spaceflight facilities [9df4459959f1, 99442251c4d9].
- **Earth Applications:** Several sensor calibration methods and telemetry frameworks apply directly to terrestrial systems, including pressure transducer calibrations in laboratory test rigs [80a01849cffc], industrial burner fuel line monitoring [dd3b99ee8c4f], high-pressure process safety vessel monitoring [5cf215c25643], high-voltage electrical safety interlocks [e6ee14c056c7], UV optical fire detection [ff7521631127], radiometry [aae208b30e02], and heat flux sensor standardization [9df4459959f1].

## Research Gaps and Limitations
- Sensor validity is strictly bound to specific hardware configurations; for example, the burner thermocouple (TC_BNR) and BRE heat flux sensor channels are explicitly noted as invalid when alternate or non-BRE burner assemblies are installed [d5fcc9e734bb, 9df4459959f1, 99442251c4d9].

## Key Conclusions
The non-imaging data file descriptions for ACME establish a robust framework for monitoring, controlling, and diagnosing gaseous combustion experiments in space. Through precise analog inputs for pressures, temperatures, radiative heat flux, ion currents, and optical emissions, alongside reliable analog outputs for illumination and safety interlocks, the architecture ensures complete operational visibility and structural containment safety during microgravity combustion research.