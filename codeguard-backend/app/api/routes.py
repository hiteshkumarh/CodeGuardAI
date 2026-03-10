import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.report_model import Report
from app.schemas.request_response import AnalyzeRequest, AnalyzeResponse, Issue
from app.utils.language_detector import detect_language
from app.analyzers.python_analyzer import PythonAnalyzer
from app.analyzers.js_analyzer import JSAnalyzer
from app.llm.llm_engine import LLMEngine
from app.services.scoring import calculate_score, calculate_severity_breakdown
from app.services.aggregator import aggregate_issues

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_code(request: AnalyzeRequest, db: Session = Depends(get_db)):
    lang = detect_language(request.code)
    
    if lang == "unknown":
        raise HTTPException(status_code=400, detail="Unsupported or unknown language. Please provide Python or JavaScript code.")
        
    # 1. Static Analysis
    static_issues = []
    if lang == "python":
        analyzer = PythonAnalyzer()
        static_issues = analyzer.analyze(request.code)
    elif lang == "javascript":
        analyzer = JSAnalyzer()
        static_issues = analyzer.analyze(request.code)
        
    # 2. LLM Analysis
    llm = LLMEngine()
    llm_issues, summary, llm_status = llm.analyze(request.code, lang)
    
    # 3. Aggregation and Scoring
    all_issues = aggregate_issues(static_issues, llm_issues)
    score = calculate_score(all_issues)
    severity_breakdown = calculate_severity_breakdown(all_issues)
    
    # 4. Save to Database
    issues_dict = {
        "static_issues": [issue.dict() if hasattr(issue, 'dict') else issue.model_dump() for issue in static_issues],
        "ai_issues": [issue.dict() if hasattr(issue, 'dict') else issue.model_dump() for issue in llm_issues],
        "summary": summary,
        "llm_status": llm_status
    }
    
    db_report = Report(
        language=lang,
        score=score,
        severity_breakdown=json.dumps(severity_breakdown),
        issues_json=json.dumps(issues_dict)
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    
    # 5. Return Response
    return AnalyzeResponse(
        language=lang,
        score=score,
        severity_breakdown=severity_breakdown,
        static_issues=static_issues,
        ai_issues=llm_issues,
        summary=summary,
        llm_status=llm_status
    )

@router.get("/reports")
def get_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = db.query(Report).order_by(Report.timestamp.desc()).offset(skip).limit(limit).all()
    
    result = []
    for r in reports:
        result.append({
            "id": r.id,
            "language": r.language,
            "score": r.score,
            "timestamp": r.timestamp,
            "severity_breakdown": json.loads(r.severity_breakdown) if r.severity_breakdown else {}
        })
    return result

@router.get("/report/{report_id}")
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
        
    issues_data = json.loads(report.issues_json) if report.issues_json else {}
    
    return {
        "id": report.id,
        "language": report.language,
        "score": report.score,
        "timestamp": report.timestamp,
        "severity_breakdown": json.loads(report.severity_breakdown),
        "static_issues": issues_data.get("static_issues", []),
        "ai_issues": issues_data.get("ai_issues", []),
        "summary": issues_data.get("summary", ""),
        "llm_status": issues_data.get("llm_status", "unknown")
    }
