import os
import subprocess
from datetime import datetime

def compile_latex_to_pdf(tex_file):
    try:
        print(f"tex_file name = {tex_file}")
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            check=True
        )
        print(f"✅ PDF successfully generated from {tex_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ LaTeX compilation failed: {e}")

def export_to_latex(problems, include_answers, subject, name_date = False, title = ""):
    os.makedirs("static", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"calculus_problems_{timestamp}.tex"
#    filepath = os.path.join("static", os.path.basename(filename))
    filepath = os.path.join("static", filename)

    if title == "":
        title = subject + " Worksheet"

    header = fr"""\documentclass[12pt]{{article}}
\usepackage{{amsmath}}
\title{{{title}}}
\begin{{document}}
\maketitle
\begin{{enumerate}}
"""
    footer = r"""\end{enumerate}
\end{document}
"""

    body = ""
    for q, a in problems:
        body += f"  \\item {q}\n"
        if include_answers:
            body += f"  \\newline \\textbf{{Answer:}} {a}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + body + footer)
    
    compile_latex_to_pdf(filepath)
    filepath = filepath[:-4] + ".pdf"
    source = filename[:-4] + ".*"

    destination_dir = os.path.dirname(filepath)
    try:
        # Use subprocess to execute the move command
        result = subprocess.run(
            ["move", source, destination_dir],
            shell=True,  # Required for Windows to execute shell commands
            check=True,  # Raise an exception if the command fails
            text=True,   # Ensures output is returned as a string
        )
        print(f"File moved successfully from '{source}' to '{destination_dir}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to move file. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return filepath