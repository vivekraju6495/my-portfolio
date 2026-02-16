from uuid import UUID
from pydantic import BaseModel

class ContactCreateSchema(BaseModel):
    name: str
    email: str
    message: str

class ContactResponseSchema(BaseModel):
    uuid: UUID
    name: str
    email: str
    message: str

    class Config:
        from_attributes = True

