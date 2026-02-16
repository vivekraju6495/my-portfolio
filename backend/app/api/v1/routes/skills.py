from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.skills import SkillSchema
from app.api.v1.controllers.skill_controller import (
    get_all_skills_controller,
    get_skills_by_category_controller
)

router = APIRouter()

@router.get("/", response_model=list[SkillSchema])
def get_all_skills(db: Session = Depends(get_db)):
    return get_all_skills_controller(db)


@router.get("/category/{category}", response_model=list[SkillSchema])
def get_skills_by_category(category: str, db: Session = Depends(get_db)):
    skills = get_skills_by_category_controller(db, category)
    if not skills:
        raise HTTPException(status_code=404, detail="No skills found for this category")
    return skills
