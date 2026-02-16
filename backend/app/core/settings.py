from pydantic_settings import BaseSettings
from pydantic import Field
from pydantic import ConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    APP_NAME: str = "Vivek Portfolio API"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    OPENAI_API_KEY: str | None = None

    BACKEND_CORS_ORIGINS: List[str] = Field(default_factory=list)

settings = Settings()
