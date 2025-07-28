
**PDF Title and Outline Extractor – Documentation**

---

**Overview:**

This Python script (`code.py`) automatically extracts the main title and a structured outline (H1, H2, H3 headings) from PDF documents. It uses text properties like font size and font weight to heuristically determine the document structure. Each PDF is processed into a corresponding `.json` file with the extracted data.

---

**How It Works:**

1. **Text Extraction:**
   Scans each page of a PDF and extracts text along with its font size, font name, and page number.

2. **Body Text Identification:**
   Determines the most common font style (size + name) in the document, assuming this to be the body text.

3. **Title Extraction:**
   The largest font size found in the document is used as the main title.

4. **Heading Detection:**
   Any text larger than the body font or styled as bold is considered a heading. The top 3 unique font sizes are mapped to H1, H2, and H3.

5. **JSON Output:**
   Outputs a structured `.json` file containing the document title and a list of all detected headings, sorted by page.

---

**Directory Structure:**

```
/your-project-folder
│
├── code.py                # Main Python script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container configuration
│
└── datasets
    ├── input              # Place your PDF files here
    └── output             # JSON output files will be saved here
```

---

**🔍 How to Test on Custom Input**

1. Add your PDF file:
   Place it in the `datasets/input` folder.

   Example:

   ```
   datasets/input/your-custom-file.pdf
   ```

2. Run the script:
   Use Python locally or Docker (instructions below).

3. View the output:
   The corresponding output will be saved to:

   ```
   datasets/output/your-custom-file.json
   ```

---

**Setup Instructions (Without Docker):**

1. Install Python (3.6+)

2. (Optional) Create a virtual environment:

   ```
   python -m venv venv
   ```

   * Windows: `.\venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`

3. Add this to `requirements.txt`:

   ```
   PyMuPDF==1.23.26
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the script:

   ```
   python code.py
   ```

---

**Output Example:**

For a file named `sample-report.pdf`, the output `sample-report.json` might look like:

```
{
  "title": "Annual Financial Report 2024",
  "outline": [
    {
      "level": "H1",
      "text": "1. Introduction",
      "page": 2
    },
    {
      "level": "H2",
      "text": "1.1. Executive Summary",
      "page": 2
    },
    {
      "level": "H1",
      "text": "2. Financial Performance",
      "page": 4
    },
    {
      "level": "H2",
      "text": "2.1. Revenue Analysis",
      "page": 5
    },
    {
      "level": "H3",
      "text": "2.1.1. Q1-Q2 Performance",
      "page": 6
    }
  ]
}
```

---

**Docker Support**

This project supports Docker to avoid dependency installation and system-specific issues.

---

**Dockerfile:**

```
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY code.py .

CMD ["python", "code.py"]
```

---

**How to Use Docker:**

1. Build the Docker image:

   ```
   docker build -t pdf-outline-extractor .
   ```

2. Run the container with volume mount:

   ```
   docker run --rm -v ${PWD}/datasets:/app/datasets pdf-outline-extractor
   ```

   > On Windows PowerShell, use:
   >
   > ```
   > docker run --rm -v ${PWD}\datasets:/app/datasets pdf-outline-extractor
   > ```

---

**Requirements:**

* Python 3.6+ (if running locally)
* PyMuPDF (`pip install pymupdf`)
* Docker 

