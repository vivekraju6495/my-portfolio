from sqlalchemy.orm import Session
from app.schemas.skills import SkillSchema
from app.services.skill_service import SkillService

def get_all_skills_controller(db: Session):
    skills = SkillService.get_all(db)
    return [SkillSchema.model_validate(skill) for skill in skills]


def get_skills_by_category_controller(db: Session, category: str):
    skills = SkillService.get_by_category(db, category)
    return [SkillSchema.model_validate(skill) for skill in skills]
