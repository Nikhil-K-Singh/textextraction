Installation Guide
==================

PyPI Installation
----------------

The easiest way to install TextExtraction is via pip:

.. code-block:: bash

    pip install textextraction

Development Installation
----------------------

For development, you can install the package with additional development dependencies:

.. code-block:: bash

    git clone https://github.com/Nikhil-K-Singh/textextraction.git
    cd textextraction
    pip install -e ".[dev]"

This will install all development dependencies including:

* pytest - for running tests
* pytest-cov - for test coverage
* flake8 - for linting
* black - for code formatting
* isort - for import sorting
* mypy - for type checking
* sphinx - for documentation

System Dependencies
------------------

TextExtraction requires two system dependencies:

1. Tesseract OCR - for text extraction from images
2. Poppler - for PDF processing

Installation instructions vary by operating system:

macOS
~~~~~

Using Homebrew:

.. code-block:: bash

    brew install tesseract poppler

Ubuntu/Debian
~~~~~~~~~~~~

Using apt:

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install -y tesseract-ocr poppler-utils

Windows
~~~~~~~

1. Install Tesseract OCR:
   
   * Download from: https://github.com/UB-Mannheim/tesseract/wiki
   * Add the installation directory to your system PATH

2. Install Poppler:
   
   * Download from: https://github.com/oschwartz10612/poppler-windows/releases/
   * Extract and add the bin/ directory to your system PATH

Verifying Installation
---------------------

You can verify the installation by running:

.. code-block:: python

    from TextExtraction import ImageText, PdfText, ScannedPdfText

    # Should not raise any import errors
    image_processor = ImageText()
    pdf_processor = PdfText()
    scanned_pdf_processor = ScannedPdfText() 