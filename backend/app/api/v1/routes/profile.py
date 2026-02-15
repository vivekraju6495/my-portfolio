from fastapi import APIRouter
from app.schemas.common import ResponseModel
from app.schemas.profile import Profile

router = APIRouter(tags=["Profile"])

@router.get("/profile", response_model=ResponseModel)
def get_profile():
    profile = Profile(
        name="Vivek Raju",
        role="Senior Software Engineer",
        summary="Experienced software engineer specializing in NestJS, Node.js, Laravel, FastAPI, Odoo, and scalable systems."
    )
    return ResponseModel(
        success=True,
        message="Profile fetched successfully",
        data=profile
    )
