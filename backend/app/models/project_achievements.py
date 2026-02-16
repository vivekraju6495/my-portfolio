import uuid
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy.orm import relationship
class ProjectAchievement(Base):
    __tablename__ = "project_achievements"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    project_id = Column(Integer, ForeignKey("projects.id"))
    achievement_text = Column(Text, nullable=False)

    project = relationship("Project", back_populates="achievements")
