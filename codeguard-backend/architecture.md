# Backend Architecture – Hybrid Multi-Language Code Review System

## Architecture Diagram

```mermaid
flowchart TD
    subgraph ClientLayer [Client Applications]
        Client["Client\n(Postman / CLI / Web Tool)"]
    end

    subgraph API [FastAPI API Layer]
        Router["FastAPI REST API\n(JSON Body with Code)"]
        Validator["Request Validation\n(Pydantic)"]
    end

    subgraph Core [Core Services]
        LangDetect["Language Detection Module\n(Syntax & Keyword Heuristics)"]
        
        subgraph StaticAnalysis [Static Analysis Layer]
            direction TB
            PyAST["Python Analyzer\n(AST-Based)"]
            JSEslint["JavaScript Analyzer\n(ESLint-Based)"]
        end
        
        subgraph SemanticAnalysis [LLM Semantic Engine]
            direction TB
            Ollama["Ollama Runtime\n(DeepSeek-Coder / CodeLlama)"]
        end
        
        Aggregator["Result Aggregator\n+ Weighted Scoring Engine"]
    end

    subgraph Data [Data Persistence]
        DB[("SQLite Database\nStores:\n- Analysis Reports\n- Issue Details\n- Severity Breakdown\n- Timestamps")]
    end

    Client -- "POST /analyze\nRaw Text Code" --> Router
    Router --> Validator
    Validator --> LangDetect
    
    LangDetect -- "Python Code" --> PyAST
    LangDetect -- "JavaScript Code" --> JSEslint
    
    PyAST --> Aggregator
    JSEslint --> Aggregator
    
    LangDetect -. "Raw Code" .-> Ollama
    Ollama --> Aggregator
    
    Aggregator --> DB
    Aggregator -- "JSON Response" --> Client

    %% Styling
    classDef client fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef api fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef core fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px;
    classDef analysis fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    classDef llm fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef db fill:#ffccbc,stroke:#e64a19,stroke-width:2px;

    class Client client;
    class Router,Validator api;
    class LangDetect,Aggregator core;
    class PyAST,JSEslint analysis;
    class Ollama llm;
    class DB db;
```

---

## API Contract

This system is completely independent of the filesystem and file uploads. It operates directly on raw code represented as a simple JSON string value.

### Request
```http
POST /analyze
Content-Type: application/json

{
  "code": "def example(): pass"
}
```

### Response
```json
{
  "language": "python",
  "score": 82,
  "severity_breakdown": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
  },
  "static_issues": [],
  "ai_issues": [],
  "summary": "The code appears clean and functional."
}
```
