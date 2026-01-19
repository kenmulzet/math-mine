import os
import copy
import zipfile
import traceback
from typing import Optional;
from datetime import datetime
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
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
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000", "http://localhost:3000", "http://127.0.0.1:3000"],  # You can restrict this later
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

@app.get("/download_all")
def download_all(
        pdf_filename: str = Query(...), 
        answer_filename: str = Query(...)
):
    ws_pdf = os.path.join("static", pdf_filename)
    ans_pdf = os.path.join("static", answer_filename)

    print(f"ws_pdf = ", ws_pdf)
    if not os.path.exists(ws_pdf) or not os.path.exists(ans_pdf):
        raise HTTPException(status_code=404, detail="Files not found")

    zip_filename = "bundle.zip"
    zip_path = os.path.join("static", zip_filename)

    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(ws_pdf, arcname=os.path.basename(ws_pdf))
        zipf.write(ans_pdf, arcname=os.path.basename(ans_pdf))

    return FileResponse(zip_path, filename=zip_filename)

# 🔧 Utility function: HTML exporter
def export_to_html(problems, category="Algebra", title=""):
    os.makedirs("static", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"math_problems_{timestamp}.html"
    filepath = os.path.join("static", filename)
    if title == "":
        title = category + " Worksheet"

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
        <h2>{title}</h2>
        <ol>
    """

    for q, a in problems:
        html += f"<li>{q}"
        html += "</li>"

    html += """
        </ol>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return html, filename

def export_latex_to_html(calc_problems, problem_type = "calculus", title = ""):
    os.makedirs("static", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{problem_type}_problems_{timestamp}.html"
    filepath = os.path.join("static", os.path.basename(filename))

    html_body = ""
    for question, answer in calc_problems:
#        print(f"question: {question}")
#        print(f"answer: {answer}")
        if f"$a_1 = " in question:
            question = question.replace(f"$a_n$", f"a<sub>n</sub>")
            question = question.replace(f"$a_1 = ", f"a<sub>1</sub> = ")
            question = question.replace(f"a_2 = ", f"a<sub>2</sub> = ")
            question = question.replace(f"$, and", ", and")
        html_body += f"<li>{question}"
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
      <h2 style="text-align:center;">{title}</h2>
      <ol>{html_body}</ol>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return html, filename

def export_to_pdf(text_lines: list[str], subject, name_date=False, title=""):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Worksheet filename
    filename = f"{subject}_ws_{timestamp}.pdf"
    filepath = os.path.join("static", filename)

    # Answer key filename
    answers_filename = f"{subject}_answers_{timestamp}.pdf"
    answers_filepath = os.path.join("static", answers_filename)

    # --- Worksheet PDF ---
    pdf = FPDF()
    pdf.add_page()

    # Title
    if title == "":
        title = f"{subject.capitalize()} Worksheet"
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.ln(5)

    # Optional name/date line (worksheet only)
    if name_date:
        pdf.set_font("Arial", size=12)
        pdf.cell(
            200,
            10,
            txt="Name ____________________    Date ____________________",
            ln=True,
            align="C",
        )
        pdf.ln(5)

    # Problems
    pdf.set_font("Arial", size=12)
    for i, line in enumerate(text_lines, start=1):
        prob = line[0] if isinstance(line, (list, tuple)) else line
        pdf.multi_cell(0, 10, txt=f"{i}. {prob}")

    pdf.output(filepath)

    # --- Answer Key PDF ---
    pdf_ans = FPDF()
    pdf_ans.add_page()
    pdf_ans.set_font("Arial", style="B", size=16)
    pdf_ans.cell(200, 10, txt=f"{subject.capitalize()} Answer Key", ln=True, align="C")
    pdf_ans.ln(5)

    pdf_ans.set_font("Arial", size=12)
    for i, line in enumerate(text_lines, start=1):
        # If text_lines are tuples like (problem, answer), use the answer
        if isinstance(line, (list, tuple)) and len(line) > 1:
            ans = line[1]
        else:
            ans = "N/A"
        pdf_ans.multi_cell(0, 10, txt=f"{i}. {ans}")

    pdf_ans.output(answers_filepath)

    return filename, answers_filename


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
def generate_problems_from_data(problem_data: dict):
    problems = []
    for problem_type, count in problem_data.items():
        generator = generator_map.get(problem_type)
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
        print(problem_data)

        # Optional flags (already snake_case)
        include_name_date = problem_data.pop("include_name_date", False)
        change_title      = problem_data.pop("change_title", False)
        title             = problem_data.pop("title", "")
        print(f"include_name_date = ", include_name_date)
        print(f"change_title = ", change_title)
        print(f"title = ", title)

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

        print(f"subject = ", subject)
        # Generate problems and export to HTML
        problems = generate_problems_from_data(problem_data)
        print("generated problems")
        if (subject == "Calculus") or (subject == "Differential Equations"):
            # deep copy so nested dicts inside problems are duplicated
            problems_for_pdf = copy.deepcopy(problems)
            problems_for_html = copy.deepcopy(problems)

            PDF_filename, Answer_key_filename = export_to_latex(problems_for_pdf, subject, include_name_date, title)
            html, HTML_filename = export_latex_to_html(problems_for_html, subject, title)
        else:
            html, HTML_filename = export_to_html(problems, subject, title)
            PDF_filename, Answer_key_filename = export_to_pdf(problems, subject, include_name_date, title)

        print(f"PDF_filename = {PDF_filename}")
        print(f"HTML_filename = {HTML_filename}")
        print(f"Answer_key_filename = {Answer_key_filename}")

        # Return both HTML and filename to frontend
        return JSONResponse(content={
            "html": html, 
            "HTML_filename": HTML_filename, 
            "PDF_filename": PDF_filename, 
            "Answer_key_filename": Answer_key_filename})

    except Exception as e:
        print(f"[ERROR] /generate failed: {e}\n{traceback.format_exc()}")
        return HTMLResponse(content=f"<h1>Internal Server Error</h1><p>{e}</p>", status_code=500)
