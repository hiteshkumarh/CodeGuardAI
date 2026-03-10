# 🛡️ CodeGuard AI

CodeGuard AI is an intelligent hybrid code review system that combines **static code analysis** with **LLM-based semantic analysis** to automatically detect security vulnerabilities, complexity issues, and code quality problems in Python and JavaScript.

The system integrates **FastAPI**, **Python AST**, **ESLint**, and **Groq LLM** to perform automated code reviews and generate a health score for submitted code.

---

# 🚀 Features

• Hybrid code analysis using **static analyzers + AI models**
• Python code inspection using **AST (Abstract Syntax Tree)**
• JavaScript analysis using **ESLint**
• LLM-powered semantic review using **Groq (Llama 3)**
• Automated **code quality scoring system**
• GitHub webhook support for **automated PR code reviews**
• Modular backend architecture using **FastAPI**
• SQLite database for **analysis report storage**

---

# 🏗️ Project Architecture

The system follows a layered architecture:

```
Client / GitHub Webhook
          │
          ▼
      FastAPI API Layer
          │
          ▼
     Core Analysis Engine
          │
          ▼
 ┌─────────────────────────────┐
 │ Static Analysis Layer       │
 │ • Python AST Analyzer       │
 │ • JavaScript ESLint Engine  │
 └─────────────────────────────┘
          │
          ▼
     LLM Semantic Analysis
          │
          ▼
      Aggregator & Scoring
          │
          ▼
      SQLite Database
```

---

# 📂 Project Structure

```
CodeGuardAI
│
├── codeguard-backend
│   │
│   ├── requirements.txt
│   ├── run_and_save.py
│   ├── run_validation.py
│   │
│   ├── app
│   │   ├── api
│   │   │   ├── dependencies.py
│   │   │   ├── routes.py
│   │   │   └── webhook.py
│   │   │
│   │   ├── core
│   │   │   └── analyze.py
│   │   │
│   │   ├── models
│   │   │   └── report_model.py
│   │   │
│   │   ├── services
│   │   │   ├── aggregator.py
│   │   │   ├── comment_service.py
│   │   │   ├── external_service.py
│   │   │   ├── github_service.py
│   │   │   ├── llm_service.py
│   │   │   └── parser_service.py
│   │   │
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   └── js-analyzer
│       ├── analyze.js
│       ├── eslint.config.js
│       └── package.json
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/hiteshkumarh/CodeGuardAI.git
cd CodeGuardAI/codeguard-backend
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install JavaScript analyzer dependencies:

```
cd js-analyzer
npm install
cd ..
```

---

# ▶️ Running the Backend

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Run Validation Tests

Run sample analysis tests:

```
python run_validation.py
```

This script sends test code snippets to the API and displays analysis results.

---

# 🔐 Environment Variables

Create a `.env` file inside `codeguard-backend`.

Example:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# 📊 Example API Request

Endpoint:

```
POST /analyze
```

Example request:

```
{
  "code": "def add(a, b): return a + b"
}
```

Example response:

```
{
  "score": 85,
  "language": "python",
  "issues": [
    {
      "severity": "low",
      "message": "Missing function docstring"
    }
  ]
}
```

---

# 🛠️ Tech Stack

Backend
• Python
• FastAPI
• SQLAlchemy

Static Analysis
• Python AST
• ESLint

AI Integration
• Groq LLM (Llama 3)

Database
• SQLite

Other Tools
• GitHub Webhooks
• REST API

---

# 📌 Future Improvements

• Support more programming languages
• Add real-time dashboard for code quality metrics
• Implement asynchronous analysis pipeline
• Improve LLM prompt engineering for deeper insights

---

# 👨‍💻 Author

Hithesh Kumar
Computer Science Engineer
Interested in **AI Engineering, Backend Systems, and Code Intelligence Tools**

GitHub:
[https://github.com/hiteshkumarh](https://github.com/hiteshkumarh)

