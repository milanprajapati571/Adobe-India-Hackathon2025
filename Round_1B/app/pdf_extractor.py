import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            sections.append({
                "section_title": text.split("\n")[0][:80],  # use first line as title
                "page_number": page_num,
                "refined_text": text.strip()
            })

    return sections
