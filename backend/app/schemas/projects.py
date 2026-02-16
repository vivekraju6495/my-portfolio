from uuid import UUID
from pydantic import BaseModel

class ProjectAchievementSchema(BaseModel):
    uuid: UUID
    achievement_text: str

    class Config:
        from_attributes = True

class ProjectSchema(BaseModel):
    uuid: UUID
    project_name: str
    role: str
    tech_stack: str
    description: str
    project_url: str | None
    github_url: str | None
    doc_url: str | None
    achievements: list[ProjectAchievementSchema]

    class Config:
        from_attributes = True
