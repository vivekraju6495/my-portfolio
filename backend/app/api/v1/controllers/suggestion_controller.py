from sqlalchemy.orm import Session
from app.schemas.suggestions import SuggestionSchema
from app.services.suggestion_service import SuggestionService

def get_all_suggestions_controller(db: Session):
    suggestions = SuggestionService.get_all(db)
    return [SuggestionSchema.model_validate(s) for s in suggestions]


def get_suggestion_by_uuid_controller(db: Session, uuid: str):
    suggestion = SuggestionService.get_by_uuid(db, uuid)
    if not suggestion:
        raise Exception("Suggestion not found")
    return SuggestionSchema.model_validate(suggestion)
