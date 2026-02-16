from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.contact_messages import ContactMessageSchema
from app.api.v1.controllers.contact_message_controller import (
    get_all_contact_messages_controller,
    get_contact_message_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[ContactMessageSchema])
def get_all_contact_messages(db: Session = Depends(get_db)):
    return get_all_contact_messages_controller(db)


@router.get("/{uuid}", response_model=ContactMessageSchema)
def get_contact_message_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_contact_message_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
