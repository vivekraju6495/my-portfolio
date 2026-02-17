from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class SuggestionSchema(BaseModel):
    id: int
    uuid: UUID
    suggestion: str
    created_at: datetime

    class Config:
        from_attributes = True


class SuggestionCreateSchema(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    suggestion: str

