from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.experience import ExperienceSchema
from app.api.v1.controllers.experience_controller import (
    get_all_experience_controller,
    get_experience_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[ExperienceSchema])
def get_all_experience(db: Session = Depends(get_db)):
    return get_all_experience_controller(db)


@router.get("/{uuid}", response_model=ExperienceSchema)
def get_experience_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_experience_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
