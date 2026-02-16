from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel
from app.api.v1.controllers.profile_controller import get_profile_service

router = APIRouter()


@router.get("/", response_model=ResponseModel)
def get_profile(db: Session = Depends(get_db)):
    try:
        profile = get_profile_service(db)
        return success_response(
            message="Profile fetched successfully",
            data=profile
        )
    except Exception as e:
        return error_response(str(e), 500)

