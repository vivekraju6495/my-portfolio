from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.contact_message_controller import (
    create_contact_message_controller,
    get_all_contact_messages_controller,
    get_contact_message_by_uuid_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel
from app.schemas.contact_messages import ContactMessageCreateSchema
from fastapi_limiter.depends import RateLimiter
from app.core.settings import settings

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

@router.post("/", response_model=ResponseModel, dependencies=[
        Depends(
            RateLimiter(
                times=settings.RATE_LIMIT_CONTACT_TIMES,
                seconds=settings.RATE_LIMIT_CONTACT_SECONDS
            )
        )
    ]
)
def create_contact_message(payload: ContactMessageCreateSchema, db: Session = Depends(get_db)):
    try:
        data = create_contact_message_controller(db, payload)
        return success_response("Message submitted successfully", data)
    except Exception as e:
        return error_response(str(e), status=400)
