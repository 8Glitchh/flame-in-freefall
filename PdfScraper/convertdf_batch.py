from pathlib import Path
import subprocess
import sys

# Set to -1 to process everything.
# Set to a number (e.g. 5) to start from that file index.
last_index = -1

# Folder containing the CSV files to convert
INPUT_FOLDER = Path("")

# Folder where converted CSV files will be saved
OUTPUT_FOLDER = Path("")

# Create output folder if it doesn't exist
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Find CSV files directly inside input folder
csv_files = sorted(INPUT_FOLDER.glob("*.csv"))

# Report if no CSV files were found
if not csv_files:
    print(f"No CSV files found in {INPUT_FOLDER}")
    sys.exit(0)

print(f"Found {len(csv_files)} CSV files.")

# Get directory containing this batch script
SCRIPT_DIR = Path(__file__).resolve().parent

# Path to convertdf.py
CONVERT_SCRIPT = SCRIPT_DIR / "convertdf.py"

# Process each CSV individually
processed = 0
failed = 0

for index, csv_path in enumerate(csv_files, start=1):

    if index < last_index:
        continue

    document_name = csv_path.name

    # Create separate output path for each CSV
    output_path = OUTPUT_FOLDER / document_name

    print("\n" + "=" * 60)
    print(f"Processing CSV {index}/{len(csv_files)}")
    print(f"Document: {document_name}")
    print("=" * 60)

    # Run convertdf.py with input and output paths
    result = subprocess.run(
        [
            sys.executable,
            str(CONVERT_SCRIPT),
            str(csv_path.resolve()),
            str(output_path.resolve()),
        ],
        check=False
    )

    if result.returncode == 0:
        print(f"Successfully converted: {document_name}")
        processed += 1
    else:
        print(f"Failed to convert: {document_name}")
        failed += 1

# Final summary
print("\n" + "=" * 60)
print("Batch conversion complete.")
print(f"Successfully processed: {processed}")
print(f"Failed: {failed}")
print(f"Output folder: {OUTPUT_FOLDER}")
print("=" * 60)