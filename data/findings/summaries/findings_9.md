# Advanced Combustion Methods (ACME) Integrated Science Requirements Definition Review Summary

## Executive Review

This summary synthesizes the experimental requirements, hardware specifications, diagnostic capabilities, and safety protocols established for the Advanced Combustion Methods (ACME) project (including ACME-FLAME-DESIGN, ACME-SFLAME, and ACME-EFIELD investigations). The extracted evidence details the operational sequences, burner hardware designs, electrical safety margins, optical diagnostics, and gas analysis systems configured to study gaseous combustion under microgravity conditions.

---

## Research Overview

The ACME project investigates fundamental gaseous combustion phenomena in microgravity environments aboard spacecraft facilities such as the Combustion Integrated Rack (CIR). The research framework utilizes standardized operational protocols, interchangeable burner geometries, precise reactant delivery systems, and multi-spectral diagnostics to evaluate flame stability, soot formation, electric field effects, and extinction limits.

- **Standardized Operational Sequence:** Testing follows a structured procedure: establishing initial burner flow conditions, igniting the flame, allowing stabilization, adjusting or ramping flows as required, activating electric fields or translating total flux probe (TFP) arrays, and terminating burner flows upon extinction detection or test completion [bd3f03f89101].
- **Test Matrix Flexibility:** Gas delivery and burner systems accommodate multiple gaseous fuels ($H_2$, $CH_4$, $C_2H_6$, $C_3H_8$, $C_2H_4$, $C_3H_6$, and mixtures), inert diluents ($N_2$, $CO_2$, $He$, $Ne$, $Ar$, $Kr$, $Xe$, and mixtures), fuel-inert mixtures, and oxygen-gas mixtures up to 85% $O_2$ [92725dc52e67]. Chamber contents are restricted to a maximum oxygen concentration of 40% [92725dc52e67, bec3b71b6ddb].

---

## Key Experimental Findings

### Burner Configurations and Hardware Specifications
The research utilizes three exchangeable burner classes to examine distinct flame structures and stabilization mechanisms [1ce6e293b79c]:
- **Porous Spherical Burners:** Available in outer diameters (OD) of 6.4 mm, 9.5 mm, and 12.7 mm (toleranced to $\pm 0.1$ mm) with a thermal resistance range of 0 to 450°C [c677958afd34]. Burner temperature measurement ranges span 0–700°C with an accuracy of $\pm 5$°C [e2fe151f9f5b]. Pressure differentials across porous spherical burners require an accuracy of $\pm 2\%$ of reading over a range of 0.1 to approximately $1.5\times$ pressure drop at 5 slpm ($N_2$ basis), with a sampling frequency $\ge 10$ samples/s and response time $\le 0.5$ s [7e942943bc59].
- **Circular Gas-Jet Burners:** Provided in six straight-tube sizes with circular cross-sections, a length $\ge 40$ inner diameters, constructed from stainless steel, and rated for thermal resistance from 0 to 1000°C [5c964a4b8bb7]. 
- **Axisymmetric Coflow Burner:** Includes one size capable of supporting inverse flames [1ce6e293b79c]. Annular coflow must exhibit axisymmetric plug flow for velocities $\le 50$ cm/s with no swirl or turbulence [da4924dec08f]. Two-dimensional (2D) burner temperature ranges span 0–300°C with $\pm 5$°C accuracy [e2fe151f9f5b].

### Electric Field (E-FIELD) Hardware and Diagnostics
Electric field experiments utilize specialized burner and electrode configurations [3327b6052862, 9a199821b0ec]:
- **Burner Grounding and Isolation:** The burner electrode maintains a resistance $< 1\ \Omega$ along and across the burner (equipotential) and is fully insulated from the combustion chamber [3327b6052862].
- **Electrode Mesh:** Constructed as a flat copper circle with 16–22 wires per inch, wire diameters of 0.38–0.64 mm, a 2–3 mm diameter edge ring, and an outer ring diameter $\ge 80$ mm [9a199821b0ec].
- **Voltage and Leakage Control:** Applied voltages range from $-10$ to $+10\text{ kV}$ ($\pm 0.1\%$ set-point accuracy) [ebf8650e1df3]. Current leakage from the burner to $\ge 20\text{ mm}$ downstream of the mesh must remain $< 100\text{ nanoamps}$ at $\pm 10\text{ kV}$ with a 35-mm spacing [ebf8650e1df3].
- **Ion Current and Potential Measurements:** Ion current measurements between the burner and mesh span $0\text{ to }25\ \mu\text{A}$ with an accuracy of the larger of $\pm 5\%$ of reading or $\pm 0.05\ \mu\text{A}$, a frequency $\ge 120$ samples/s, and a response time $\le 1\text{ ms}$ [5a21c066051b]. Electric potential monitoring requires $\pm 1\%$ accuracy, matching range, frequency $\ge 1$ sample/s, and response time $\le 0.5$ s [f6b83e64bd56].

