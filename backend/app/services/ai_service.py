import httpx
from app.core.config import settings


class AIService:
    """
    AI service that supports:
    - Local AI (Ollama)
    - OpenAI (production)
    """

    async def generate(self, prompt: str) -> str:
        """
        Main entry point.
        Chooses provider based on AI_PROVIDER env variable.
        """
        if settings.AI_PROVIDER == "local":
            return await self._local_llm(prompt)
        return await self._openai_llm(prompt)

    # ---------------------------------------------------------
    # LOCAL AI (OLLAMA)
    # ---------------------------------------------------------
    async def _local_llm(self, prompt: str) -> str:
        """
        Calls Ollama running locally on http://localhost:11434
        """
        async with httpx.AsyncClient(timeout=settings.AI_TIMEOUT_SECONDS) as client:
            response = await client.post(
                settings.LOCAL_AI_URL,
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )

            data = response.json()
            return data.get("response", "")

    # ---------------------------------------------------------
    # OPENAI (PRODUCTION)
    # ---------------------------------------------------------
    async def _openai_llm(self, prompt: str) -> str:
        """
        Calls OpenAI Chat Completion API
        """
        from openai import OpenAI
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=settings.AI_TEMPERATURE,
            max_tokens=settings.AI_MAX_TOKENS,
        )

        return response.choices[0].message["content"]
