from app.schemas.common import ResponseModel

def success_response(message: str, data=None, status: int = 200):
    return ResponseModel(
        success=True,
        message=message,
        status=status,
        data=data
    )

def error_response(message: str, status: int = 400, data=None):
    return ResponseModel(
        success=False,
        message=message,
        status=status,
        data=data
    )
