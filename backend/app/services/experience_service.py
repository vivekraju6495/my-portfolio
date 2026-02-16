from sqlalchemy.orm import Session
from app.models.experience import Experience

class ExperienceService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Experience).order_by(Experience.start_date.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Experience).filter(Experience.uuid == uuid).first()
