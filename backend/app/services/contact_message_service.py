from sqlalchemy.orm import Session
from app.models.contact_messages import ContactMessage

class ContactMessageService:

    @staticmethod
    def get_all(db: Session):
        return db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(ContactMessage).filter(ContactMessage.uuid == uuid).first()
