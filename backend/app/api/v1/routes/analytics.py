from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.controllers.analytics_controller import (
    get_analytics_controller,
    increment_visitors_controller,
    increment_resume_downloads_controller,
    increment_page_views_controller,
    increment_api_hits_controller
)
from app.core.response import success_response, error_response
from app.schemas.common import ResponseModel

router = APIRouter()

@router.get("/", response_model=ResponseModel)
def get_analytics(db: Session = Depends(get_db)):
    try:
        data = get_analytics_controller(db)
        return success_response("Analytics fetched successfully", data)
    except Exception as e:
        return error_response(str(e), status=404)


@router.post("/increment/visitors", response_model=ResponseModel)
def increment_visitors(db: Session = Depends(get_db)):
    try:
        data = increment_visitors_controller(db)
        return success_response("Visitor count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/resume-downloads", response_model=ResponseModel)
def increment_resume_downloads(db: Session = Depends(get_db)):
    try:
        data = increment_resume_downloads_controller(db)
        return success_response("Resume download count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/page-views", response_model=ResponseModel)
def increment_page_views(db: Session = Depends(get_db)):
    try:
        data = increment_page_views_controller(db)
        return success_response("Page view count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)


@router.post("/increment/api-hits", response_model=ResponseModel)
def increment_api_hits(db: Session = Depends(get_db)):
    try:
        data = increment_api_hits_controller(db)
        return success_response("API hit count incremented", data)
    except Exception as e:
        return error_response(str(e), status=400)
