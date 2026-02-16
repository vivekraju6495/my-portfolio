import uuid
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ExperienceAchievement(Base):
    __tablename__ = "experience_achievements"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    experience_id = Column(Integer, ForeignKey("experience.id"))
    achievement_text = Column(Text, nullable=False)

    experience = relationship("Experience", back_populates="achievements")