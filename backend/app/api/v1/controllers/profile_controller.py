from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileResponse

def get_profile_service(db: Session):
    profile = db.query(Profile).first()

    if not profile:
        raise Exception("Profile not found")

    return ProfileResponse.model_validate(profile)

