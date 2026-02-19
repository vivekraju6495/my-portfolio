from app.core.config import settings

class AIConfig:
    provider: str = settings.AI_PROVIDER

    # Local AI (Ollama)
    local_url: str = settings.LOCAL_AI_URL

    # OpenAI
    openai_api_key: str | None = settings.OPENAI_API_KEY
    openai_model: str = settings.OPENAI_MODEL
    openai_embedding_model: str = settings.OPENAI_EMBEDDING_MODEL

    # Behavior
    temperature: float = settings.AI_TEMPERATURE
    max_tokens: int = settings.AI_MAX_TOKENS
    timeout_seconds: int = settings.AI_TIMEOUT_SECONDS
    max_retries: int = settings.AI_MAX_RETRIES


ai_config = AIConfig()
