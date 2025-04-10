Contributing Guide
==================

Thank you for considering contributing to TextExtraction! This document provides guidelines and instructions for contributing.

Development Setup
----------------

1. Fork and Clone
~~~~~~~~~~~~~~~~

First, fork the repository on GitHub, then clone your fork:

.. code-block:: bash

    git clone https://github.com/YOUR_USERNAME/textextraction.git
    cd textextraction

2. Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
~~~~~~~~~~~~~~~~~~~~~

Install the package in development mode with all development dependencies:

.. code-block:: bash

    pip install -e ".[dev]"

Development Workflow
------------------

1. Create a Branch
~~~~~~~~~~~~~~~~

Create a branch for your feature or bugfix:

.. code-block:: bash

    git checkout -b feature/amazing-feature

2. Make Changes
~~~~~~~~~~~~~

Make your changes to the code. Be sure to:

* Follow PEP 8 style guidelines
* Add docstrings for new functions/classes
* Add or update tests as needed
* Update documentation if needed

3. Code Quality
~~~~~~~~~~~~~

Before committing, run:

.. code-block:: bash

    # Format code
    black .
    isort .

    # Run linter
    flake8

    # Run type checker
    mypy .

    # Run tests
    pytest
    pytest --cov=TextExtraction tests/

4. Commit Changes
~~~~~~~~~~~~~~~

.. code-block:: bash

    git add .
    git commit -m "Add amazing feature"
    git push origin feature/amazing-feature

5. Submit Pull Request
~~~~~~~~~~~~~~~~~~~

Go to GitHub and submit a Pull Request from your feature branch to the main repository's main branch.

Documentation
------------

To build the documentation locally:

.. code-block:: bash

    cd docs
    make html

The built documentation will be in ``docs/_build/html``. 