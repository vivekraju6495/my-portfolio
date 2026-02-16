from datetime import datetime
from sqlalchemy.orm import Session
from app.models.contact_messages import ContactMessage
from app.schemas.contact_messages import ContactMessageCreateSchema

class ContactMessageService:

    @staticmethod
    def get_all(db: Session):
        return db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(ContactMessage).filter(ContactMessage.uuid == uuid).first()

    @staticmethod
    def create(db: Session, payload: ContactMessageCreateSchema):
        new_message = ContactMessage(
            name=payload.name,
            email=payload.email,
            message=payload.message,
            created_at=datetime.utcnow()
        )
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
