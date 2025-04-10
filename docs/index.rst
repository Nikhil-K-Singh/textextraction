Welcome to TextExtraction's documentation!
========================================

TextExtraction is a Python package for extracting and processing text from images, PDFs, and scanned PDFs. It converts the extracted text into Markdown format while preserving the original text structure and filtering out non-English words.

Features
--------

* Extract text from image files using OCR
* Extract text from regular PDF files with preserved line breaks
* Extract text from scanned PDF files using OCR
* Filter text to keep only valid English words and proper nouns
* Convert extracted text to Markdown format
* Maintain the original document structure in the output

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   contributing
   changelog

Installation
------------

You can install TextExtraction using pip:

.. code-block:: bash

   pip install textextraction

For development installation:

.. code-block:: bash

   pip install -e ".[dev]"

System Dependencies
------------------

The package requires Tesseract OCR and Poppler to be installed on your system.

macOS:

.. code-block:: bash

   brew install tesseract poppler

Ubuntu/Debian:

.. code-block:: bash

   apt-get update && apt-get install -y tesseract-ocr poppler-utils

Windows:

* Install Tesseract OCR from: https://github.com/UB-Mannheim/tesseract/wiki
* Install Poppler for Windows from: https://github.com/oschwartz10612/poppler-windows/releases/

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 