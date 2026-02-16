from pydantic import BaseModel
from uuid import UUID

class SkillSchema(BaseModel):
    uuid: UUID
    category: str
    skill_name: str

    class Config:
        from_attributes = True
