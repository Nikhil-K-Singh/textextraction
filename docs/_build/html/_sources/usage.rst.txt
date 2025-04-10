Usage Guide
===========

Basic Usage
----------

Here's how to use the main features of TextExtraction:

Processing Images
~~~~~~~~~~~~~~~~

.. code-block:: python

    from TextExtraction import ImageText

    # Initialize the image processor
    image_processor = ImageText()

    # Process an image and save to markdown
    markdown_text = image_processor.process_image(
        image_path="path/to/image.png",
        output_path="output_image.md",
        filter_words=True
    )

Processing PDFs
~~~~~~~~~~~~~~

.. code-block:: python

    from TextExtraction import PdfText

    # Initialize the PDF processor
    pdf_processor = PdfText()

    # Process a PDF and save to markdown
    markdown_text = pdf_processor.process_pdf(
        pdf_path="path/to/document.pdf",
        output_path="output_pdf.md",
        filter_words=True
    )

Processing Scanned PDFs
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from TextExtraction import ScannedPdfText

    # Initialize the scanned PDF processor
    scanned_pdf_processor = ScannedPdfText()

    # Process a scanned PDF and save to markdown
    markdown_text = scanned_pdf_processor.process_pdf(
        pdf_path="path/to/scanned_document.pdf",
        output_path="output_scanned.md",
        filter_words=True
    )

Advanced Usage
-------------

Text Filtering
~~~~~~~~~~~~~

By default, the text filtering process:

* Keeps valid English words
* Preserves proper nouns (capitalized words)
* Maintains technical terms with at least 3 characters
* Preserves the original document structure

You can disable filtering by setting ``filter_words=False`` in any process method:

.. code-block:: python

    markdown_text = processor.process_image(
        image_path="path/to/image.png",
        output_path="output.md",
        filter_words=False  # Disable filtering
    )

Custom Processing
~~~~~~~~~~~~~~~

You can also use the individual processing steps:

.. code-block:: python

    from TextExtraction import ImageText

    processor = ImageText()

    # Extract text
    extracted_text = processor.extract_from_image("path/to/image.png")

    # Filter text (optional)
    filtered_text = processor.filter_english_words(extracted_text)

    # Convert to markdown
    markdown_text = processor.to_markdown(filtered_text, title="Custom Title") 