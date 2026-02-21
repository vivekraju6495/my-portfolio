from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd
import numpy as np
from app.core.database import get_db
from app.api.v1.controllers.analytics_controller import (
    get_analytics_controller,
    increment_visitors_controller,
    increment_resume_downloads_controller,
    increment_page_views_controller,
    increment_api_hits_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel
from app.models.skills import Skill

router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_analytics(db: Session = Depends(get_db)):
    try:
        data = get_analytics_controller(db)
        return success_response("Analytics fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)


@router.post("/increment/visitors", response_model=ResponseModel)
def increment_visitors(db: Session = Depends(get_db)):
    try:
        data = increment_visitors_controller(db)
        return success_response("Visitor count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/resume-downloads", response_model=ResponseModel)
def increment_resume_downloads(db: Session = Depends(get_db)):
    try:
        data = increment_resume_downloads_controller(db)
        return success_response("Resume download count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/page-views", response_model=ResponseModel)
def increment_page_views(db: Session = Depends(get_db)):
    try:
        data = increment_page_views_controller(db)
        return success_response("Page view count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/api-hits", response_model=ResponseModel)
def increment_api_hits(db: Session = Depends(get_db)):
    try:
        data = increment_api_hits_controller(db)
        return success_response("API hit count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)

@router.post("/insights")
def resume_insights(text: str):
    # Split into words
    words = text.split()
    df = pd.DataFrame({"word": words})

    # Frequency of top words
    top_words = df["word"].value_counts().head(10).to_dict()

    # Average word length
    avg_word_length = float(np.mean([len(w) for w in words])) if words else 0

    # Sentence count
    sentences = [s for s in text.split(".") if s.strip()]
    sentence_count = len(sentences)

    return {
        "word_count": len(words),
        "sentence_count": sentence_count,
        "top_words": top_words,
        "avg_word_length": avg_word_length,
    }

@router.get("/skills/analyze")
def analyze_skills(db: Session = Depends(get_db)):

    # Fetch skill name + category from DB
    skill_records = db.query(Skill.skill_name, Skill.category).all()

    if not skill_records:
        return {
            "total_skills": 0,
            "category_breakdown": {}
        }

    # Convert to DataFrame
    df = pd.DataFrame(skill_records, columns=["skill", "category"])

    # Group and count by category
    counts = df.groupby("category").size().to_dict()

    return {
        "total_skills": len(df),
        "category_breakdown": counts,
        "categories": df["category"].unique().tolist()
    }