# Investigation of Cool Flame Phenomena and Droplet Combustion for Spacecraft Fire Safety: A Synthesis of FLEX and CFI Findings

## Executive Summary
Understanding low-temperature combustion behavior, specifically cool-flame burning and extinction following hot-flame extinction in microgravity, is critical for advancing spacecraft fire safety, hazard assessment, and life support system design. Data extracted from the Flame Extinction (FLEX) and Cool Flame Investigation (CFI) programs outline key findings regarding droplet combustion dynamics, fuel mixture variations, environmental pressure and oxygen parameters, and optical diagnostic sensor configurations. These investigations highlight the complex nature of unmonitored secondary combustion and toxic byproduct generation, defining rigorous environmental and technical requirements for future spaceflight experiments.

---

## Research Overview
The experimental studies encompass liquid droplet combustion of normal alkanes, pure fuels, bio-fuel constituents, and surrogate reference mixtures under microgravity conditions [1604274b7d24, 397077733521, 42404d63b5b9]. To achieve the spherical symmetry required for simplifying mathematical models, microgravity environments with gravitational levels below $10^{-4} g_0$ (and specifically $\le 10^{-5} g_0$) are required [a2b840658d72, e460febe7ab6]. Ground-based drop towers are restricted to 5-second test windows [73f68cdbd6da], and parabolic aircraft flights cannot sustain the required low-g thresholds [2b7ce0f6530f], making long-duration spaceflight platforms essential for observing multi-phase phenomena such as cool-flame burning (which lasts between 5 to 60 seconds) [a2b840658d72].

---

## Key Experimental Findings

### Combustion Phenomena and Fuel Characterization
* **Cool Flame Discovery:** Hot flame extinction leads to a low-temperature cool-flame burning state in microgravity, observed during heptane droplet combustion (initial diameter $D_0 = 3.610\text{ mm}$, ambient pressure $767.836\text{ mmHg}$, $0.210$ oxygen mole fraction) [c2e7d43f14d0, cca6305f17fa]. Reported droplet parameters include average burning rates ($k_{\text{avg}} = 0.485\text{ mm}^2/\text{sec}$; $k_{\text{avg, cool}} = 0.366\text{ mm}^2/\text{sec}$) and extinction diameters ($D_{\text{ext}} = 2.838\text{ mm}$; $D_{\text{ext, cool}} = 1.146\text{ mm}$) [c2e7d43f14d0, cca6305f17fa].
* **Normal Alkane and Surrogate Studies:** Normal dodecane is utilized as a model normal alkane fuel for studying ignition, hot-flame burning/extinction, and cool-flame burning/extinction [42404d63b5b9]. Low-temperature burning characteristics are evaluated for pure fuels, bio-fuel constituents, and surrogate mixtures—including 2,6,10-trimethyldodecane (farnesane), n-dodecane mixtures, n-dodecane/iso-octane/n-propyl benzene/1,3,5-trimethyl benzene mixtures, and n-heptane/2,2,4-trimethylpentane mixtures—to establish relationships with octane and cetane behavior [397077733521, 5a2fd0f696f4].
* **Additive and Chemical Pathway Disruption:** Ground-based experiments explore alkane low-temperature chemistry by mixing additives into the fuel to disrupt low-temperature chemical pathways [65eaefa66836].

### Environmental and Operational Parameters
* **Pressure Range:** Ambient pressure strongly influences cool-flame burning and extinction under both hypo- and hyper-baric conditions, with operational requirements spanning $0.5$ to $3.0\text{ atm}$ (and up to $5.0\text{ atm}$ desired based on hardware limits) [76355dcacc10].
* **Oxygen Concentration:** Ambient oxygen mole fractions span $0.10$ to $0.40$ [67e9b8aaf67a]. While FLEX examined flammability limits by testing gradually decreasing oxygen ambients, CFI targets fewer oxygen ambients with a higher density of tests within each ambient [0833864d610d].
* **Diluent Gases:** Nitrogen serves as the primary diluent, while helium and xenon strongly influence cool-flame burning and extinction behaviors by modifying thermal and mass diffusion [3967e514e0ee].
* **Ambient Restrictions:** Ambient humidity must remain below $10\%$ to prevent moisture interference with ignition limits [e460febe7ab6].

### Hardware and Optical Diagnostics
* **Support Fiber Optimization:** In FLEX-064 experiments, support fiber diameter was reduced from $80\ \mu\text{m}$ to $40\ \mu\text{m}$ because the larger $80\ \mu\text{m}$ fiber introduced thermal and physical disturbances near cool-flame extinction [248563b3f25d].
* **Field of View and Droplet Drift:** To accommodate greater free deployment droplet drift and increase experiment success rates, the imaging field of view (FOV) is increased from $30\text{ mm}$ (FLEX, requiring drift $<1\text{ mm/sec}$) to $50\text{ mm}$ and subsequently $80\text{ mm}$ in CFI [ccbeb1dcae48, 5b541946f9c2, c81c81e32d6e].
* **Chemiluminescence Imaging:** 
  * $\text{OH}^*$ chemiluminescence at $310\text{ nm}$ is extremely dim, requiring $2 \times 2$ pixel binning which sacrifices spatial resolution [54f3437872f1].
  * $\text{CH}$ chemiluminescence at $430\text{ nm}$ offers improved contrast and reduced noise, potentially eliminating binning at the expense of higher data storage and downlink demands [158dd38b86eb].
  * Hot-flame imaging requires $\text{OH}^*$ or $\text{CH}$ chemiluminescence capability, $100\ \mu\text{m}$ spatial resolution, $30\text{ fps}$ frame rate, and adjustable gain [36117a1ac2b7]. Simultaneous hot-flame and cool-flame chemiluminescence with current camera configurations is unlikely [02fa29a5035b]. Cool flames are expected to be roughly half the size of hot flames [673226c72ff2] and very dim [daca347e5596].
