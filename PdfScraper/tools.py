import os
import sys
import hashlib
from pathlib import Path
import pymupdf
from pydantic import ValidationError
from dotenv import load_dotenv
from litellm import completion
from assets import *

load_dotenv()

FD = os.path.dirname(os.path.abspath(sys.argv[0]))
active_process = None
Temperature = 0.8
Model_name = os.environ["MODEL_NAME"]
Api_key = os.environ["MODEL_API_KEY"]

def get_pdf_hash(file_path: str | Path) -> str:
    """Computes a stable SHA-256 hash of a PDF file's binary content."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()[:16]  # Truncate to 16 chars for clean IDs

def generate_finding_id(document_name: str, finding_text: str) -> str:
    """Generates a stable, unique hash ID for a finding."""
    raw_str = f"{document_name}:{finding_text}"
    return hashlib.sha256(raw_str.encode("utf-8")).hexdigest()[:12]

def chunk_pdf_to_markdown(pdf_path: str, n_pages=None):
    """
    Opens a PDF and yields markdown content grouped by N pages, 
    preserving page boundaries and tracking metadata.
    """
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    if n_pages is None:
        n_pages = total_pages // 10
        if n_pages == 0:
            n_pages = 1
    
    for start_page in range(0, total_pages, n_pages):
        end_page = min(start_page + n_pages, total_pages)
        
        # PyMuPDF to_markdown accepts a list of 0-based page indices
        page_indices = list(range(start_page, end_page))
        page_numbers = [n+1 for n in page_indices]
        chunk_md = doc.to_markdown(pages=page_indices)
        
        yield page_numbers, chunk_md
        
    doc.close()

def extract_findings_from_chunk(chunk_content: str, document_name: str, document_id: str,
    page_numbers: list[int]):

    raw_json_output = None
    
    user_prompt = EXTRACTOR_USER_PROMPT_TEMPLATE.format(
        document_id=document_id,
        document_name=document_name,
        page_numbers=page_numbers,
        chunk_content=chunk_content
    )

    try:
        response = completion(
            model=Model_name,
            api_key=Api_key,
            messages=[
                {"role": "system", "content": EXTRACTOR_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            response_format=DocumentExtraction,
            temperature=Temperature
        )

        raw_json_output = response.choices[0].message.content
        validated_extraction = DocumentExtraction.model_validate_json(raw_json_output)

        validated_extraction.document_id = document_id
        validated_extraction.document_name = document_name
        validated_extraction.page_numbers = page_numbers
        for finding in validated_extraction.findings:
            finding.id = generate_finding_id(document_name, finding.finding)
        
        return validated_extraction

    except ValidationError as ve:
        print(f"Error extracting findings for {document_name} on pages {page_numbers}: {ve}")
        return (ve, raw_json_output)
    
    except Exception as api_err:
        print(f"API Error for {document_name} on pages {page_numbers}: {api_err}.")
        return None
        

def repair_findings(chunk_content: str, raw_failed_output: str, validation_error: str,
    document_name: str, document_id: str, page_numbers: list[int]):

    user_prompt = REPAIR_USER_PROMPT_TEMPLATE.format(
        document_id=document_id,
        document_name=document_name,
        page_numbers=page_numbers,
        validation_error=validation_error,
        raw_failed_output=raw_failed_output,
        chunk_content=chunk_content
    )

    try:
        response = completion(
            model=Model_name,
            api_key=Api_key,
            messages=[
                {"role": "system", "content": REPAIR_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            response_format=DocumentExtraction,
            temperature=Temperature
        )

        raw_json_output = response.choices[0].message.content
        validated_extraction = DocumentExtraction.model_validate_json(raw_json_output)

        validated_extraction.document_id = document_id
        validated_extraction.document_name = document_name
        validated_extraction.page_numbers = page_numbers

        for finding in validated_extraction.findings:
            finding.id = generate_finding_id(document_name, finding.finding)

        return validated_extraction

    except ValidationError as ve:
        print(f"Repair validation error for {document_name} on pages {page_numbers}: {ve}")
        return (ve, raw_json_output)

    except Exception as api_err:
        print(f"Repair API Error for {document_name} on pages {page_numbers}: {api_err}.")
        return None
    
def generate_summary(document_id: int, document_name: str, page_numbers: list[int],
    extracted_findings: list[dict]):

    user_prompt = SUMMARY_USER_PROMPT_TEMPLATE.format(
        document_id=document_id,
        document_name=document_name,
        page_numbers=page_numbers,
        extracted_findings=extracted_findings
    )

    try:
        response = completion(
            model=Model_name,
            api_key=Api_key,
            messages=[
                {"role": "system", "content": SUMMARY_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=Temperature
        )

        raw_markdown_output = response.choices[0].message.content

        return raw_markdown_output

    except Exception as api_err:
        print(f"API Error generating summary for {document_name} on pages {page_numbers}: {api_err}.")
        return None