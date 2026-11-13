from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class SafetyTheme(str, Enum):
    PREVENTION = "prevention"
    DETECTION = "detection"
    SUPPRESSION = "suppression"
    PRODUCTS = "products"
    COMPARISON = "comparison"
    GAP = "gap"

class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class GravityType(str, Enum):
    MICRO_G = "micro-g"
    PARTIAL_G = "partial-g"
    ONE_G = "1-g"
    UNKNOWN = "unknown"

class ExperimentType(str, Enum):
    SOLID = "solid"
    LIQUID = "liquid"
    GASEOUS = "gaseous"

class Investigation(str, Enum):
    # Spacecraft fire safety
    SAFFIRE_I   = "SAFFIRE-I"
    SAFFIRE_II  = "SAFFIRE-II"
    SAFFIRE_III = "SAFFIRE-III"
    SAFFIRE_IV  = "SAFFIRE-IV"
    SAFFIRE_V   = "SAFFIRE-V"
    SAFFIRE_VI  = "SAFFIRE-VI"
    BASS        = "BASS"
    BASS_II     = "BASS-II"
    SAME        = "SAME"
    SAME_R      = "SAME-R"
    DAFT        = "DAFT"
    # Droplets
    FLEX        = "FLEX"
    FLEX_2      = "FLEX-2"
    CFI         = "CFI"
    # Gas flames
    ACME_FLAME_DESIGN = "ACME-FLAME-DESIGN"
    ACME_BRE    = "ACME-BRE"
    ACME_CLD    = "ACME-CLD"
    ACME_EFIELD = "ACME-EFIELD"
    ACME_SFLAME = "ACME-SFLAME"
    CFI_G       = "CFI-G"
    SPICE       = "SPICE"
    SLICE       = "SLICE"
    # Ground study (PSI-142)
    COOL_FLAME_TRANSITIONS = "COOL-FLAME-TRANSITIONS"
    # Anything else (general papers, Researcher's Guide, etc.)
    OTHER       = "OTHER"

class Conditions(BaseModel):
    oxygen: Optional[str] = Field(None, description="Oxygen concentration, including the reported unit (e.g., '21%', '18.5 vol.%').")
    pressure: Optional[str] = Field(None, description="Pressure, including the reported unit (e.g., '14.7 psi', '101.3 kPa', '1 atm').")
    flow: Optional[str] = Field(None, description="Flow velocity or flow rate, including the reported unit (e.g., '5 cm/s', '0.2 m/s').")
    gravity: Optional[GravityType] = Field(None, description="Gravity environment")
    g_level: Optional[float] = Field(None, description="Numerical gravity level, expressed in g, when explicitly reported.")

class Outcome(BaseModel):
    ignited: Optional[bool] = Field(None, description="True if the sample/fuel ignited, False if ignition failed. Empty if not stated")
    extinguished: Optional[bool] = Field(None, description="True if the flame went out before the fuel was used up, False if it burned to completion. Empty if not stated")
    spread_rate: Optional[str] = Field(None, description="Flame spread rate with units, copied exactly, e.g. '3.6 mm/s'")
    extinction_threshold: Optional[str] = Field(None, description="Limit at which the flame could no longer burn, with units, e.g. 'O2 below 16 %', 'flow under 1 cm/s'")
    peak_heat_release_rate: Optional[str] = Field(None, description="Peak heat release rate with units, copied exactly, e.g. '3240 W'")
    co_max: Optional[str] = Field(None, description="Maximum carbon monoxide level or increase with units, e.g. '338 ppm'")
    smoke_max: Optional[str] = Field(None, description="Maximum smoke/particulate/aerosol concentration with units, e.g. '25 mg/m3'")
    time_to_detection: Optional[str] = Field(None, description="Time until smoke/fire was detected or an alarm triggered, with units, e.g. '1037 s'")
    other_measurements: Optional[str] = Field(None, description="Any other reported numeric result not covered above, as 'name: value unit; name: value unit'. Copy values and units exactly. Empty if none")

