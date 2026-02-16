from sqlalchemy.orm import Session
from app.models.suggestions import Suggestion

class SuggestionService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Suggestion).order_by(Suggestion.created_at.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Suggestion).filter(Suggestion.uuid == uuid).first()
