from sqlalchemy.orm import Session
from app.models.educations import Education

class EducationService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Education).order_by(Education.start_date.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Education).filter(Education.uuid == uuid).first()
