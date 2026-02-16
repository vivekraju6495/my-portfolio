from sqlalchemy.orm import Session
from app.schemas.contact_messages import ContactMessageCreateSchema, ContactMessageSchema
from app.services.contact_message_service import ContactMessageService

def get_all_contact_messages_controller(db: Session):
    messages = ContactMessageService.get_all(db)
    return [ContactMessageSchema.model_validate(m) for m in messages]


def get_contact_message_by_uuid_controller(db: Session, uuid: str):
    msg = ContactMessageService.get_by_uuid(db, uuid)
    if not msg:
        raise Exception("Contact message not found")
    return ContactMessageSchema.model_validate(msg)

def create_contact_message_controller(db: Session, payload: ContactMessageCreateSchema):
    message = ContactMessageService.create(db, payload)
    return ContactMessageSchema.model_validate(message)
