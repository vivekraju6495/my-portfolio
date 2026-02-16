from sqlalchemy.orm import Session
from app.schemas.certifications import CertificationSchema
from app.services.certification_service import CertificationService

def get_all_certifications_controller(db: Session):
    certifications = CertificationService.get_all(db)
    return [CertificationSchema.model_validate(c) for c in certifications]


def get_certification_by_uuid_controller(db: Session, uuid: str):
    cert = CertificationService.get_by_uuid(db, uuid)
    if not cert:
        raise Exception("Certification not found")
    return CertificationSchema.model_validate(cert)
