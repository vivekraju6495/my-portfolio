from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.profile import ProfileResponse
from app.api.v1.controllers.profile_controller import get_profile_controller

router = APIRouter()

@router.get("/", response_model=ProfileResponse)
def get_profile(db: Session = Depends(get_db)):
    try:
        return get_profile_controller(db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
