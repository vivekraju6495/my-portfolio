from sqlalchemy.orm import Session
from app.schemas.experience import ExperienceSchema
from app.services.experience_service import ExperienceService

def get_all_experience_controller(db: Session):
    experiences = ExperienceService.get_all(db)
    return [ExperienceSchema.model_validate(exp) for exp in experiences]


def get_experience_by_uuid_controller(db: Session, uuid: str):
    exp = ExperienceService.get_by_uuid(db, uuid)
    if not exp:
        raise Exception("Experience not found")
    return ExperienceSchema.model_validate(exp)