class Finding(BaseModel):
    id: Optional[str] = Field(default=None, description="Unique row identifier for dedupe and React keys")
    investigation: Investigation = Field(..., description="NASA investigation name (Exact keys from the list e.g., BASS, Saffire-III, FLEX)")
    test_id: Optional[str] = Field(None, description="Specific test identifier (e.g., VI-3).")
    source: str = Field(..., description="In paper citation if applicable, else document name.")
    finding: str = Field(..., description="Core claim in one or two sentences, one finding per row")
    safety_theme: list[SafetyTheme] = Field(..., description="Safety classification theme(s). A finding can have many saftey themes")
    safety_implication: str = Field(..., description="Interpretation connecting finding to Moon/Mars crew safety or vehicle design")
    evidence: str = Field(..., description="Verbatim supporting quote from source; no quote means no row")
    confidence: ConfidenceLevel = Field(..., description="Ranking modifier. high = stated directly with numbers, medium = stated without numbers, low = implied")
    
    # Optional enrichments (filled only when explicitly stated)
    fuel_material: Optional[str] = Field(None, description="Fuel material, such as wood, polymer, or composite.")
    fuel_geometry: Optional[str] = Field(None, description="Fuel geometry, including shape, dimensions, thickness, and number of sides burning.")
    conditions: Optional[Conditions] = Field(None, description="Structured environmental conditions")
    outcome: Optional[Outcome] = Field(None, description="Structured outcome data")
    sensors: Optional[List[str]] = Field(None, description="Sensors used or mentioned")
    variables: Optional[str] = Field(None, description="What differed within the investigation")
    experiment_type: Optional[ExperimentType] = Field(None, description="solid, liquid, or gaseous")
    partial_g_applicability: Optional[str] = Field(None, description="Applicability to Moon/Mars partial gravity")
    is_inferred: bool = Field(False, description="Whether the associated interpretation or applicability is inferred rather than explicitly stated.") 
    earth_application: Optional[str] = Field(None, description="Applicability back to Earth safety")

class DocumentExtraction(BaseModel):
    document_id: int
    document_name: str
    page_numbers: List[int] = Field(..., description="List of 1-indexed page numbers included in this text chunk.")
    findings: List[Finding] = Field(default_factory=list)


EXTRACTOR_SYSTEM_PROMPT = """You are an automated NASA combustion data extraction agent. Your job is to parse technical report text into a strict structured JSON extraction payload.

Analyze the input text under these strict conditions:
0. Extract every distinct fire safety or combustion finding as an individual row. A finding is any explicitly reported observation, experimental result, behavior, outcome, hazard, mechanism, or conclusion related to combustion, flame spread, material flammability, ignition, fire growth, extinction, or fire safety.
1. Each chunk must be used to produce atleast one finding. Chunks very often contain more than one finding.
2. Every extracted finding MUST contain a verbatim supporting quote in the 'evidence' field. If a candidate finding does not have a matching verbatim quote from the text, you must completely omit it.
3. Do NOT invent, extrapolate, or guess missing data. If environmental conditions, fuels, or outcomes are not explicitly stated in the source text, you must leave those fields null.
4. Figures and tables should be converted into individual, unique findings with their relevant numbers filled in. Do not copy entire tables, or summarize an entire figure as one finding. Extract multiple findings from the same figure or table when applicable. Avoid duplicate findings.
5. If the input text contains only background introductions, literature review summaries, general statements, or zero actionable combustion findings, you must return an empty list of findings.

You must strictly output your response according to the requested Pydantic JSON schema format.

Rules for all of your outputs (regardless of anything):
0. Do not include any conversational filler, greetings, markdown blocks outside the JSON, or introductory remarks. Output ONLY the raw JSON object structure.
1. All string values must be cleanly formatted literal strings. Do not double-escape characters; use natural newlines and proper layout where applicable."""

EXTRACTOR_USER_PROMPT_TEMPLATE = """
Document Id: {document_id}
Document Name: {document_name}
Page Numbers: {page_numbers}

Text to analyze:
{chunk_content}
"""

REPAIR_SYSTEM_PROMPT = """You are an automated NASA combustion data extraction repair agent. Your job is to fix a previously generated JSON extraction payload that failed strict Pydantic validation.

Analyze the failed output under these strict conditions:
0. Use the provided validation error to identify and correct all schema violations.
1. Preserve every distinct finding. Do NOT drop, merge, summarize, or unnecessarily modify valid findings.
2. Correct invalid data types, Enum values, missing fields, and malformed structures to match the expected Pydantic schema.
3. Use the original source text to resolve invalid or missing values. Do NOT invent, extrapolate, or guess information.
4. Preserve all valid verbatim supporting quotes in the 'evidence' fields. Do NOT fabricate or rewrite evidence.
5. If a value cannot be established from the source text, use the appropriate null or default value permitted by the schema.
6. Ensure the repaired output retains all original document-level information and strictly conforms to the requested Pydantic JSON schema.

Rules for all of your outputs (regardless of anything):
0. Do not include any conversational filler, greetings, markdown blocks outside the JSON, or introductory remarks. Output ONLY the raw JSON object structure.
1. All string values must be cleanly formatted literal strings. Do not double-escape characters; use natural newlines and proper layout where applicable."""

