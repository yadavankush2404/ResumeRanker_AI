from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_similarity(jd_text, resume_texts):
    jd_vec = model.encode([jd_text])
    resume_vecs = model.encode(resume_texts)
    return cosine_similarity(jd_vec, resume_vecs)[0]