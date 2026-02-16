from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.projects import ProjectSchema
from app.api.v1.controllers.project_controller import (
    get_all_projects_controller,
    get_project_by_uuid_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel

router = APIRouter()

@router.get("/", response_model=list[ProjectSchema])
def get_all_projects(db: Session = Depends(get_db)):
    data = get_all_projects_controller(db)
    return success_response("Projects fetched successfully", data)

@router.get("/{uuid}", response_model=ProjectSchema)
def get_project_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        data = get_project_by_uuid_controller(db, uuid)
        return success_response("Projects fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)
