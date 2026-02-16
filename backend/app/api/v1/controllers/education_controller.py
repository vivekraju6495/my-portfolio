from sqlalchemy.orm import Session
from app.schemas.educations import EducationSchema
from app.services.education_service import EducationService

def get_all_education_controller(db: Session):
    educations = EducationService.get_all(db)
    return [EducationSchema.model_validate(edu) for edu in educations]


def get_education_by_uuid_controller(db: Session, uuid: str):
    edu = EducationService.get_by_uuid(db, uuid)
    if not edu:
        raise Exception("Education not found")
    return EducationSchema.model_validate(edu)