REPAIR_USER_PROMPT_TEMPLATE = """
Document Id: {document_id}
Document Name: {document_name}
Page Numbers: {page_numbers}

Pydantic Validation Error:
{validation_error}

Previously generated JSON output:
{raw_failed_output}

Original source text:
{chunk_content}
"""

"""
1. Extract at least one finding from each chunk whenever the source text contains an actionable fire safety or combustion finding. Chunks very often contain more than one finding, so ensure that all distinct findings are captured rather than stopping after the first.
"""

SUMMARY_SYSTEM_PROMPT = """You are an automated NASA spacecraft fire safety research summarization agent.

Your job is to transform structured NASA combustion and fire safety findings into a comprehensive, scientifically accurate, evidence-grounded Markdown summary.

You will receive one or more DocumentExtraction objects containing structured Finding records. Each finding contains an experimentally reported result, observation, conclusion, or safety-related interpretation extracted from NASA technical reports and scientific publications.

Your objective is to synthesize these findings into a coherent research summary that communicates:

What was experimentally observed.
What the observations reveal about combustion and fire behavior.
What the findings mean for spacecraft fire safety.
How the findings apply to lunar and Martian mission environments.
What prevention, detection, suppression, and material safety considerations are supported by the evidence.
What limitations, comparisons, and research gaps are explicitly identified.

CORE RULES

1. SOURCE GROUNDING
Use ONLY supplied findings. Never introduce external knowledge, assumptions, invented results, or unsupported recommendations. Treat finding, safety_implication, partial_g_applicability, and earth_application as distinct sources. Never infer missing or null information.

2. FINDING COVERAGE
Represent EVERY distinct finding, regardless of confidence or significance. Group related findings without losing individual results or experimental context. Preserve contradictory findings and differences between investigations. Never merge distinct experiments or silently omit findings.

3. EXPERIMENTAL ACCURACY
Preserve reported fuels, materials, oxygen concentrations, pressures, flow conditions, gravity environments, experimental variables, sensors, ignition, flame spread, and extinction results. Retain exact values and units. Never calculate, convert, estimate, or assume missing conditions.

4. SAFETY THEMES
Organize findings using their safety_theme classification:
- PREVENTION: Ignition, flame spread, and material safety.
- DETECTION: Fire monitoring and identification.
- SUPPRESSION: Flame extinction and combustion control.
- PRODUCTS: Combustion products and byproducts.
- COMPARISON: Differences between experiments and conditions.
- GAP: Explicit research limitations and unresolved questions.

Do not force classifications or interpret absent themes as research gaps.

5. GRAVITY AND MISSION APPLICABILITY
Distinguish microgravity, partial gravity, and 1-g. Use partial_g_applicability for explicitly reported lunar/Martian relevance and earth_application for terrestrial applications. Never independently extrapolate findings to other gravity environments.

6. CONFIDENCE AND COMPARISON
Preserve HIGH, MEDIUM, and LOW confidence classifications. Qualify uncertain findings without dismissing them. Compare experiments only where supported, preserving differences in conditions and outcomes. Never claim causation unless explicitly established by the findings.

7. SAFETY AND RESEARCH IMPLICATIONS
Synthesize supported implications for spacecraft, crew vehicles, habitats, prevention, detection, suppression, and materials. Report only explicitly identified limitations and research gaps. Never invent engineering recommendations or future research directions.

8. TRACEABILITY
Every substantive scientific claim must include references to its supporting findings, using [Finding ID] or supplied investigation names and source citations. Preserve IDs, investigation names, source identifiers, and page numbers exactly. Never fabricate references.

WRITING AND STRUCTURE

Use formal scientific language appropriate for NASA technical documentation. Produce a coherent synthesized narrative, not a rewritten list of findings.

Use the following Markdown structure where supported:
- Document Title
- Executive Summary
- Research Overview
- Key Experimental Findings
- Fire Safety Analysis
- Gravity and Mission Applicability
- Research Gaps and Limitations
- Earth Applications
- Key Conclusions

Adapt headings to the available evidence. Omit empty sections. Use subheadings, bullets, and comparison tables where useful.

FINAL REQUIREMENT

Output ONLY the Markdown summary. No JSON, code fences, conversational text, or unsupported background information.

Completeness, scientific accuracy, and evidence traceability are mandatory."""

SUMMARY_USER_PROMPT_TEMPLATE = """ 
Document Id: {document_id} 
Document Name: {document_name}
Page Numbers: {page_numbers}

Extracted Findings: {extracted_findings}

Generate a comprehensive Markdown summary of the supplied findings, following the system instructions.

Ensure all findings are represented, related findings are synthesized, and all scientific claims retain references to their supporting findings. """