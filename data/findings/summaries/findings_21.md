# Combustion and Fire Safety Research Summary: Flame Extinguishment Experiment (FLEX) and- Droplet Combustion Investigation (CFI)

## Executive Summary
This document synthesizes combustion and fire safety research findings derived from the International Space Station (ISS) Flame Extinguishment Experiment (FLEX), FLEX-2, the FLEX-Italian Combustion Experiment for Green Air (FLEX-ICE-GA), and the Droplet Combustion Investigation (CFI). Conducted within the Combustion Integrated Rack (CIR) located in the Destiny module, these investigations explore the fundamental burning, radiative extinction, and low-temperature chemistry of isolated liquid fuel droplets under microgravity conditions. A central discovery of these investigations is the persistence of quasi-steady cool flames governed by negative temperature coefficient (NTC) chemistry following hot-flame extinction. These findings fundamentally alter spacecraft fire safety paradigms, demonstrating that traditional hot-flame sensing and hazard analyses are insufficient for assuring complete post-extinction safety.

---

## Research Overview
The experimental campaigns evaluated droplet combustion across diverse pure fuels and binary mixtures—including heptane, methanol, octane, decane, propylbenzene, dodecane, ethanol, hexanol, and complex multi-component hydrocarbon blends [17b2f131cff5, 86da389ad750, f1f590f85dfb]. Droplets ranging from 2 mm to 6 mm in diameter were deployed either as free droplets between opposed 250 µm stainless-steel needles or fixed on 80 µm silicon-carbide (SiC) support fibers [5ee439dd6d99, 25ef7e2a6d9a, ce0c5eb863d4]. 

To achieve quiescent microgravity conditions, the CIR was mounted on the Passive Rack Isolation System (PaRIS), which suppressed high-frequency vibrations and g-jitter to levels typically below $10^{-5}\ g_0$ [ffd9d8e411b2], corroborated by Space Acceleration Measurement System (SAMS) monitoring [ffd9d8e411b2]. Environmental parameters were strictly controlled: ambient pressures ranged from sub-atmospheric levels up to 5.0 atm [5e87a8eb5df0, 86462072e9bb], oxygen mole fractions spanned 0.10 to 0.40 [bd5d95238626], chamber relative humidity was maintained below 10% [44a69e87b418], and initial fuel temperatures were regulated between 18 °C and 27 °C [0d6519c95ad8].

---

## Key Experimental Findings

### Droplet Combustion and Burning Behavior
* **Droplet Sizing and Lifetimes:** Droplets deployed for testing measured 2 mm to 6 mm ($\pm 0.25\text{ mm}$), reproducible to within $\pm 10\%$ [c8a2b9fa528c, 466a3be265ec]. Lifetimes ($\tau_l$) for n-heptane and methanol droplets burning in air at 1.0 atm ranged from 18 s to 72 s for initial diameters of 3 mm to 6 mm, assuming an average burning rate constant of $0.5\text{ mm}^2/\text{s}$ [ec18316f60b8].
* **Droplet Size Effects on Flame Appearance:** Smaller droplets (approx. 2 mm) initially exhibited a luminous yellow flame that transitioned quickly to a bright blue flame before decreasing in size until micro-explosion/disruption [d0994d0655be]. Larger droplets (approx. 3 mm) displayed a continuously dimming blue flame with a growing flame zone [d0994d0655be].
* **Diluent Effects:** Increasing helium ambient mole fraction increased the average burning rate constant for both hot and cool flame regimes for n-octane droplets [c4fb4bd1e579]. Xenon dilution enabled cool flame burning at lower ambient oxygen mole fractions and supported longer burning durations compared to nitrogen or helium dilution [7026bb920c40].
* **Fuel Composition and Additives:** Alcohols such as methanol did not exhibit a cool flame burning regime [5493bf9f011a]. The addition of ethanol to heptane (50/50 by weight) inhibited cool flame burning and eliminated linear $d$-squared behavior after visible flame extinction [fa5733e3b64e]. Furthermore, alkane isomeric structure significantly reduced low-temperature and negative-temperature kinetic behavior relative to n-alkanes of equivalent carbon number [bfa9fd47e2a3].

### Cool Flame Persistence and Multi-Stage Combustion
* **Cool Flame Discovery:** FLEX conclusively revealed that large alkane droplets (2–6 mm) undergo lengthy unique burning behavior in the low-temperature regime governed by NTC chemistry following hot-flame radiative extinction [5ee439dd6d99, a9cd7b1275f0]. 
* **Vaporization Dynamics:** Following radiative extinction of the hot flame for large heptane droplets, the vaporization rate (slope of droplet diameter squared versus time) remained constant for an extended duration before abruptly decreasing, which coincided with the appearance of a large vapor cloud observed by color cameras [0c53af6fa517].
* **Numerical Model Discrepancies:** Detailed chemical kinetic models (using the Curran mechanism) over-predicted the second-stage burning rate and under-predicted the droplet extinction diameter by a factor of 3.5 [f9532f7ceaac]. Numerical predictions confirmed that radiative heat loss is responsible for initiating the cool flame following hot-flame extinction [ad3edfa336ae], with peak gas temperatures during the second stage reaching approximately 700 K [ad3edfa336ae].

### Pressure and Environment Effects on Combustion
* **Sub-Atmospheric Conditions:** At sub-atmospheric pressures, identifying cool flames for heptane using standard radiometer packages was extremely difficult due to extremely short or absent linear $d$-squared behavior following hot-flame extinction [5e87a8eb5df0].
* **Hyperbaric Conditions:** Conversely, decane droplets burning at 1.0 atm exhibited higher cool flame burning rates, smaller cool flame extinction diameters, and significantly higher cool flame radiance compared to 0.50 atm tests [fb81a4990042]. At 3.0 atm ambient pressure, heptane hot-flame extinction became indiscernible on wideband radiometers, and cool flames periodically re-ignited into hot flames with radiant intensities that saturated wideband radiometers [3c280250733c]. Similarly, decane/hexanol mixtures exhibited multiple hot-flame reignitions at hyperbaric pressures [3ad7cb0c0235].

