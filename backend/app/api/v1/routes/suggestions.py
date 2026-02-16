from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.suggestions import SuggestionSchema
from app.api.v1.controllers.suggestion_controller import (
    get_all_suggestions_controller,
    get_suggestion_by_uuid_controller
)

router = APIRouter()

@router.get("/", response_model=list[SuggestionSchema])
def get_all_suggestions(db: Session = Depends(get_db)):
    return get_all_suggestions_controller(db)


@router.get("/{uuid}", response_model=SuggestionSchema)
def get_suggestion_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        return get_suggestion_by_uuid_controller(db, uuid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
