# 💼 AI-Powered Resume Ranker 🔍📄

An AI-powered web application that ranks resumes based on how well they match a given Job Description (JD). It uses cutting-edge **Natural Language Processing (NLP)** techniques like **BERT-based embeddings**, **Named Entity Recognition (NER)**, and **semantic similarity scoring**.

Built with **Streamlit** for a clean and interactive user interface.

---

## 🚀 Features

* 📄 Upload **multiple resumes** in PDF format
* 📋 Paste any **Job Description (JD)**
* 📊 Automatically **ranks resumes** based on relevance to the JD
* 🧠 Uses **NER** to extract skills, education, and work experience
* ❌ Highlights **missing skills** in each resume compared to the JD
* ⚡ Lightweight and easy to deploy locally or in the cloud

---

## 🖼️ Demo UI Flow

1. **Paste JD**
2. **Upload Resumes**
3. **Click "Rank Resumes"**
4. **View Ranked List**: See match scores, extracted skills, and missing skills

---

## 🧠 Technologies Used

| Technology           | Purpose                          |
| -------------------- | -------------------------------- |
| Python 3             | Core Programming Language        |
| Streamlit            | Web UI Framework                 |
| PyMuPDF              | PDF to Text Conversion           |
| spaCy                | Named Entity Recognition (NER)   |
| SentenceTransformers | Semantic Embeddings (BERT-based) |
| Scikit-learn         | Cosine Similarity for Matching   |

---

## 📁 Project Structure

```
ResumeRankerApp/
│
├── app.py                  # Streamlit frontend
├── requirements.txt        # Python dependencies
│
├── resumes/                # Uploaded resumes
├── job_descriptions/       # Uploaded job descriptions
│
├── utils/                  # Helper modules
│   ├── extract_text.py         # Extract text from PDF files
│   ├── jd_resume_parser.py     # Clean and parse resumes & JDs
│   ├── ner.py                  # Named Entity Recognition logic
│   └── similarity.py           # Embedding & similarity scoring
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Resume-Ranker.git

# Navigate into the project directory
cd AI-Resume-Ranker

# Install required Python packages
pip install -r requirements.txt

# Launch the application
streamlit run app.py
```

---

## 📝 Sample Usage

1. Paste a **Job Description** into the input box.
2. Upload **multiple resumes** in PDF format.
3. Click **“Rank Resumes”**.
4. View results:

   * ✅ **Match Score** (based on semantic similarity)
   * 📌 **Skills Found** in each resume
   * ❌ **Missing Skills** (as compared to the JD)

---

## 📚 Sample Files

Preloaded sample files for quick testing:

* `job_descriptions/data_scientist.txt`
* `resumes/sample_resume.txt`

---

## 🔮 Future Improvements

* 🧾 Extract more entities (e.g., years of experience, degree types)
* 📥 Generate **automated feedback PDFs** for each resume
* ☁️ **Deploy to Cloud** (Streamlit Cloud, Hugging Face Spaces)
* 📈 Add **advanced visualization** of skill match results

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Feel free to reach out for questions, feedback, or collaborations.
