from fastapi import APIRouter

router = APIRouter(tags=["Profile"])

@router.get("/")
def get_profile():
    return {"message": "profile works"}
