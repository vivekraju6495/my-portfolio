import uuid
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy.orm import relationship

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)  # internal only
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    linkedin = Column(String(255), nullable=False)
    github = Column(String(255), nullable=False)
    work_auth = Column(String(255), nullable=False)
    summary = Column(Text, nullable=False)

