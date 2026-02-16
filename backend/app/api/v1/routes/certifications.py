from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.certifications import CertificationSchema
from app.api.v1.controllers.certification_controller import (
    get_all_certifications_controller,
    get_certification_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[CertificationSchema])
def get_all_certifications(db: Session = Depends(get_db)):
    return get_all_certifications_controller(db)


@router.get("/{uuid}", response_model=CertificationSchema)
def get_certification_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_certification_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
