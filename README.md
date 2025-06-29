# 🧠 Smart Resume Analyzer

An AI-powered resume matching tool that compares your resume with a job description, calculates a similarity score, and highlights missing skills. Ideal for job seekers to tailor their resumes and for recruiters to shortlist candidates effectively.

---

## 📌 Features

- 📄 Upload resumes in **PDF** format
- 📝 Paste job descriptions directly
- 🔍 **Match score** calculation using TF-IDF + Cosine Similarity
- ⚠️ Highlights **missing skills or keywords**
- 🌐 Flask-based **web interface**
- 📁 Offline tool – no internet or data upload required
- 📤 Optional: **PDF report generation**

---

## 🚀 Demo

**Sample Output**
```
Match Score: 82%
Missing Skills: ['flask', 'rest', 'docker']
```

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **pdfminer.six** (PDF resume parsing)
- **scikit-learn** (TF-IDF, similarity)
- **FPDF** (optional report generation)
- **HTML/CSS** (frontend UI)

---

## 🖥️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/smart-resume-analyzer.git
   cd smart-resume-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install flask pdfminer.six scikit-learn fpdf
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser:
   ```
   http://localhost:5000
   ```

---

## 📂 Project Structure

```
.
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Temporary storage for resumes
├── sample_resume.pdf     # Example resume to test
└── README.md             # Project overview
```

---

## 🌱 Future Enhancements

- Use **BERT/SBERT** for better semantic similarity
- Add **batch resume processing** for recruiters
- Integrate **LinkedIn API** for JD fetching
- Use **Named Entity Recognition (NER)** to extract experience, companies, etc.
- Deploy to **Heroku or AWS**

---

## 👤 Author

**Manju THershini**  
`B.Tech CSE | Vel Tech High Tech Engineering College`  

