import httpx
import asyncio
from app.core.config import settings


class EmbeddingService:
    """
    Supports:
    - Local embeddings (Ollama)
    - OpenAI embeddings (production)
    """

    async def embed(self, text: str) -> list[float]:
        if settings.AI_PROVIDER == "local":
            return await self._local_embedding(text)
        return await self._openai_embedding(text)

    def embed_sync(self, text: str) -> list[float]:
        """Sync wrapper for ingestion scripts."""
        return asyncio.run(self.embed(text))

    # ---------------------------------------------------------
    # LOCAL EMBEDDINGS (OLLAMA)
    # ---------------------------------------------------------
    async def _local_embedding(self, text: str) -> list[float]:
        async with httpx.AsyncClient(timeout=settings.AI_TIMEOUT_SECONDS) as client:
            response = await client.post(
                "http://localhost:11434/api/embeddings",
                json={"model": "llama3", "prompt": text}
            )
            data = response.json()
            return data.get("embedding", [])

    # ---------------------------------------------------------
    # OPENAI EMBEDDINGS
    # ---------------------------------------------------------
    async def _openai_embedding(self, text: str) -> list[float]:
        from openai import OpenAI
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.embeddings.create(
            model=settings.OPENAI_EMBEDDING_MODEL,
            input=text
        )

        return response.data[0].embedding
