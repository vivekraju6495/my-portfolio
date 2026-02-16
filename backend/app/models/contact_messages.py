import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.core.database import Base

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
