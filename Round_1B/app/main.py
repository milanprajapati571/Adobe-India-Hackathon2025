from app.pdf_extractor import extract_text_blocks
from app.semantic_ranker import rank_sections
from app.output_generator import generate_output
from app.utils import read_input_json
import os
from datetime import datetime
import json

def main():
    config = read_input_json("datasets/input/input.json")
    persona_desc = config["persona"]
    job_goal = config["job_to_be_done"]
    documents = config["documents"]

    content_pool = []

    for item in documents:
        path = os.path.join("datasets/input", item["filename"])
        sections = extract_text_blocks(path)
        for s in sections:
            s["document"] = item["filename"]
            content_pool.append(s)

    refined_segments = rank_sections(content_pool, persona_desc, job_goal, top_k=6)

    output = generate_output(refined_segments, config, datetime.now().isoformat())

    with open("datasets/output/output.json", "w", encoding="utf-8") as out_file:
        json.dump(output, out_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
