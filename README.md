# 🛡️ CodeGuard AI

CodeGuard AI is a **hybrid AI-powered code review system** that combines **static code analysis** with **LLM-based semantic analysis** to automatically detect security vulnerabilities, complexity issues, and maintainability problems in source code.

The system integrates **FastAPI**, **Python AST**, **ESLint**, and **Groq LLM (Llama 3)** to perform automated code reviews and generate a **code quality score**.

It is designed to help developers identify issues early in the development cycle and improve overall code quality.

---

# 📌 Problem Statement

Manual code reviews are time-consuming and often inconsistent. Developers may miss critical issues such as:

• Security vulnerabilities

• High algorithmic complexity

• Poor coding practices

• Maintainability issues

• Hidden logical bugs

Traditional static analyzers detect structural issues but **cannot understand code intent or deeper logical problems**.

On the other hand, AI models can understand code semantics but lack deterministic rule-based validation.

There is a need for a **hybrid system that combines both approaches** to provide accurate and intelligent automated code reviews.

---

# 🎯 Solution

CodeGuard AI addresses this problem by combining:

1. **Static Analysis Engines**

   * Python AST
   * ESLint

2. **AI-Based Semantic Analysis**

   * Groq LLM (Llama 3)

The system analyzes source code using both methods and produces:

• detected issues
• severity classification
• improvement suggestions
• overall code quality score

This hybrid approach provides **both rule-based accuracy and AI reasoning**.

---

# 🚀 Features

• Hybrid code analysis using **static analyzers + AI models**

• Python code inspection using **AST (Abstract Syntax Tree)**

• JavaScript analysis using **ESLint**

• LLM-powered semantic code review using **Groq (Llama 3)**

• Automated **code quality scoring system**

• REST API built with **FastAPI**

• SQLite database for **analysis report storage**

• Modular and scalable backend architecture

• GitHub webhook support for automated **pull request code reviews**

---

# 🏗️ System Architecture

The system follows a **layered architecture** that separates API handling, analysis logic, AI integration, and data storage.

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

# 🔄 System Workflow

1️⃣ **User Request**

A developer sends a code snippet to the API or triggers analysis through a GitHub webhook.

2️⃣ **Language Detection**

The system detects whether the code is written in **Python or JavaScript**.

3️⃣ **Static Code Analysis**

The code is analyzed using rule-based analyzers.

Python:

* AST parsing
* complexity detection
* dangerous function detection (`eval`, `exec`)

JavaScript:

* ESLint rules
* syntax validation
* scope and style checks

4️⃣ **LLM Semantic Analysis**

The code is sent to **Groq Llama-3 model** to detect:

• logical bugs
• security risks
• maintainability issues
• inefficient algorithms

5️⃣ **Issue Aggregation**

Results from both analyzers are merged and duplicate issues are removed.

6️⃣ **Code Quality Scoring**

The system calculates a score starting from **100**.

| Severity | Penalty |
| -------- | ------- |
| Critical | -30     |
| High     | -20     |
| Medium   | -10     |
| Low      | -5      |

7️⃣ **Database Storage**

Analysis results are stored in **SQLite** using SQLAlchemy.

8️⃣ **Response Delivery**

The API returns a structured JSON response containing:

• detected issues
• severity breakdown
• code quality score
• LLM summary

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

Install Python dependencies:

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

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Run Validation Tests

Run sample analysis tests:

```
python run_validation.py
```

This script sends test code snippets to the API and prints analysis results.

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
  "language": "python",
  "score": 85,
  "issues": [
    {
      "severity": "low",
      "message": "Missing function documentation"
    }
  ]
}
```

---

# 🛠️ Tech Stack

1.Backend

  • Python
  • FastAPI
  • SQLAlchemy

2.Static Analysis

  • Python AST
  • ESLint

3.AI Integration

  • Groq LLM (Llama 3)

4.Database

  • SQLite

5.Other Tools

  • GitHub Webhooks
  • REST API

---

# 📌 Future Improvements

• Support additional programming languages

• Implement asynchronous analysis pipeline

• Add dashboard for code quality metrics

• Improve LLM prompt engineering

• CI/CD integration for automated code reviews

---

# 👨‍💻 Author

**Hithesh Kumar**

GitHub
[https://github.com/hiteshkumarh](https://github.com/hiteshkumarh)





