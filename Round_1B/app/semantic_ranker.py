from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona, job, top_k=6):
    query = f"{persona}: {job}"
    corpus = [query] + [s["refined_text"] for s in sections]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    
    similarities = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()

    ranked_sections = []
    for idx, score in enumerate(similarities):
        section = sections[idx]
        section["importance_rank"] = int((1 - score) * 1000)  # convert to rank-like
        ranked_sections.append(section)

    ranked_sections.sort(key=lambda x: x["importance_rank"])
    return ranked_sections[:top_k]
