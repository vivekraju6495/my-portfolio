from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.educations import EducationSchema
from app.api.v1.controllers.education_controller import (
    get_all_education_controller,
    get_education_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[EducationSchema])
def get_all_education(db: Session = Depends(get_db)):
    return get_all_education_controller(db)


@router.get("/{uuid}", response_model=EducationSchema)
def get_education_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_education_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
