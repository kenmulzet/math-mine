# Math Mine

Math Mine is a personal Python project for generating mathematics problems and worksheets. It combines topic-specific problem generators, a FastAPI backend, and a browser-based interface for producing instructional materials.

## Features

- Parameterized mathematical problem generation
- Subject-specific Python modules, including algebra, calculus, differential equations, and geometry
- FastAPI application in `backend.py`
- Browser interface in `math_generator.html`
- Worksheet rendering and PDF-related functionality

## Project structure

- `backend.py` — web application and API endpoints
- `math_generator.html` — browser interface
- `*_problems.py` — topic-specific generators
- `problem_registry.json` — problem registry
- `latex_compile.py` — LaTeX-related processing
- `maps/` — supporting project resources

## Local development

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/kenmulzet/math-mine.git
cd math-mine
python -m venv .venv
```

Activate it:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the application's required Python dependencies in the environment. A pinned dependency manifest is a planned improvement; inspect the imports and system prerequisites before installation. At minimum, the backend uses FastAPI and an ASGI server such as Uvicorn.

Start the backend:

```bash
uvicorn backend:app --reload
```

The local server normally listens on `http://127.0.0.1:8000`. See `backend.py` for the available routes. Depending on the worksheet export path, additional LaTeX or PDF tooling may be required.

> **Setup status:** These instructions reflect the repository structure but have not yet been validated in a clean environment. Dependency pinning and a reproducible setup guide are tracked in the roadmap.

## Development roadmap

See [ROADMAP.md](ROADMAP.md) for planned work on tests, generator coverage, API quality, export reliability, and documentation. The roadmap describes future work, not features claimed as already complete.

## Ownership and license

Math Mine is an independently developed personal project by Ken Mulzet. Distributed under the [MIT License](LICENSE).
