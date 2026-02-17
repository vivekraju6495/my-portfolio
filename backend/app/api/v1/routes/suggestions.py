from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.controllers.suggestion_controller import (
    create_suggestion_controller,
    get_all_suggestions_controller,
    get_suggestion_by_uuid_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel
from app.schemas.suggestions import SuggestionCreateSchema

router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_all_suggestions(db: Session = Depends(get_db)):
    data = get_all_suggestions_controller(db)
    return success_response("Suggestions fetched successfully", data)

@router.get("/{uuid}", response_model=ResponseModel)
def get_suggestion_by_uuid(uuid: str, db: Session = Depends(get_db)):
    try:
        data = get_suggestion_by_uuid_controller(db, uuid)
        return success_response("Suggestions fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)

@router.post("/", response_model=ResponseModel)
def create_suggestion(payload: SuggestionCreateSchema, db: Session = Depends(get_db)):
    try:
        data = create_suggestion_controller(db, payload)
        return success_response("Suggestion submitted successfully", data)
    except Exception as e:
        return error_response(str(e), status=400)