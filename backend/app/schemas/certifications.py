from uuid import UUID
from pydantic import BaseModel


class CertificationSchema(BaseModel):
    uuid: UUID
    name: str
    issuer: str
    year: str

    class Config:
        from_attributes = True
