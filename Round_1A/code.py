import fitz  # PyMuPDF
import os
import json
from collections import Counter

SOURCE_FOLDER = "datasets/input"
DESTINATION_FOLDER = "datasets/output"

def extract_text_properties(pdf_document):
    """Extracts text properties (size, font, content, page) from a PDF."""
    text_data = []
    for p_idx, page in enumerate(pdf_document):
        blocks = page.get_text("dict")["blocks"]
        for block_data in blocks:
            if "lines" in block_data:
                for line_data in block_data["lines"]:
                    for span_data in line_data["spans"]:
                        text_content = span_data["text"].strip()
                        if text_content:
                            text_data.append((
                                round(span_data["size"]),
                                span_data["font"],
                                text_content,
                                p_idx + 1
                            ))
    return text_data

def determine_body_text_style(text_data):
    """Determines the most common font style, likely the body text."""
    if not text_data:
        return None, None
        
    style_frequencies = Counter((size, font) for size, font, _, _ in text_data)
    if not style_frequencies:
        return None, None
        
    dominant_style = style_frequencies.most_common(1)[0][0]
    return dominant_style[0], dominant_style[1]  # returns size, font

def identify_headings(text_data, body_text_size, body_text_font):
    """Identifies headings based on font size and weight relative to body text."""
    candidate_headings = []
    for size, font, text, page in text_data:
        is_bold = "bold" in font.lower()
        # Headings are larger or bolded at the same size
        if size > body_text_size or (size == body_text_size and is_bold and font != body_text_font):
            candidate_headings.append({'size': size, 'font': font, 'text': text, 'page': page})

    unique_heading_sizes = sorted(list(set(h['size'] for h in candidate_headings)), reverse=True)
    size_to_heading_map = {size: f"H{i+1}" for i, size in enumerate(unique_heading_sizes[:3])}

    document_structure = []
    for h in candidate_headings:
        if h['size'] in size_to_heading_map:
            document_structure.append({
                "level": size_to_heading_map[h['size']],
                "text": h['text'],
                "page": h['page']
            })
            
    return document_structure

def find_document_title(text_data):
    """Finds the document title, assuming it's the text with the largest font."""
    if not text_data:
        return "Untitled Document"
    
    # Title is assumed to be the span with the largest font size.
    largest_text_style = max(text_data, key=lambda item: item[0])
    return largest_text_style[2]

def analyze_pdf_structure(pdf_filepath):
    """Analyzes a single PDF to extract its title and hierarchical outline."""
    try:
        pdf_document = fitz.open(pdf_filepath)
    except Exception as e:
        print(f"Failed to open {pdf_filepath}: {e}")
        return None

    all_text_properties = extract_text_properties(pdf_document)
    if not all_text_properties:
        return {"title": "Empty or Unreadable Document", "outline": []}

    body_text_size, body_text_font = determine_body_text_style(all_text_properties)
    if body_text_size is None:
        return {"title": "Could not determine document structure", "outline": []}

    title = find_document_title(all_text_properties)
    structure = identify_headings(all_text_properties, body_text_size, body_text_font)
    
    structure.sort(key=lambda x: x['page'])
    
    # Ensure the title itself is not listed in the outline
    final_structure = [item for item in structure if item['text'] != title]

    return {
        "title": title,
        "outline": final_structure
    }

if __name__ == "__main__":
    if not os.path.exists(DESTINATION_FOLDER):
        os.makedirs(DESTINATION_FOLDER)

    for doc_name in os.listdir(SOURCE_FOLDER):
        if doc_name.lower().endswith(".pdf"):
            pdf_filepath = os.path.join(SOURCE_FOLDER, doc_name)
            print(f"Analyzing {pdf_filepath}...")
            
            analysis_result = analyze_pdf_structure(pdf_filepath)
            
            if analysis_result:
                json_filename = os.path.splitext(doc_name)[0] + ".json"
                json_filepath = os.path.join(DESTINATION_FOLDER, json_filename)
                
                with open(json_filepath, 'w', encoding='utf-8') as f:
                    json.dump(analysis_result, f, indent=2, ensure_ascii=False)
                
                print(f"Saved structure to {json_filepath}")