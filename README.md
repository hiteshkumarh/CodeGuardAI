Your README is already good. To make it look **startup-level and more impressive to recruiters**, add two things:

1️⃣ **Project Demo section**
2️⃣ **API Endpoint Documentation section**

Below is the **FULL upgraded README** with those included. You can **copy-paste directly**.

---

# 🛡️ CodeGuard AI

CodeGuard AI is a **hybrid AI-powered code review system** that combines **static code analysis** with **LLM-based semantic analysis** to automatically detect security vulnerabilities, complexity issues, and maintainability problems in source code.

The system integrates **FastAPI**, **Python AST**, **ESLint**, and **Groq LLM (Llama 3)** to perform automated code reviews and generate a **code quality score**.

It is designed to help developers detect issues early in the development cycle and improve overall code quality.

---

# 📌 Problem Statement

Manual code reviews are essential for maintaining high-quality software, but they have several limitations:

• Time-consuming for development teams
• Inconsistent review quality between developers
• Hard to detect hidden logical issues
• Security vulnerabilities can be overlooked
• Performance issues such as high algorithmic complexity may go unnoticed

Traditional **static analysis tools** detect structural issues but cannot understand **code intent or deeper logic**.

AI models can understand semantics but lack deterministic rule-based validation.

Therefore, there is a need for a **hybrid system combining rule-based analysis with AI reasoning**.

---

# 🎯 Solution

CodeGuard AI solves this by combining:

### Static Code Analysis

Rule-based analysis using:

• **Python AST (Abstract Syntax Tree)**
• **ESLint for JavaScript**

This detects:

• syntax errors
• unsafe functions (`eval`)
• nested loop complexity
• code style violations

---

### AI Semantic Analysis

Code is also analyzed using **Groq LLM (Llama 3)** which identifies:

• logical bugs
• security vulnerabilities
• maintainability problems
• inefficient algorithms
• readability issues

---

### Final Output

The system generates:

• detected issues
• severity classification
• improvement suggestions
• overall code quality score

This hybrid approach provides both **deterministic accuracy and AI reasoning**.

---

# 🚀 Features

• Hybrid analysis using **static analyzers + AI models**

• Python code inspection using **AST (Abstract Syntax Tree)**

• JavaScript analysis using **ESLint**

• LLM-powered semantic analysis using **Groq (Llama 3)**

• Automated **code quality scoring system**

• REST API built with **FastAPI**

• SQLite database for **analysis report storage**

• Modular backend architecture

• GitHub webhook support for automated **pull request code reviews**

---

# 🎬 Project Demo

Example request:

```
POST /analyze
```

Input code:

```
def add(a,b):
    return a+b
```

Example API response:

```
{
  "language": "python",
  "score": 90,
  "severity_breakdown": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 2
  },
  "static_issues": [],
  "ai_issues": [
    {
      "type": "Code Style",
      "message": "Function name should use snake_case",
      "severity": "low"
    }
  ],
  "summary": "The code works correctly but has minor style issues."
}
```

---

# 🏗️ System Architecture

```
User Request / GitHub PR
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
 │  • Python AST Analyzer      │
 │  • ESLint JavaScript Engine │
 └─────────────────────────────┘
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
   JSON Response / GitHub Comment
```

---

# 🔄 End-to-End Analysis Pipeline

```
Client Request
      ↓
FastAPI Endpoint
      ↓
Language Detection
      ↓
Static Analysis
 (Python AST / ESLint)
      ↓
LLM Semantic Analysis
      ↓
Issue Aggregation
      ↓
Score Calculation
      ↓
JSON Response
```

---

# 📡 API Endpoints

### Analyze Code

```
POST /analyze
```

Request body:

```
{
  "code": "def add(a,b): return a+b"
}
```

Returns analysis result including issues and score.

---

### Get Reports

```
GET /reports
```

Returns stored analysis reports from the database.

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

Clone the repository

```
git clone https://github.com/hiteshkumarh/CodeGuardAI.git
cd CodeGuardAI/codeguard-backend
```

Create virtual environment

```
python -m venv venv
```

Activate environment

```
venv\Scripts\activate
```

Install Python dependencies

```
pip install -r requirements.txt
```

Install JavaScript analyzer

```
cd js-analyzer
npm install
cd ..
```

---

# ▶️ Running the Backend

Start FastAPI server

```
uvicorn app.main:app --reload
```

Server will run at

```
http://127.0.0.1:8000
```

API documentation

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Run Validation Tests

```
python run_validation.py
```

This script sends test code snippets to the API and prints analysis results.

---

# 🔐 Environment Variables

Create `.env` file inside `codeguard-backend`.

Example:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# 🛠️ Tech Stack

### Backend

• Python
• FastAPI
• SQLAlchemy

### Static Analysis

• Python AST
• ESLint

### AI Integration

• Groq LLM (Llama 3)

### Database

• SQLite

### Other Tools

• GitHub Webhooks
• REST API

---

# ⭐ Why This Project Matters

Modern development teams rely heavily on automated code review tools to maintain code quality at scale.

CodeGuard AI demonstrates how **traditional static analysis can be combined with LLM capabilities** to build intelligent developer tools.

This project showcases:

• backend architecture design
• AI integration in developer tools
• static code analysis systems
• REST API development
• automated code scoring

---

# 📌 Future Improvements

• Support additional programming languages

• Implement asynchronous analysis pipeline

• Add dashboard for code quality metrics

• CI/CD integration for automated PR reviews

---

# 👨‍💻 Author

**Hithesh Kumar**

GitHub
[https://github.com/hiteshkumarh](https://github.com/hiteshkumarh)



