from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.contact_message_controller import (
    get_all_contact_messages_controller,
    get_contact_message_by_uuid_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel

router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_all_contact_messages(db: Session = Depends(get_db)):
    data = get_all_contact_messages_controller(db)
    return success_response("Contact messages fetched successfully", data)

@router.get("/{uuid}", response_model=ResponseModel)
def get_contact_message_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        data = get_contact_message_by_uuid_controller(db, uuid)
        
    except Exception as e:
         return error_response(str(e), status=404)
