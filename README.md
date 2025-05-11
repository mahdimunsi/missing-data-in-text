# Text Restoration Tools

This repository contains a collection of Python scripts for restoring missing or degraded text in documents. These scripts are designed to handle basic text recovery scenarios, including masked token prediction, multiple gap filling, and OCR-based text restoration for scanned PDFs.

---

## **Included Tools:**

### 1. Single Token Unmasker ([single_unmasker.py](./single_unmasker.py))
A simple interactive script that uses a BERT model to predict single masked tokens in a sentence.

**Key Features:**
- Interactive command-line interface
- Real-time token prediction
- Supports multiple top-k predictions

**Usage:**
```bash
python single_unmasker.py
```

### 2. Multiple Token Unmasker ([multiple_unmasker.py](./multiple_unmasker.py))
An extended version that can handle multiple [MASK] tokens in a single sentence, replacing each one in sequence until the text is fully restored.

**Key Features:**
- Handles multiple masks in a single pass
- Iteratively replaces masks until the sentence is complete
- Simple and efficient approach for text reconstruction

**Usage:**
```bash
python multiple_unmasker.py
```

### 3. PDF Restoration Pipeline ([pdf_restoration_pipeline.py](./pdf_restoration_pipeline.py))
A comprehensive pipeline for restoring text from scanned PDFs using OCR and GPT-based text refinement.

**Key Features**
- Extracts text from scanned PDF pages using EasyOCR
- Cleans and refines extracted text using OpenAI's GPT API
- Reconstructs a polished PDF output
- Handles noisy, low-quality scans effectively

**Usage:**
1. Set up your OpenAI API key in the `pdf_restoration_pipeline.py`:
```python
API_KEY = "your-openai-api-key"
```
2. Change your input pdf and output location in the same script (you can use the example document `Honkela95.pdf` to get the output `Honkela95_refined.pdf`):
```python
PDF_PATH = 'Honkela95.pdf'
OUTPUT_PDF = 'Honkela95_refined.pdf'
```
3. Save it and run the script:
```bash
python pdf_restoration_pipeline.py
```


## Installation
### Requirements
- Python 3.10+
- Required libraries:
```bash
pip install torch transformers easyocr openai pdf2image pillow pymupdf fpdf
```

## Contributors
1. Mahdi Munshi (mahdi.munshi@helsinki.fi)
2. Maria Strzelecka (maria.strzelecka@helsinki.fi)
3. Ruiting Li (ruiting.li@helsinki.fi)

### Acknowledgement
Special thanks to **Maria Valaste** for her guidance throughout the course and the project.
