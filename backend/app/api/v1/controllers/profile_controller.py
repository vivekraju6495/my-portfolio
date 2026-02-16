from sqlalchemy.orm import Session
from app.schemas.profile import ProfileResponse
from app.services.profile_service import ProfileService

def get_profile_controller(db: Session):
    profile = ProfileService.get_profile(db)

    if not profile:
        raise Exception("Profile not found")

    return ProfileResponse.model_validate(profile)
