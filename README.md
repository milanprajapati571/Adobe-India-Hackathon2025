

# 🎯 Adobe India Hackathon Solutions

This repository contains the solutions for the challenges presented during the Adobe India Hackathon 2025. The project is divided into two distinct rounds, each located in its own self-contained folder.

---

## 🚀 Project Overview

This project tackles two document intelligence challenges, demonstrating capabilities in PDF data extraction, structural analysis, and semantic understanding using modern NLP and document processing techniques.

---

## 📘 Round 1A: PDF Outline Extraction

* **Objective**: Automatically analyze PDF documents to extract a structured outline.
* **Approach**: The system identifies the document's title and hierarchical headings (H1, H2, H3) by analyzing font properties such as size and weight.
* **Output**: For each input PDF, a `.json` file is generated containing the structured outline of the document.

For more details, navigate to the `Round_1A` directory.

---

## 📗 Round 1B: Persona-Driven Document Intelligence

* **Objective**: Acts as an intelligent document analyst. Given:

  * A user **persona** (e.g., Investment Analyst)
  * A **job-to-be-done** (e.g., Analyze revenue trends)
  * A set of PDF documents

  The system identifies and ranks the most relevant sections and sub-sections across all documents.

* **Output**: A single `.json` file with:

  * Metadata
  * A ranked list of top relevant sections
  * Refined sub-section analyses

For more details, navigate to the `Round_1B` directory.

---

## 📂 Dataset Setup

The `Datasets/` directory provides all the required input files for testing both rounds.

### 🗂️ `Datasets/Input_Round_1A/`

* Contains sample **PDF files** for testing the Round 1A model.
* ✅ **To test**: Copy all the PDF files from this folder to:

  ```
  Round_1A/datasets/input/
  ```

### 🗂️ `Datasets/Input_Round_1B/`

* Contains folders: `set1/`, `set2/`, `set3/`.

* Each set includes:

  * An `input.json` file (containing the persona, job-to-be-done, and list of associated PDFs)
  * The PDF files used in that input

* ✅ **To test**: For each set (e.g., `set1`), copy both `input.json` and all PDFs to:

  ```
  Round_1B/datasets/input/
  ```

  Replace the files as needed for each test set.

> Refer to the README.md files inside `Round_1A/` and `Round_1B/` folders for exact steps to run the code.

---

## 🧰 Technology Stack

* **Language**: Python 3.9+
* **PDF Processing**: PyMuPDF (fitz)
* **Semantic Search (Round 1B)**: sentence-transformers (`all-MiniLM-L6-v2`)
* **Optional Similarity Metric**: TF-IDF (scikit-learn)
* **Containerization**: Docker

---

## 👥 Contributors

* [@milanprajapati571](https://github.com/milanprajapati571)
* [@Kunal-3004](https://github.com/Kunal-3004)


