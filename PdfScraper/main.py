import sys
from tools import *
import pandas as pd
import time

# Tunable parameter
N = None
api_retries = 4
repair_retries = 2

pdf_path = sys.argv[1] if len(sys.argv) > 1 else ""
document_name = sys.argv[2] if len(sys.argv) > 2 else ""
output_path = sys.argv[3] if len(sys.argv) > 3 else ""

document_id = get_pdf_hash(pdf_path)

# Explicit CSV column definitions
CSV_COLUMNS = [
    # Document metadata
    "document_id",
    "document_name",
    "page_numbers",

    # Finding fields
    "finding_id",
    "investigation",
    "test_id",
    "source",
    "finding",
    "safety_theme",
    "safety_implication",
    "evidence",
    "confidence",
    "is_inferred",

    # Fuel
    "fuel_material",
    "fuel_geometry",

    # Conditions
    "oxygen",
    "pressure",
    "flow",
    "gravity",
    "g_level",

    # Outcome
    "ignited",
    "extinguished",
    "spread_rate",
    "extinction_threshold",
    "peak_heat_release_rate",
    "co_max",
    "smoke_max",
    "time_to_detection",
    "other_measurements",

    # Additional enrichments
    "sensors",
    "variables",
    "experiment_type",
    "partial_g_applicability",
    "earth_application",
]


# Flatten individual finding into a CSV row
def finding_to_row(finding, extraction):

    conditions = finding.conditions
    outcome = finding.outcome

    return {
        # Document metadata
        "document_id": extraction.document_id,
        "document_name": extraction.document_name,
        "page_numbers": ", ".join(map(str, extraction.page_numbers)),

        # Finding fields
        "finding_id": finding.id,
        "investigation": finding.investigation.value,
        "test_id": finding.test_id,
        "source": finding.source,
        "finding": finding.finding,
        "safety_theme": ", ".join(theme.value for theme in finding.safety_theme),
        "safety_implication": finding.safety_implication,
        "evidence": finding.evidence,
        "confidence": finding.confidence.value,
        "is_inferred": finding.is_inferred,

        # Fuel
        "fuel_material": finding.fuel_material,
        "fuel_geometry": finding.fuel_geometry,

        # Conditions
        "oxygen": conditions.oxygen if conditions else None,
        "pressure": conditions.pressure if conditions else None,
        "flow": conditions.flow if conditions else None,
        "gravity": conditions.gravity.value if conditions and conditions.gravity else None,
        "g_level": conditions.g_level if conditions else None,

        # Outcome
        "ignited": outcome.ignited if outcome else None,
        "extinguished": outcome.extinguished if outcome else None,
        "spread_rate": outcome.spread_rate if outcome else None,
        "extinction_threshold": outcome.extinction_threshold if outcome else None,
        "peak_heat_release_rate": outcome.peak_heat_release_rate if outcome else None,
        "co_max": outcome.co_max if outcome else None,
        "smoke_max": outcome.smoke_max if outcome else None,
        "time_to_detection": outcome.time_to_detection if outcome else None,
        "other_measurements": outcome.other_measurements if outcome else None,

        # Additional enrichments
        "sensors": ", ".join(finding.sensors) if finding.sensors else None,
        "variables": finding.variables,
        "experiment_type": finding.experiment_type.value if finding.experiment_type else None,
        "partial_g_applicability": finding.partial_g_applicability,
        "earth_application": finding.earth_application,
    }


# Collect rows
rows = []

for page_numbers, chunk_content in chunk_pdf_to_markdown(pdf_path, N):

    extraction = extract_findings_from_chunk(
        chunk_content=chunk_content,
        document_name=document_name,
        document_id=document_id,
        page_numbers=page_numbers,
    )

    i = 0  # API retries
    j = 0  # Repair retries

    while not isinstance(extraction, DocumentExtraction):

        if extraction is None and i < api_retries:
            sleep_time = 2 ** i
            print(f"Retrying in {sleep_time}s...")
            time.sleep(sleep_time)
            i += 1

            extraction = extract_findings_from_chunk(
                chunk_content=chunk_content,
                document_name=document_name,
                document_id=document_id,
                page_numbers=page_numbers,
            )

        elif isinstance(extraction, tuple) and j < repair_retries:
            ve, raw_json_output = extraction
            extraction = repair_findings(
                chunk_content=chunk_content,
                raw_failed_output=raw_json_output,
                validation_error=str(ve),
                document_name=document_name,
                document_id=document_id,
                page_numbers=page_numbers
            )
            j += 1

        else:
            print("Maximum retries reached. Could not extract findings.")
            break

    # Iterate over individual findings
    for finding in extraction.findings:

        row = finding_to_row(finding, extraction)
        rows.append(row)


# Construct DataFrame with explicitly defined columns
df = pd.DataFrame(rows, columns=CSV_COLUMNS)

#Use CSV to create MD summary
summary_path = output_path.replace(".csv", ".md")
extracted_findings = df.to_dict(orient="records")

all_page_numbers = sorted({
    int(page.strip())
    for pages in df["page_numbers"].dropna()
    for page in str(pages).split(",")
    if page.strip()
})

markdown_summary = generate_summary(
    document_id=document_id,
    document_name=document_name,
    page_numbers=all_page_numbers,
    extracted_findings=extracted_findings
)

i = 0
while markdown_summary is None and i < api_retries:
    sleep_time = 2 ** i
    print(f"Retrying in {sleep_time}s...")
    time.sleep(sleep_time)
    i += 1

    markdown_summary = generate_summary(
        document_id=document_id,
        document_name=document_name,
        page_numbers=all_page_numbers,
        extracted_findings=extracted_findings
    )

if i < api_retries:
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(markdown_summary)
else:
    print("Maximum retries reached. Could not summarize findings.")

print(f"Markdown summary saved to: {summary_path}")

# Export CSV
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Total findings extracted: {len(df)}")
print(f"CSV saved to: {output_path}")

print(df.head())