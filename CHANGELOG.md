# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2025-04-14

### Added
- New `PdfUnlocker` class for removing password protection from PDF files
- Command-line interface for PDF unlocking functionality
- Support for both PyPDF2 and pypdfium2 as PDF unlocking backends

### Changed
- Improved lazy loading in package initialization
- Enhanced error handling and logging throughout the package
- Updated package structure to better organize functionality

### Fixed
- Resolved issues with table extraction in scanned PDFs
- Fixed markdown formatting for tables in output
- Corrected page number handling in markdown output

## [0.1.3] - 2025-04-12

### Added
- Table detection and extraction functionality
- Support for both pure and scanned PDFs with tables
- Markdown table formatting in output

### Changed
- Improved text extraction accuracy


### Fixed
- Resolved issues with text extraction from scanned PDFs
- Fixed formatting issues in markdown output
- Corrected page number handling

## [0.1.2] - 2025-04-11

### Added
- Support for scanned PDF processing
- OCR capabilities for image-based text extraction
- Dictionary-based text correction

### Changed
- Improved text extraction accuracy
- Enhanced error handling
- Updated documentation

### Fixed
- Resolved issues with text extraction from complex PDFs
- Fixed formatting issues in markdown output

## [0.1.1] - 2025-04-10

### Added
- Basic PDF text extraction
- Markdown output formatting
- Page number support

### Changed
- Improved text extraction accuracy
- Enhanced error handling

### Fixed
- Initial bug fixes and improvements

## [0.1.0] - 2025-04-08

### Added
- Initial release
- Basic PDF text extraction functionality
- Markdown output support 