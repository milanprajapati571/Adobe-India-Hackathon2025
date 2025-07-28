

# Persona-Driven Document Intelligence System 🧠📄

A document intelligence system that extracts and ranks the **top relevant sections** from multiple PDFs based on a given **persona** and **job-to-be-done**. Developed for the **Adobe India Hackathon 2025**.

---

## 🗂 File Structure

```
Project/
├── app/
│   ├── main.py
│   ├── pdf_processor.py
│   ├── semantic_ranker.py
│   ├── output_generator.py
├── datasets/
│   ├── input/
│   └── output/
├── input/
│   └── input.json
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works – Step-by-Step

### 1. 📥 Input

* Reads `input/input.json` containing:

  * A **persona**
  * A **job to be done**
  * A list of PDF filenames located in `datasets/input/`

### 2. 📄 PDF Processing

* Extracts text from each page using PyMuPDF.
* Detects a **section title** and the **paragraph body**.
* Filters out any page without a valid section title.

### 3. 🔍 Semantic Ranking

* Each section is ranked based on its relevance to the persona and job-to-be-done.

---

## 🤖 Model Used: **TF-IDF with Cosine Similarity**

### 📌 Why TF-IDF?

* **TF-IDF (Term Frequency–Inverse Document Frequency)** is a fast and lightweight technique to numerically represent how important a word is in a document relative to a collection of documents.
* It helps filter out common words and prioritize important ones — critical for identifying semantic alignment with the input persona and job.

### ⚙️ How It Works:

1. Combines the **persona** and **job description** into a single query.
2. Vectorizes all section texts and the query using TF-IDF.
3. Measures **cosine similarity** between each section and the query.
4. Ranks and selects the top N sections with the highest similarity scores.

### 🎯 Why Not LLMs?

* TF-IDF offers:

  * Simplicity
  * Low resource usage
  * Fast inference
* Ideal for fast prototyping in environments with resource/time constraints like hackathons.

---

## 💡 Use Case Example

If the persona is a "**Technical Recruiter**" and the job is "**Evaluate a candidate’s open-source contributions**", then the system:

* Scans all provided PDFs (resumes, portfolios, reports)
* Extracts the most relevant sections (e.g., "GitHub Projects", "Open Source Contributions")
* Outputs a ranked list highlighting only what the recruiter cares about

---

## 📤 Output

* A JSON file is generated inside `datasets/output/` with:

  * Extracted sections
  * Refined text
  * Metadata

---

## 🚀 How to Run

### Option 1: Local

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Add your PDFs to:

   ```
   datasets/input/
   ```

3. Modify `input/input.json` as needed.

4. Run:

   ```
   python -m app.main
   ```

5. Output will be saved in `datasets/output/output.json`.

---

### Option 2: Docker

1. Build the Docker image:

   ```
   docker build -t document-intelligence .
   ```

2. Run the app:

   ```
   docker run --rm -v "$(pwd)/datasets":/app/datasets -v "$(pwd)/input":/app/input document-intelligence
   ```

---

## 🧪 Test with New PDFs

* Place PDFs in `datasets/input/`
* Edit `input/input.json` with correct filenames
* Run `python -m app.main`

---

## 🛠 Tech Stack

* Python 3.9+
* PyMuPDF
* scikit-learn (for TF-IDF & cosine similarity)
* Docker

---

## ✅ Output Format

Example:

```json
{
  "document": "France Guide.pdf",
  "section_title": "Top Attractions",
  "importance_rank": 1,
  "page_number": 2
}
```

---

## 📌 Notes

* Sections without a title are skipped.
* Ranking is based on the top 10 across all files.
* Fast execution (<3 seconds for multiple PDFs).
* Designed for adaptability — you can swap TF-IDF with more advanced models like SBERT for richer semantics if needed.