---

## Fire Safety Analysis

### Prevention and Material Safety
* **Atmospheric and Pressure Limits:** Operational boundaries established by the test matrices (oxygen mole fractions from 0.10 to 0.40, pressures from 0.5 to 5.0 atm) define safety envelopes for spacecraft cabin atmospheres [38fc51c239fb, bd5d95238626]. Maintaining strict control over initial fuel purity, droplet dimensions, and chamber humidity ($\le 10\%$) is required to ensure predictable flammability limits [0d6519c95ad8, c8a2b9fa528c, 44a69e87b418].
* **Diluent and Additive Strategies:** Control over cool flame extinction diameters and burning limits can be achieved via diluent management (helium, xenon) [44bbefc1512, 7026bb920c40] or fuel blending additives (such as ethanol) to suppress secondary cool-flame risks [fa5733e3b64e].

### Detection Challenges
* **Blind Spots in Standard Detection:** Because cool flames persist quietly after hot-flame extinction without luminous yellow radiation [5ee439dd6d99, fb1107c59e3e], safety monitoring systems relying solely on hot-flame properties or standard broadband sensors will fail to detect ongoing low-temperature combustion [5ee439dd6d99, a9cd7b1275f0].
* **Advanced Diagnostics Requirements:** Robust detection requires specialized instrumentation, including:
  * Intensified UV cameras targeting OH* (310 nm) or CH (430 nm) radical emission for hot flames [f7f5c2025895].
  * Intensified cameras sensitive to formaldehyde ($\text{CH}_2\text{O}$) chemiluminescence between 390 nm and 490 nm for cool flames [9c5e9194384a].
  * Narrowband and wideband radiometers (0.6 µm to 5 µm) sampled at $\ge 20\text{ Hz}$ [219ff342935b].

### Suppression and Containment
* **Facility Containment:** The CIR combustion chamber (90-liter volume) is engineered for operating pressures up to 9 atm, though conservative safety analyses restricted FLEX operations to approximately 3 atm [a47fe4ca880e]. 
* **Unexpected Reignition Hazards:** High-pressure environments (e.g., 3.0 atm) can induce spontaneous transitions from cool flames back to intense hot flames [3c280250733c, 3ad7cb0c0235], presenting severe unpredicted thermal feedback and pressure spike hazards inside closed habitats.

---

## Gravity and Mission Applicability

### Microgravity Environment
* **Buoyancy Suppression:** Microgravity levels below $10^{-5}\ g_0$ (and specifically between $2\times 10^{-6}$ and $2\times 10^{-4}$ on three axes) are necessary to eliminate buoyancy-driven convective flows, ensuring pure diffusive transport that matches theoretical spacecraft fire models [ffd9d8e411b2, fabd777ff40e, da7981d7446b].
* **Spacecraft Applicability:** The discovery of cool flame persistence directly impacts spacecraft fire safety procedures, as undiscovered cool flames can linger on fuel residues or materials, generating unexpected vapor clouds [0c53af6fa517] and posing latent ignition threats [5ee439dd6d99].

### Partial-G and Terrestrial Applications
* **Lunar/Martian Relevance:** Findings regarding droplet combustion under varied oxygen and pressure conditions inform fire safety guidelines for future planetary habitats and spacecraft operating under partial-gravity or variable-pressure regimes [5ee439dd6d99, 6fc6248bd471, f1f590f85dfb].
* **Earth Applications:** The data supports next-generation piston engine technologies, alternative green aviation fuel safety, hyperbaric industrial chamber design, spray combustion safety, and refined chemical kinetic modeling [5ee439dd6d99, 17b2f131cff5, f9532f7ceaac, fb81a4990042].

---

## Research Gaps and Limitations
* **Kinetic Model Inaccuracies:** Detailed chemical kinetic mechanisms (such as the Curran mechanism) fail to accurately capture low-temperature phenomena, under-predicting droplet extinction diameters by a factor of 3.5 [f9532f7ceaac].
* **Support Fiber Artifacts:** While silicon-carbide support fibers successfully fix droplets in space, they induce significant droplet oscillations and disruptions near cool-flame extinction, limiting the accuracy of extinction diameter measurements [ba4b57c5270a]. Non-contact levitation methods (such as acoustic or magnetic levitation) are identified as necessary to eliminate these support artifacts.
* **Low-Pressure Detection Limits:** Cool flames under sub-atmospheric pressures are exceptionally difficult to infer using conventional radiometry, representing an analytical gap in monitoring reduced-pressure compartments [5e87a8eb5df0].

---

## Key Conclusions
1. **Cool Flames are Ubiquitous:** Isolated liquid alkane droplets reliably form persistent, low-temperature cool flames governed by NTC chemistry following radiative hot-flame extinction across a wide range of spaceflight environments [5ee439dd6d99, ec7cd6226318].
2. **Sensor Redundancy is Mandatory:** Spacecraft fire detection systems must incorporate specialized optical (formaldehyde chemiluminescence) and radiometer diagnostics to prevent undetected cool-flame hazards [5ee439dd6d99, 9c5e9194384a, 219ff342935b].
3. **Pressure and Composition Drive Reactivity:** Elevated pressures (up to 3.0 atm) and specific diluent/fuel mixtures can trigger spontaneous hot-flame reignitions from cool flames, necessitating stringent atmospheric control in crewed habitats and high-pressure enclosures [3c280250733c, 3ad7cb0c0235].