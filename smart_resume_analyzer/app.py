import os
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_desc = request.form['jobdesc']
        resume_path = os.path.join("uploads", resume_file.filename)
        resume_file.save(resume_path)

        resume_text = extract_text(resume_path)

        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([resume_text, job_desc])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

        jd_tokens = set(vectorizer.build_analyzer()(job_desc))
        resume_tokens = set(vectorizer.build_analyzer()(resume_text))
        missing_skills = list(jd_tokens - resume_tokens)[:10]

        result = {
            "score": round(score * 100, 2),
            "missing": missing_skills
        }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
