from sqlalchemy.orm import Session
from app.models.skills import Skill

class SkillService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Skill).all()

    @staticmethod
    def get_by_category(db: Session, category: str):
        return (
            db.query(Skill)
            .filter(Skill.category.ilike(category))
            .all()
        )
