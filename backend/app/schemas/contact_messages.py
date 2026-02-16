from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class ContactMessageSchema(BaseModel):
    uuid: UUID
    name: str
    email: EmailStr
    message: str
    created_at: datetime

    class Config:
        from_attributes = True


class ContactMessageCreateSchema(BaseModel):
    name: str
    email: EmailStr
    message: str
