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
User Request
     │
     ▼
FastAPI API Endpoint (/analyze)
     │
     ▼
Language Detection
     │
     ▼
Static Analysis
 (AST / ESLint)
     │
     ▼
LLM Semantic Analysis
     │
     ▼
Issue Aggregation
     │
     ▼
Code Quality Scoring
     │
     ▼
Database Storage
     │
     ▼
JSON Response to Client
```

---

# 📂 Project Structure

```
CodeGuardAI
│
├── codeguard-backend                       (Main backend application folder)
│   │
│   ├── requirements.txt                    (Lists all Python dependencies needed to run the backend)
│   ├── run_and_save.py                     (Script to run code analysis and save results into the database)
│   ├── run_validation.py                   (Testing script that sends sample code to the API to verify system behavior)
│   │
│   ├── app                                 (Core FastAPI backend application)
│   │   │
│   │   ├── api                             (Handles API endpoints and request routing)
│   │   │   ├── dependencies.py              (Defines shared FastAPI dependencies such as DB session injection)
│   │   │   ├── routes.py                    (Main REST endpoints like /analyze and /reports)
│   │   │   └── webhook.py                   (GitHub webhook handler for automatic code review on pull requests)
│   │   │
│   │   ├── core                            (Core analysis orchestration logic)
│   │   │   └── analyze.py                   (Coordinates static analysis + LLM analysis and returns combined results)
│   │   │
│   │   ├── models                          (Database ORM models)
│   │   │   └── report_model.py              (SQLAlchemy model representing stored analysis reports)
│   │   │
│   │   ├── services                        (Business logic layer)
│   │   │   ├── aggregator.py                (Combines results from static analyzers and LLM analysis)
│   │   │   ├── comment_service.py           (Formats and posts analysis results as GitHub PR comments)
│   │   │   ├── external_service.py          (Handles calls to external APIs such as Groq LLM)
│   │   │   ├── github_service.py            (Interacts with GitHub API to fetch PR code and post comments)
│   │   │   ├── llm_service.py               (Handles prompt creation and communication with the LLM)
│   │   │   └── parser_service.py            (Processes and structures code analysis results)
│   │   │
│   │   ├── config.py                       (Central configuration management using environment variables)
│   │   ├── database.py                     (Database connection setup and session management)
│   │   └── main.py                         (FastAPI application entry point and server initialization)
│   │
│   └── js-analyzer                         (Node.js microservice for JavaScript static analysis)
│       ├── analyze.js                      (Runs ESLint to analyze JavaScript code)
│       ├── eslint.config.js                (ESLint configuration defining rules and checks)
│       └── package.json                    (Node.js dependencies and project configuration)
│
├── README.md                               (Project documentation including setup instructions)
└── .gitignore                              (Specifies files that Git should ignore such as .env, db files, and caches)
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

