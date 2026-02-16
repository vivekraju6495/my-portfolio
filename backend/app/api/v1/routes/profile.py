from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.profile_controller import get_profile_controller
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel

router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_profile(db: Session = Depends(get_db)):
    try:
        data = get_profile_controller(db)
        return success_response("Profile fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)
