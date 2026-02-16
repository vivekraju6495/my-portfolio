from uuid import UUID
from pydantic import BaseModel

class SuggestionCreateSchema(BaseModel):
    name: str | None
    email: str | None
    suggestion: str

class SuggestionResponseSchema(BaseModel):
    uuid: UUID
    name: str | None
    email: str | None
    suggestion: str

    class Config:
        from_attributes = True
