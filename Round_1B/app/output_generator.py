def generate_output(ranked_data, config, timestamp):
    output = {
        "metadata": {
            "input_documents": config["documents"],
            "persona": config["persona"],
            "job_to_be_done": config["job_to_be_done"],
            "processing_timestamp": timestamp
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    rank = 1
    for entry in ranked_data:
        if not entry["section_title"].strip():
            continue

        output["extracted_sections"].append({
            "document": entry["document"],
            "section_title": entry["section_title"].strip(),
            "importance_rank": rank,
            "page_number": entry["page_number"]
        })

        output["subsection_analysis"].append({
            "document": entry["document"],
            "refined_text": entry["refined_text"].strip(),
            "page_number": entry["page_number"]
        })

        rank += 1

    return output
