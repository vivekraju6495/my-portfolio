from sqlalchemy.orm import Session
from app.models.profile import Profile

class ProfileService:

    @staticmethod
    def get_profile(db: Session):
        return db.query(Profile).first()