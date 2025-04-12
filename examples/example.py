from textextraction import ImageText, PdfText, ScannedPdfText

def process_with_tesseract():
    print("\n=== Processing with Tesseract OCR ===")
    
    # Process an image with Tesseract
    image_processor = ImageText(ocr_engine="tesseract")
    image_processor.process_image(
        image_path="/path/to/image.png",
        output_path="output_image_tesseract.md",
        filter_words=True
    )
    print("✓ Processed image with Tesseract")

    # Process a scanned PDF with Tesseract
    scanned_pdf_processor = ScannedPdfText(ocr_engine="tesseract")
    scanned_pdf_processor.process_pdf(
        pdf_path="/path/to/scanned_document.pdf",
        output_path="output_scanned_tesseract.md",
        filter_words=True
    )
    print("✓ Processed scanned PDF with Tesseract")

def process_with_easyocr():
    print("\n=== Processing with EasyOCR ===")
    
    # Process an image with EasyOCR (default)
    image_processor = ImageText()  # EasyOCR is default
    image_processor.process_image(
        image_path="/path/to/image.png",
        output_path="output_image_easyocr.md",
        filter_words=True
    )
    print("✓ Processed image with EasyOCR")

    # Process a scanned PDF with EasyOCR (default)
    scanned_pdf_processor = ScannedPdfText()  # EasyOCR is default
    scanned_pdf_processor.process_pdf(
        pdf_path="/path/to/scanned_document.pdf",
        output_path="output_scanned_easyocr.md",
        filter_words=True
    )
    print("✓ Processed scanned PDF with EasyOCR")

def process_regular_pdf():
    print("\n=== Processing Regular PDF ===")
    # Process a regular PDF (no OCR needed)
    pdf_processor = PdfText()
    pdf_processor.process_pdf(
        pdf_path="/path/to/document.pdf",
        output_path="output_pdf.md",
        filter_words=True
    )
    print("✓ Processed regular PDF")

if __name__ == "__main__":
    # Process with both OCR engines
    process_with_tesseract()
    process_with_easyocr()
    process_regular_pdf()
