from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from app.core.database import Base
from sqlalchemy import Float

class ResumeChunk(Base):
    __tablename__ = "resume_chunks"

    id = Column(Integer, primary_key=True, index=True)
    chunk_text = Column(Text, nullable=False)
    embedding = Column(ARRAY(Float), nullable=False)
