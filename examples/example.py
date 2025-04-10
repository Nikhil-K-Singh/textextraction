from TextExtraction import ImageText, PdfText, ScannedPdfText

# Process an image
image_processor = ImageText()
image_processor.process_image(
    image_path="path/to/image.png", output_path="output_image.md", filter_words=True
)

# Process a regular PDF
pdf_processor = PdfText()
pdf_processor.process_pdf(
    pdf_path="path/to/document.pdf", output_path="output_pdf.md", filter_words=True
)

# Process a scanned PDF
scanned_pdf_processor = ScannedPdfText()
scanned_pdf_processor.process_pdf(
    pdf_path="path/to/scanned_document.pdf",
    output_path="output_scanned.md",
    filter_words=True,
)
