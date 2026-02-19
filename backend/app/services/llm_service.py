import httpx
from app.core.config import settings
from openai import OpenAI


class LLMService:

    async def generate(self, prompt: str) -> str:
        if settings.AI_PROVIDER == "local":
            return await self._local_llm(prompt)
        return await self._openai_llm(prompt)

    # ---------------------------------------------------------
    # LOCAL LLM (OLLAMA)
    # ---------------------------------------------------------
    async def _local_llm(self, prompt: str) -> str:
        async with httpx.AsyncClient(timeout=settings.AI_TIMEOUT_SECONDS) as client:
            response = await client.post(
                "http://host.docker.internal:11434/api/generate",  #http://host.docker.internal:11434
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )
        data = response.json()
        return data.get("response", "")


    # ---------------------------------------------------------
    # OPENAI LLM
    # ---------------------------------------------------------
    async def _openai_llm(self, prompt: str) -> str:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
