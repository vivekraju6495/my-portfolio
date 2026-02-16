from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.skill_controller import (
    get_all_skills_controller,
    get_skills_by_category_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel

router = APIRouter()

@router.get("/", response_model=ResponseModel)  
def get_all_skills(db: Session = Depends(get_db)):
    data = get_all_skills_controller(db)
    return success_response("Skills fetched successfully", data)

@router.get("/category/{category}", response_model=ResponseModel) 
def get_skills_by_category(category: str, db: Session = Depends(get_db)):
    try:
        skills = get_skills_by_category_controller(db, category)
        if not skills:
            return success_response("No skills found for this category", data=[], status=200)
        return success_response("Skills fetched successfully", skills)
    except Exception as e:
        return error_response(str(e), status=400)
