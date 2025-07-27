import spacy
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "ORG": [], "GPE": [], "PERSON": [],
        "DATE": [], "EDUCATION": [], "SKILLS": [],
    }

    skill_keywords = [
        "python", "tensorflow", "pytorch", "sql", "docker", "git", "react", "node", "nlp"
    ]
    lowered_text = text.lower()
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    found_skills = [s for s in skill_keywords if s in lowered_text]
    entities["SKILLS"] = list(set(found_skills))
    return entities