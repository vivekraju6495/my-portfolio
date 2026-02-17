from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from fastapi_limiter.depends import RateLimiter
from app.core.settings import settings
from app.core.response import error_response

router = APIRouter()

@router.get(
    "/download",
    dependencies=[
        Depends(
            RateLimiter(
                times=settings.RATE_LIMIT_RESUME_TIMES,
                seconds=settings.RATE_LIMIT_RESUME_SECONDS
            )
        )
    ]
)
def download_resume():
    try:
        return FileResponse(
            path=settings.RESUME_FILE_PATH,
            filename=settings.RESUME_FILE_NAME,
            media_type="application/pdf"
        )
    except Exception as e:
        return error_response(str(e), status=500)
