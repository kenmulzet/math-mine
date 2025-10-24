import os
import traceback
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
import json
import algebra_problems as alg
import calculus_problems as calc
import geometry_problems as geom
import diffeq_problems as diffeq
from latex_compile import export_to_latex

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with open("math_generator.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/maps/{map_name}")
def get_map(map_name: str):
    try:
        with open(f"maps/{map_name}_map.json") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except FileNotFoundError:
        return JSONResponse(content={"error": "Map not found"}, status_code=404)

# 🔧 Utility function: HTML exporter
def export_to_html(problems, include_answers=True, category="Algebra"):
    os.makedirs("static", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"math_problems_{timestamp}.html"
    filepath = os.path.join("static", filename)

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Math Worksheet – </title>
        <style>
            body {{ font-family: Georgia, serif; margin: 2em; }}
            h2 {{ text-align: center; }}
            ol {{ line-height: 1.6; }}
            li {{ margin-bottom: 1em; }}
            .answer {{ color: #2c3e50; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h2>{category} Practice Worksheet</h2>
        <ol>
    """

    for q, a in problems:
        html += f"<li>{q}"
        if include_answers:
            html += f"<br><span class='answer'>Answer:</span> {a}"
        html += "</li>"

    html += """
        </ol>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return html, filename

def export_latex_to_html(calc_problems, include_answers=True, problem_type = "calculus"):
    os.makedirs("static", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{problem_type}_problems_{timestamp}.html"
    filepath = os.path.join("static", os.path.basename(filename))

    html_body = ""
    for question, answer in calc_problems:
        print(f"question: {question}")
        print(f"answer: {answer}")
        html_body += f"<li>{question}"
        if include_answers:
            html_body += f"<br><span class='answer'>Answer:</span> {answer}"
        html_body += "</li>"

    html = f"""
    <html>
    <head>
      <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
      <script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
      </script>
      <style>
        body {{ font-family: sans-serif; }}
        ol {{ padding-left: 1.2em; }}
        li {{ margin-bottom: 1em; }}
        .answer {{ color: green; font-weight: bold; }}
      </style>
    </head>
    <body>
      <ol>{html_body}</ol>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return html, filename

def export_to_pdf(text_lines: list[str], subject) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{subject}_ws_{timestamp}.pdf"
    filepath = os.path.join("static", filename)
    pdf = FPDF()
    pdf.add_page()
    
    # Format title based on subject
    title = f"{subject.capitalize()} Worksheet"

    # Title styling
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.ln(5)

    # Problem list
    pdf.set_font("Arial", size=12)
    for i, line in enumerate(text_lines, start=1):
        prob = line[0] if isinstance(line, (list, tuple)) else line
        pdf.multi_cell(0, 10, txt=f"{i}. {prob}")

    try:
        pdf.output(filepath)
        return filepath
    except Exception as e:
        raise RuntimeError(f"PDF export failed: {e}")

@app.route("/")
def index():
    return render_template_string(open("index.html").read())

# ✅ Global generator map
def load_domain_map(path, module):
    with open(path, "r", encoding="utf-8") as f:
        raw_map = json.load(f)

    function_map = {}
    label_map = {}
    key_list = []

    for key, value in raw_map.items():
        function_map[key] = getattr(module, value["function"])  # ✅ actual function object
        label_map[key] = value["label"]
        key_list.append(key)

    return function_map, label_map, key_list

generator_map = {}
algebra_map, algebra_labels, algebra_keys = load_domain_map("maps/algebra_map.json", alg)
generator_map.update(algebra_map)
print(f"algebra_keys = {algebra_keys}")

calculus_map, calculus_labels, calculus_keys = load_domain_map("maps/calculus_map.json", calc)
generator_map.update(calculus_map)
print(f"calculus_keys = {calculus_keys}")

geometry_map, geometry_labels, geometry_keys = load_domain_map("maps/geometry_map.json", geom)
generator_map.update(geometry_map)
print(f"geometry_keys = {geometry_keys}")

diffeq_map, diffeq_labels, diffeq_keys = load_domain_map("maps/diffeq_map.json", diffeq)
generator_map.update(diffeq_map)
print(f"diffeq_keys = {diffeq_keys}")

# ✅ Shared logic
def generate_problems_from_data(problem_data: dict, include_answers: bool):
    problems = []
    for problem_type, count in problem_data.items():
        generator = generator_map.get(problem_type)
        print(f"generator = {generator}")
        if not generator:
            print(f"Unknown problem type: {problem_type}")
            continue
        for _ in range(count):
            problems.append(generator())
    return problems

# ✅ JSON-based route
@app.post("/generate")
async def generate_worksheet(request: Request):
    try:
        # Parse incoming JSON
        problem_data = await request.json()
        include_answers = problem_data.pop("include_answers", False)

        for key in problem_data:
            problem_type = key
            break
    
        subject = (
            "Algebra" if problem_type in algebra_keys else
            "Calculus" if problem_type in calculus_keys else
            "Geometry" if problem_type in geometry_keys else
            "Differential Equations" if problem_type in diffeq_keys else
            "Math"
        )

        # Generate problems and export to HTML
        problems = generate_problems_from_data(problem_data, include_answers)
        if (subject == "Calculus") or (subject == "Differential Equations"):
            PDF_filename = export_to_latex(problems, include_answers, subject)
            html, HTML_filename = export_latex_to_html(problems, include_answers, subject)
            print(f"PDF_filename = {PDF_filename}")
            print(f"HTML_filename = {HTML_filename}")
        else:
            html, HTML_filename = export_to_html(problems, include_answers, subject)
            PDF_filename = export_to_pdf(problems, subject)

        # Return both HTML and filename to frontend
        return JSONResponse(content={"html": html, "HTML_filename": HTML_filename, "PDF_filename": PDF_filename})

    except Exception as e:
        print(f"[ERROR] /generate failed: {e}\n{traceback.format_exc()}")
        return HTMLResponse(content=f"<h1>Internal Server Error</h1><p>{e}</p>", status_code=500)
