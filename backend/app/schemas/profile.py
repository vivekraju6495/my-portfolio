from pydantic import BaseModel
from uuid import UUID
class ProfileResponse(BaseModel):
    id: int
    uuid: UUID
    name: str
    title: str
    location: str
    email: str
    phone: str
    linkedin: str
    github: str
    work_auth: str
    summary: str

    class Config:
        from_attributes = True
