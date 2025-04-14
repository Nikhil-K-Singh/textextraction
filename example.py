#!/usr/bin/env python3
"""
Example usage of the textextraction package for processing different types of documents.
"""

import os
import logging
from textextraction import ImageText, ScannedPdfText, PdfText

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create output directory
os.makedirs("private", exist_ok=True)

# Initialize the processors with markdown output options
img_processor = ImageText(
    ocr_engine="easyocr",     # Use EasyOCR for better accuracy
    dictionary=True,          # Filter out non-English words
    add_metadata=True         # Add YAML metadata to the markdown
)

scanned_pdf_processor = ScannedPdfText(
    ocr_engine="easyocr",     # Use EasyOCR for better accuracy
    add_page_number=True,     # Add page numbers to the output
    dictionary=True,          # Filter out non-English words
    table_detection=False,     # Disable table detection
    add_metadata=True         # Add YAML metadata to the markdown
)

scanned_pdf_processor_2 = ScannedPdfText(
    ocr_engine="tesseract",  # Use EasyOCR for better accuracy
    add_page_number=True,  # Add page numbers to the output
    dictionary=True,  # Filter out non-English words
    table_detection=False,  # Disable table detection
    add_metadata=True,  # Add YAML metadata to the markdown
)

pdf_processor = PdfText(
    add_page_number=True,     # Add page numbers to the output
    dictionary=True,          # Filter out non-English words
    add_metadata=True,
    table_detection=True,         # Add YAML metadata to the markdown
)

# Process scanned PDF with table detection
print("\nProcessing scanned PDF with table detection...")
extracted_text_scanned = scanned_pdf_processor.process(
    input_path="private/scanned.pdf",           # Path to the scanned PDF file
    output_path="private/scanned_output_easyocr.md"      # Path to the output markdown file
)
print(f"Scanned PDF processed. Extracted {len(extracted_text_scanned.split())} words.")

print("\nProcessing scanned PDF with table detection...")
extracted_text_scanned = scanned_pdf_processor_2.process(
    input_path="private/scanned.pdf",           # Path to the scanned PDF file
    output_path="private/scanned_output_tesseract.md"      # Path to the output markdown file
)
print(f"Scanned PDF processed. Extracted {len(extracted_text_scanned.split())} words.")


# Also process an image and regular PDF for comparison
print("\nProcessing image...")
extracted_text = img_processor.process(
    input_path="private/image.png",              # Path to the image file
    output_path="private/image_output.md"         # Path to the output markdown file
)
print(f"Image processed. Extracted {len(extracted_text.split())} words.")

print("\nProcessing regular PDF...")
extracted_text_pdf = pdf_processor.process(
    input_path="private/document.pdf",           # Path to the regular PDF file
    output_path="private/pdf_output.md"           # Path to the output markdown file
)
print(f"Regular PDF processed. Extracted {len(extracted_text_pdf.split())} words.")
