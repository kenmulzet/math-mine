# Math Mine

![GitHub repo size](https://img.shields.io/github/repo-size/kenmulzet/math-mine)
![GitHub last commit](https://img.shields.io/github/last-commit/kenmulzet/math-mine)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Made with Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-blue)

Math Mine is a Python application for generating and serving mathematics worksheets and problems. It combines topic-specific problem-generation modules with a backend API and browser-based interface.

The project grew out of mathematics curriculum development and is designed to make problem generation reproducible, modular, and easy to extend across mathematical subjects.

## Features

* Algorithmic generation of mathematics problems and worksheets
* Topic-specific Python modules for different areas of mathematics
* FastAPI-based backend for serving generated content
* Dynamic HTML worksheet rendering
* PDF generation and delivery
* Parameterized problem generation for producing varied problem sets
* Modular architecture for adding new problem types and mathematical topics

## Supported Mathematics

The repository includes problem-generation modules covering subjects such as:

* Algebra
* Calculus
* Complex numbers
* Differential equations
* Linear algebra
* Precalculus
* Probability and statistics
* Trigonometry

Additional problem types can be added by extending the existing Python modules.

## Architecture

Math Mine separates mathematical problem-generation logic from the application layer.

Individual Python modules implement generators for specific mathematical subjects. The backend coordinates requests to these generators and serves the resulting worksheets and supporting resources through HTTP endpoints.

This structure allows new problem generators to be developed independently while sharing the same application infrastructure.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/kenmulzet/math-mine.git
cd math-mine
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Install the dependencies required by the application.

### 4. Start the development server

```bash
uvicorn backend:app --reload
```

The application will be available locally at:

```text
http://127.0.0.1:8000/
```

## Repository Structure

```text
math-mine/
├── maps/
├── algebra_problems.py
├── backend.py
├── calculus_problems.py
├── complex.py
├── diffeq_problems.py
├── math_generator.html
├── README.md
└── ...
```

The subject-specific Python modules contain the mathematical generation logic, while `backend.py` provides the application backend and `math_generator.html` provides the browser interface.

## Development

New mathematical topics can be incorporated by adding or extending problem-generation modules and exposing the appropriate functionality through the backend.

The project emphasizes:

* deterministic and parameterized problem generation
* separation of mathematical logic from application logic
* reusable problem-generation components
* straightforward extension to additional mathematical subjects

## Author

**Ken Mulzet**

Mathematics professor and software developer focused on Python backend development, mathematical software, and educational technology.

[LinkedIn](https://www.linkedin.com/in/ken-mulzet-19b4866/) · [GitHub](https://github.com/kenmulzet)
