from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    role: str
    summary: str
