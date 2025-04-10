# Contributing to TextExtraction

Thank you for considering contributing to TextExtraction!

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/Nikhil-K-Singh/textextraction.git
cd textextraction

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

## Code Style

Please follow PEP 8 guidelines and include docstrings for all functions and classes.

## Running Tests

```bash
pytest
```

### CHANGELOG.md

```markdown:CHANGELOG.md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-XX-XX

### Added
- Initial release
- Support for text extraction from images
- Support for text extraction from regular PDFs
- Support for text extraction from scanned PDFs
- English word filtering
- Markdown output formatting
```

### GitHub Workflows (CI/CD)

Create a `.github/workflows` directory with a workflow for testing:

```yaml:.github/workflows/python-test.yml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y tesseract-ocr poppler-utils
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        pip install -e .
    - name: Test with pytest
      run: |
        pytest
```

## Enhance Your README.md

Add badges to your README.md:

```markdown
# TextExtraction

[![PyPI version](https://badge.fury.io/py/textextraction.svg)](https://badge.fury.io/py/textextraction)
[![Python Versions](https://img.shields.io/pypi/pyversions/textextraction.svg)](https://pypi.org/project/textextraction/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

TextExtraction is a Python package for extracting and processing text from images, PDFs, and scanned PDFs...
```

## After Uploading to GitHub

1. **Link to PyPI**: Add your GitHub URL to your PyPI project page
2. **Create a Release**: Create a release on GitHub that corresponds to your PyPI version
3. **Setup Documentation**: Consider setting up Read the Docs to host your documentation
4. **Issue Templates**: Add issue and pull request templates to standardize contributions

By maintaining your code on GitHub, you make it easier for others to contribute, report issues, and for you to manage versions and updates. 