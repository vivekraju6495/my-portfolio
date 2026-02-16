from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.projects import ProjectSchema
from app.api.v1.controllers.project_controller import (
    get_all_projects_controller,
    get_project_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[ProjectSchema])
def get_all_projects(db: Session = Depends(get_db)):
    return get_all_projects_controller(db)


@router.get("/{uuid}", response_model=ProjectSchema)
def get_project_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_project_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
