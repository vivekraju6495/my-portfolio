from sqlalchemy.orm import Session
from app.schemas.projects import ProjectSchema
from app.services.project_service import ProjectService

def get_all_projects_controller(db: Session):
    projects = ProjectService.get_all(db)
    return [ProjectSchema.model_validate(p) for p in projects]


def get_project_by_uuid_controller(db: Session, uuid: str):
    project = ProjectService.get_by_uuid(db, uuid)
    if not project:
        raise Exception("Project not found")
    return ProjectSchema.model_validate(project)
