import streamlit as st
from utils.extract_text import extract_text_from_pdf
from utils.similarity import get_similarity
from utils.ner import extract_entities
from utils.jd_resume_parser import clean_text
import os

st.set_page_config(page_title="AI Resume Ranker", layout="wide")

st.title("📄 AI-Powered Resume Ranker")

jd_input = st.text_area("Paste the Job Description here:")

resume_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type="pdf")

if st.button("Rank Resumes"):
    if jd_input and resume_files:
        jd_clean = clean_text(jd_input)
        jd_entities = extract_entities(jd_clean)

        resume_texts = []
        resume_entities = []
        filenames = []

        for uploaded_file in resume_files:
            with open(os.path.join("resumes", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
            text = extract_text_from_pdf(f"resumes/{uploaded_file.name}")
            cleaned_text = clean_text(text)
            resume_texts.append(cleaned_text)
            resume_entities.append(extract_entities(cleaned_text))
            filenames.append(uploaded_file.name)

        scores = get_similarity(jd_clean, resume_texts)
        ranked = sorted(zip(filenames, scores, resume_entities), key=lambda x: x[1], reverse=True)

        for i, (name, score, ents) in enumerate(ranked, start=1):
            st.subheader(f"{i}. {name} — Match Score: {score:.2f}")
            st.markdown(f"Skills Found: {ents['SKILLS']}")
            st.markdown(f"Missing Skills: {list(set(jd_entities['SKILLS']) - set(ents['SKILLS']))}")
    else:
        st.warning("Please provide a JD and upload at least one resume.")