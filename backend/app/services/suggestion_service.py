from datetime import datetime
from sqlalchemy.orm import Session
from app.models.suggestions import Suggestion
from app.schemas.suggestions import SuggestionCreateSchema
class SuggestionService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Suggestion).order_by(Suggestion.created_at.desc()).all()

    @staticmethod
    def get_by_uuid(db: Session, uuid: str):
        return db.query(Suggestion).filter(Suggestion.uuid == uuid).first()

    @staticmethod
    def create(db: Session, payload: SuggestionCreateSchema):
        new_suggestion = Suggestion(
            name=payload.name,
            email=payload.email,
            suggestion=payload.suggestion,
            created_at=datetime.utcnow()
        )
        db.add(new_suggestion)
        db.commit()
        db.refresh(new_suggestion)
        return new_suggestion

