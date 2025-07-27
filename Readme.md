AI-Powered Resume Ranker 🔍📄

This project is an AI-powered application that ranks resumes based on how well they match a given job description (JD). It uses modern Natural Language Processing (NLP) techniques including embeddings, Named Entity Recognition (NER), and semantic similarity scoring.

Built with Streamlit for a simple and interactive user interface.

🚀 Features

Upload multiple resumes in PDF format
Paste any job description (JD)
Automatically ranks resumes by relevance
Named Entity Recognition (NER) to extract skills, education, and experience
Highlights missing skills per resume
Lightweight and easy to deploy
🖼️ Demo UI

Paste JD → Upload Resumes → Click "Rank Resumes" → See ranked list with skills & match scores.

🧠 Technologies Used

Python 3
Streamlit (UI)
PyMuPDF (PDF to text)
spaCy (NER)
sentence-transformers (BERT-based embeddings)
Scikit-learn (cosine similarity)
📁 Project Structure

ResumeRankerApp/
├── app.py → Streamlit frontend
├── requirements.txt → Python dependencies
├── resumes/ → Uploaded resume files
├── job_descriptions/ → Uploaded JD files
├── utils/ → Helper modules
│ ├── extract_text.py → Extract text from PDF
│ ├── jd_resume_parser.py → Clean and parse text
│ ├── ner.py → Named Entity Recognition
│ └── similarity.py → Embedding & cosine similarity logic

📦 Installation

Clone this repo or unzip the folder:
git clone https://github.com/yourusername/AI-Resume-Ranker.git
Navigate into the directory:
cd AI-Resume-Ranker
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py
📝 Sample Usage

Paste a job description in the JD input box.
Upload multiple resumes in PDF format.
Click “Rank Resumes” and view the results with:
Match score (based on semantic similarity)
Skills found in resume
Missing skills (compared to JD)
📚 Sample JD & Resume

Preloaded sample files are provided in:

job_descriptions/data_scientist.txt
resumes/sample_resume.txt
🛠️ Future Improvements

Extract more entities: experience years, degree types
Support for resume feedback PDF generation
Cloud deployment (Streamlit Cloud, HuggingFace Spaces)
Advanced visualization of results