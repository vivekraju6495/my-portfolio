from sqlalchemy.orm import Session
from app.models.certifications import Certification

class CertificationService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Certification).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Certification).filter(Certification.uuid == uuid).first()
