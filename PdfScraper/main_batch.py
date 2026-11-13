from pathlib import Path
import subprocess
import sys

last_index = -1

# Folder containing the PDFs to process
INPUT_FOLDER = Path("")

# Folder where the extracted CSV and Markdown files will be saved
OUTPUT_FOLDER = Path("")

# Create the output folder if it doesn't already exist
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Find PDFs directly inside the input folder (non-recursive)
pdf_files = sorted(INPUT_FOLDER.glob("*.pdf"))

# Report if no PDFs were found
if not pdf_files:
    print(f"No PDF files found in {INPUT_FOLDER}")
    sys.exit(0)

# Display the number of PDFs to process
print(f"Found {len(pdf_files)} PDF files.")

# Process each PDF individually
for index, pdf_path in enumerate(pdf_files, start=1):

    if index < last_index:
        continue

    # Get the PDF filename
    document_name = pdf_path.name

    # Create separate CSV output paths for each PDF
    output_path = OUTPUT_FOLDER / f"findings_{index}.csv"

    print("\n" + "=" * 60)
    print(f"Processing PDF {index}/{len(pdf_files)}")
    print(f"Document: {document_name}")
    print("=" * 60)

    # Run the extraction script with the current PDF and output paths
    # Get the directory containing batch_process.py
    SCRIPT_DIR = Path(__file__).resolve().parent

    # Build the absolute path to main.py
    MAIN_SCRIPT = SCRIPT_DIR / "main.py"

    # Run main.py using its absolute path
    result = subprocess.run(
        [
            sys.executable,
            str(MAIN_SCRIPT),
            str(pdf_path.resolve()),
            document_name,
            str(output_path.resolve()),
        ],
        check=False
    )

    # Report whether processing succeeded
    if result.returncode == 0:
        print(f"Successfully processed: {document_name}")
    else:
        print(f"Failed to process: {document_name}")

# Report completion
print("\n" + "=" * 60)
print("Batch processing complete.")
print(f"Processed {len(pdf_files)} PDFs.")
print(f"Output folder: {OUTPUT_FOLDER}")
print("=" * 60)