from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    success: bool = True
    message: Optional[str] = None
    status: int = 200
    data: Optional[Any] = None
