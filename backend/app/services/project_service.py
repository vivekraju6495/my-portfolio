from sqlalchemy.orm import Session
from app.models.projects import Project

class ProjectService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Project).filter(Project.uuid == uuid).first()