### Chamber Monitoring and Instrumentation
- **Pressure:** Chamber pressure monitoring operates across 0.1–4.0 bar absolute with $\pm 1\%$ reading accuracy, frequency $\ge 1$ sample/s, and response time $\le 0.5$ s [921dd71c5c4a].
- **Gas Flow Rates:** Supply line flow rates require $\pm 5\%$ reading accuracy, frequency $\ge 10$ samples/s, response time $\le 1$ s, and mandatory measurement across all supply lines during testing regardless of active use [df1d13cac87b].
- **Atmospheric Composition:** Initial oxygen concentration and post-test gas composition are quantified via a Gas Chromatograph Instrumentation Package (GCIP) [a17231ab8bc7, dfb588d4cbdc]. Pre-test measurements occur prior to each test after filling, scrubbing, and mixing [a17231ab8bc7]. Post-test measurements occur immediately after extinction and/or mixing, tracking species including $CO$, $CO_2$, $CH_4$, $C_2H_2$, $C_2H_4$, $N_2$, and $O_2$ [dfb588d4cbdc].
- **Acceleration Environment:** Microgravity acceleration jitter is monitored via the Space Acceleration Measurement System (SAMS) with sensors located at or near the CIR [4de1f1154053].

### Optical and Thermal Diagnostics
- **Color Imaging:** Operational color imaging utilizes a spectral range of 0.4–0.7 $\mu\text{m}$, chamber-axis focus, a field of view (FOV) encompassing a $\ge 90\text{ mm}$ circle, uplink control for gain or iris, framing rate $\ge 25\text{ fps}$, near-real-time downlink, and optional uplink illumination [7c715686ce1a]. SFLAME color imaging specifies a bit depth of $3\times 12$ bits ($12\text{ bits each for Red, Green, Blue}$) [bc18683ed2bd].
- **Ultraviolet (UV) Imaging:** Ultraviolet diagnostics target OH* radical emission at a spectral center of 310 nm with a 10 nm FWHM [c4b2d5fd2e72].
- **Soot and Temperature Diagnostics:** Temperature measurements in hot soot-containing regions require a frequency $\ge 0.2$ sample/s and response time $\le 5$ s [d512839ee491]. Field of view (FOV) requirements for soot-free hot regions mandate $\ge 85\text{ mm}$ diameter for spherical flames, and $50\pm 5\text{ mm}$ along the axis ($\ge 20\text{ mm}$ wide) for 2D flames [4bfefa68799b]. Far-field temperature probe measurements require ranges of 700–1700°C for $r \le 40\text{ mm}$ (accuracy $\pm 3$°C) and 0–1250°C for outer positions (accuracy $\pm 1$°C) [da613bf76708].
- **Soot Volume Fraction and Radiative Emission:** Soot volume fraction FOV requires $\ge 45\text{ mm}$ along and wide for 1D flames, and $\ge 25\text{ mm}$ along and wide for 2D flames [77442974ffd3]. Radiant emission sensors require $\pm 10\%$ accuracy, a spectral range of 0.2–11 $\mu\text{m}$, and an irradiance range of $0.0001\text{ to }0.1\text{ W/cm}^2$ [3ecf5e6cfe47].

---

## Fire Safety Analysis

- **Prevention:** Standardized operational sequences, strict burner insulation (< 1 $\Omega$ resistance) [3327b6052862], stringent electrical leakage limits ($< 100\text{ nA}$) [ebf8650e1df3], and the reduction of maximum chamber oxygen concentrations from 50% to 40% directly minimize ignition, arcing, and flammability hazards in closed spacecraft habitats [bec3b71b6ddb].
- **Detection:** Redundant pressure, flow, and GCIP atmospheric sensors [921dd71c5c4a, a17231ab8bc7, df1d13cac87b] ensure immediate identification of off-nominal gas delivery ratios or containment anomalies prior to ignition.
- **Products:** Post-test GCIP analysis quantifies toxic combustion byproducts and asphyxiants ($CO$, $CO_2$, unburned hydrocarbons) to verify atmospheric cleanup and crew safety post-extinction [dfb588d4cbdc].

---

## Gravity and Mission Applicability

- **Microgravity Environment:** All combustion experiments are explicitly designed for microgravity operations ($micro\text{-}g$), where buoyancy-driven convection is eliminated, allowing isolation of diffusion, radiation, and electric field transport mechanisms [bd3f03f89101, 92725dc52e67, da613bf76708]. SAMS integration ensures g-jitter disturbances are tracked relative to flame behavior [4de1f1154053].
- **Partial Gravity Applicability:** No explicit lunar or Martian partial-gravity ($partial\text{-}g$) conditions or findings were reported in the source text.
- **Terrestrial Applications:** Supported earth applications include standardizing combustion research procedures [bd3f03f89101, 4bfefa68799b], defining materials and gas-mixing compatibility guidelines for industrial test rigs [92725dc52e67], informing oxygen control limits in hyperbaric/medical chambers [bec3b71b6ddb], improving industrial burner safety and electric field combustion understanding [5a21c066051b], and advancing radiant heat hazard [3ecf5e6cfe47] and particulate emission diagnostics [77442974ffd3].

---

## Research Gaps and Limitations

- **Field of View and Spatial Resolution Constraints:** Specific spatial boundaries are imposed on optical diagnostics (e.g., FOV size limits for spherical vs. 2D flames and far-field temperature zones), representing bounded operational limits rather than open-ended research gaps [4bfefa68799b, da613bf76708, 77442974ffd3, 3ecf5e6cfe47, 5a21c066051b]. No broader theoretical gaps or unresolved scientific questions were explicitly identified in the source documentation.

---

## Key Conclusions

The ACME project requirements establish a rigorous, highly instrumented framework for conducting gaseous combustion and fire safety research in microgravity. Through precise hardware standardization, multi-spectral optical diagnostics, strict electrical isolation, and comprehensive atmospheric monitoring, the facility ensures safe spacecraft integration while generating empirical data on fundamental flame behavior, electric field modulation, soot formation, and combustion products.