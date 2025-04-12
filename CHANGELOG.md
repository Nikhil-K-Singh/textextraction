# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2024-07-30

### Added
- Added support for mixed content (text and tables) on the same page

- Added PyMuPDF dependency for better PDF handling
- Always use EasyOCR for table detection even when Tesseract is selected as main OCR engine
- Better handling of complex table structures 
- Support for page range selection in PDF processing

### Changed
- Enhanced table formatting in markdown output
- Improved error handling and dependency checks


## [0.1.2] - 2025-04-15

### Added
- Support for EasyOCR engine
- Better line and paragraph handling

## [0.1.1] - 2025-01-20

### Added
- Initial release with basic OCR functionality
- Support for images and PDFs
- Tesseract OCR integration

## [0.1.0] - 2025-04-10

### Added
- Initial release
- Support for text extraction from images
- Support for text extraction from regular PDFs
- Support for text extraction from scanned PDFs
- English word filtering
- Markdown output formatting 