import uuid
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy.orm import relationship
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    project_name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=True)
    tech_stack = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    project_url = Column(String(255), nullable=True)
    github_url = Column(String(255), nullable=True)
    doc_url = Column(String(255), nullable=True)

    achievements = relationship(
        "ProjectAchievement",
        back_populates="project",
        cascade="all, delete-orphan"
    )


from app.models.project_achievements import ProjectAchievement