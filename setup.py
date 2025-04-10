from setuptools import setup, find_packages

setup(
    name="textextraction",
    version="0.1.0",
    author="Nikhil K Singh",
    author_email="nsr.nikhilsingh@gmail.com",
    description="Extract and process text from images and PDFs",
    long_description=open(file="README.md", mode="r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nikhil-K-Singh/textextraction/tree/main",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "nltk>=3.9,<4.0",
        "Pillow>=11.0,<12.0",
        "pdfminer.six>=20221105",
        "pytesseract>=0.3.0",
        "pdf2image>=1.17.0,<2.0",
        "regex>=2024.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
            "sphinx>=7.0.0",
        ],
    },
)
