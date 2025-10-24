# 📘 Math Mine: Dynamic Problem Rendering for Educators and Engineers

![GitHub repo size](https://img.shields.io/github/repo-size/kenmulzet/math-mine)
![GitHub last commit](https://img.shields.io/github/last-commit/kenmulzet/math-mine)
![GitHub license](https://img.shields.io/github/license/kenmulzet/math-mine)
![Educator-Polished](https://img.shields.io/badge/educator--polished-✅-blue)
![Built for Clarity](https://img.shields.io/badge/built--for--clarity-🧠-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Made with Uvicorn](https://img.shields.io/badge/made--with-uvicorn-ff69b4)

Ken Mulzet is a mathematics professor turned software developer, passionate about backend architecture and data-driven applications.

- 💼 [LinkedIn](https://www.linkedin.com/in/ken-mulzet-19b4866/)
- 🧑‍💻 [GitHub](https://github.com/kenmulzet)

---

📘 Math Mine: Dynamic Problem Rendering for Educators and Engineers
Math Mine is a modular, educator-facing platform for rendering and serving math problems with precision and polish. Built for technical educators, backend engineers, and interviewers who demand clarity, it transforms static problem sets (PDFs, LaTeX, or markdown) into dynamic HTML pages with clean routing, reproducible logic, and frontend/backend sync.
Whether you're prepping students, building challenge banks, or debugging nested data workflows, Math Mine gives you:
- 📄 Dynamic rendering of math problems from static files
- 🔗 Clean URL generation for PDFs and HTMLs — no filesystem leaks
- 🧠 Educator-polished UX with toggleable views and preview links
- 🛠️ Modular backend for scaling up problem generation and metadata tagging
- 🚀 Frontend clarity with dynamic link injection and file validation
Math Mine is built to be reproducible, inspectable, and collaborative — perfect for technical interviews, classroom deployment, or open-source contribution.

---

⚙️ Setup Instructions
Follow these steps to run Math Mine locally and start serving dynamic math problems:
1. **Clone the Repository**

git clone https://github.com/kenmulzet/math-mine.git
cd math-mine

2. **Create a Virtual Environment (Optional but Recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run the Backend Server**

uvicorn backend:app --reload

5. **The server will start at http://localhost:8000**

Navigate to: http://127.0.0.1:8000/


Generate worksheets!

---

📁 Project Structure
MathMine/
├── backend/
│   ├── app.py (or main.py)
│   ├── routes/
│   └── utils/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── static/
│   ├── calculus_problems_*.pdf
│   └── generated_html/
├── templates/ (if using Flask or Django)
├── README.md
├── requirements.txt
└── .gitignore
