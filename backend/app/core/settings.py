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

    BACKEND_CORS_ORIGINS: List[str] = Field(default_factory=list)

    REDIS_URL: str

    RATE_LIMIT_RESUME_TIMES: int = 3
    RATE_LIMIT_RESUME_SECONDS: int = 60

    RATE_LIMIT_CONTACT_TIMES: int = 1
    RATE_LIMIT_CONTACT_SECONDS: int = 60

    RATE_LIMIT_SUGGESTIONS_TIMES: int = 1
    RATE_LIMIT_SUGGESTIONS_SECONDS: int = 60

    RESUME_FILE_PATH: str
    RESUME_FILE_NAME: str


    # AI Provider
    AI_PROVIDER: str = Field(default="local")  
    # options: "local" or "openai"

    # Local AI (Ollama)
    LOCAL_AI_URL: str = Field(default="http://localhost:11434/api/generate")


    # OpenAI (Production)
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = Field(default="gpt-4.1-mini")
    OPENAI_EMBEDDING_MODEL: str = Field(default="text-embedding-3-small")
    # AI Behavior
    AI_TEMPERATURE: float = Field(default=0.2)
    AI_MAX_TOKENS: int = Field(default=800)
    AI_TIMEOUT_SECONDS: int = Field(default=30)
    AI_MAX_RETRIES: int = Field(default=3)


settings = Settings()
