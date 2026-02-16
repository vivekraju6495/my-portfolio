from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.certification_controller import (
    get_all_certifications_controller,
    get_certification_by_uuid_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel


router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_all_certifications(db: Session = Depends(get_db)):
    data = get_all_certifications_controller(db)
    return success_response("Certifications fetched successfully", data)


@router.get("/{uuid}", response_model=ResponseModel)
def get_certification_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        data = get_certification_by_uuid_controller(db, uuid)
        return success_response("Certification fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)