* **Radiometric Measurements:** Original FLEX radiometers suffered from low sensitivity and poor signal-to-noise ratios for detecting dim or hot flames [310b24bd3c62]. Upgraded FLEX systems implemented a broadband sensor ($0.6$ to $10.0\ \mu\text{m}$) for hot flames and a narrowband sensor ($5.0$ to $6.5\ \mu\text{m}$, $\text{H}_2\text{O}$) sensitive to cool flames [376690de6fcd]. CFI requires matching wavelength bands with auto-gain capabilities covering a flame radiance range of $0.1$ to $100\text{ W}$ [652777cc0d0f].
* **Pyrometry and Hardware Modifications:** The initial HiBMS-2/Liquid Crystal Tunable Filter (LCTF) configuration for SiC fiber two-color pyrometry was hindered by slow LCTF cycling times and low detector quantum efficiency multiplied by LCTF transmission [ec2f9f962ad2, 8b62b728a3f1]. Modifications require removing the LCTF, substituting a wideband bandpass IR filter, incorporating a calibration insert into the igniter circuit [d24f9c6aba3e], and enabling SiC pyrometry for fiber-supported tests (though not necessarily simultaneously for hot and cool flames) [7c5a895eae02]. The standard FLEX color camera with internal chamber lighting images vapor clouds and hot flames but cannot image cool flames [3094379592eb].

---

## Fire Safety Analysis

### Prevention
* **Ignition and Flammability Limits:** Characterizing low-temperature autoignition, droplet cool-flame dynamics, and pressure/oxygen limits prevents unpredicted combustion and fuel leakage hazards in spacecraft fuel and propulsion systems [42404d63b5b9, 5a2fd0f696f4, 0833864d610d].
* **Chemical Inhibition:** Exploring alkane low-temperature chemistry via fuel additives provides pathways for novel fire suppression and ignition inhibition strategies [65eaefa66836].
* **Artifact Minimization:** Using reduced-diameter support fibers ($40\ \mu\text{m}$) prevents thermal sink interferences that could mask true flammability limits [248563b3f25d].

### Detection
* **Cool Flame Visibility:** Because cool flames are dim [daca347e5596], half the size of hot flames [673226c72ff2], and invisible to standard color cameras and lighting setups [3094379592eb], spacecraft fire detection systems must integrate specialized optical sensors.
* **Sensor Specifications:** Upgraded radiometry (broadband $0.6\text{--}10.0\ \mu\text{m}$ and narrowband $5.0\text{--}6.5\ \mu\text{m}$ $\text{H}_2\text{O}$) with auto-gain across a $0.1\text{--}100\text{ W}$ radiance range are necessary to capture both intense hot flames and dim secondary combustion without sensor saturation or inadequate signal-to-noise ratios [310b24bd3c62, 376690de6fcd, 652777cc0d0f].

### Products and Secondary Combustion
* **Unmonitored Hazards:** Understanding cool-flame pathways is vital for predicting unmonitored secondary combustion and the generation of toxic byproducts during spacecraft cabin fires [c2e7d43f14d0].

---

## Gravity and Mission Applicability
* **Microgravity and Exploration Context:** The findings directly apply to microgravity spacecraft conditions relevant to lunar or Martian transit and long-duration exploration architectures where fuel mixtures and alternative bio-fuels are evaluated [1604274b7d24, 397077733521, 5a2fd0f696f4]. 
* **Strict Environmental Control:** Achieving valid microgravity combustion data requires strict adherence to environmental thresholds ($\le 10^{-5}\text{ g}_0$ gravity and $<10\%$ ambient humidity) [e460febe7ab6].

---

## Research Gaps and Limitations
* **Diagnostic Constraints:** Current camera setups cannot simultaneously perform chemiluminescence imaging of hot and cool flames [02fa29a5035b]. Furthermore, $\text{OH}^*$ imaging requires pixel binning that degrades spatial resolution [54f3437872f1], and LCTF-based pyrometry systems are limited by slow cycling times and insufficient transmission efficiency [ec2f9f962ad2, 8b62b728a3f1].
* **Platform Limitations:** Parabolic flights fail to reach the required $<10^{-4} g_0$ quiet microgravity environment [2b7ce0f6530f], and ground drop towers are restricted to 5-second durations, precluding full observation of extended cool-flame phenomena [73f68cdbd6da].

---

## Earth Applications
The insights gained from these microgravity combustion experiments translate directly to terrestrial applications:
* Improving engine knock prediction and industrial safety regarding low-temperature fuel oxidation [c2e7d43f14d0].
* Enhancing fundamental combustion models and low-temperature chemical kinetics for automotive and aerospace engines [1604274b7d24].
* Assisting in the formulation of cleaner-burning alternative fuels and biofuels with well-characterized autoignition safety profiles [397077733521].
* Guiding fuel additive design for safer fuel transport, handling, and engine knock suppression [65eaefa66836].
* Informing industrial safety standards for hyperbaric chambers, oxygen-enriched environments, and specialized gas-mixing life support systems [76355dcacc10, 67e9b8aaf67a, 3967e514e0ee].
* Advancing high-speed pyrometry, low-light optical sensor sensitivity, and combustion diagnostic hardware design [ec2f9f962ad2, 8b62b728a3f1, d24f9c6aba3e].