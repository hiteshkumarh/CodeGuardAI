from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class AnalyzeRequest(BaseModel):
    code: str

class Issue(BaseModel):
    type: str
    message: str
    severity: str  # critical, high, medium, low
    line: Optional[int] = None

class AnalyzeResponse(BaseModel):
    language: str
    score: float
    severity_breakdown: Dict[str, int]
    static_issues: List[Issue]
    ai_issues: List[Issue]
    summary: str
    llm_status: str = "success"
