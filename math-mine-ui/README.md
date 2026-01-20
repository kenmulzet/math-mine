# Math Mine React 🧮⚛️

A React frontend for **Math Mine**, a worksheet generator powered by a Python/FastAPI backend.  
This project demonstrates full‑stack capability: modular backend APIs + modern React UI with dynamic analytics.

---

## ✨ Features

- **Problem Type Selection**  
  Choose from multiple math categories (Algebra, Geometry, Calculus, etc.) via dropdown.

- **Customizable Worksheet Options**  
  - Include Name/Date line  
  - Toggle answer inclusion  
  - Change worksheet title dynamically  

- **Problem Counts**  
  Input the number of problems per type with clean, responsive form controls.

- **File Generation & Download**  
  - HTML worksheet output  
  - PDF answer files  
  - Answer key download  
  - “Download All” button for convenience

- **Histogram Analytics**  
  - Toggle button to show/hide problem distribution chart  
  - Responsive Chart.js bar chart  
  - Matches vanilla frontend functionality, now modularized in React

---

## 🛠️ Tech Stack

- **Frontend:** React, Bootstrap 5, Chart.js  
- **Backend:** FastAPI (Python), RESTful endpoints  
- **Build Tools:** npm, axios for API calls  
- **Version Control:** Git + GitHub branches (`math-mine-react`)

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/math-mine-react.git
   cd math-mine-react
2. Install dependencies:
   npm install
3. Run the development server:
   npm start
4. Make sure the FastAPI backend is running at http://localhost:8000.

📊 Demo Flow
- Select a problem type.
- Enter counts for each problem category.
- Click Excavate to generate files.
- Use Show Histogram button to visualize distribution.
- Download worksheet, answers, and answer key.

🔎 Recruiter Note
This React frontend demonstrates:
- Translating vanilla JS logic into modular React components.
- State management with hooks (useState, useEffect).
- Integration with backend APIs.
- Responsive UI/UX polish with Bootstrap.
- Dynamic data visualization with Chart.js.

📂 Project Structure
src/
 └── components/
      ├── DynamicProblemForm.js   # Main form logic
      └── Histogram.js            # Chart.js wrapper



📝 License
MIT License. Free to use and adapt.

