import os
from typing import List, Dict, Any

from openai import AsyncOpenAI
import httpx


class LLMClient:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "openai")  # 'openai' or 'ollama'

        if self.provider == "openai":
            self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        else:
            self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
            self.ollama_model = os.getenv("OLLAMA_MODEL", "llama3.1")

    async def resume_chat(
        self,
        message: str,
        context: str,
        history: List[Dict[str, str]] | None = None,
        mode: str = "default",
    ) -> str:
        system_prompt = self._build_system_prompt(mode)
        user_prompt = self._build_user_prompt(message, context)

        if self.provider == "openai":
            messages: List[Dict[str, str]] = [{"role": "system", "content": system_prompt}]
            if history:
                messages.extend(history)
            messages.append({"role": "user", "content": user_prompt})

            resp = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.2,
                max_tokens=500,
            )
            return resp.choices[0].message.content.strip()

        # Ollama chat
        payload = {
            "model": self.ollama_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                *(history or []),
                {"role": "user", "content": user_prompt},
            ],
            "options": {"temperature": 0.2},
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.ollama_url}/api/chat",
                json=payload,
                timeout=120,
            )
            resp.raise_for_status()
            data = resp.json()
            return data["message"]["content"].strip()

    def _build_system_prompt(self, mode: str) -> str:
        base = """
You are an AI assistant trained ONLY on the resume of a backend engineer named Vivek Raju.

RULES:
1. Use ONLY the provided resume context.
2. If the answer is NOT in the context, reply exactly:
   "I’m only trained to answer questions based on Vivek’s resume."
3. Do NOT guess or hallucinate.
4. Keep answers clear, concise, and professional.
""".strip()

        if mode == "recruiter":
            base += """
When in recruiter mode:
- Speak like a technical recruiter pitching Vivek to a hiring manager.
- Emphasize impact, ownership, and technical depth.
""".strip()
        elif mode == "kid":
            base += """
When in kid mode:
- Explain Vivek’s experience in very simple, child-friendly language.
- Avoid technical jargon.
""".strip()

        return base

    def _build_user_prompt(self, message: str, context: str) -> str:
        return f"""
[CONTEXT]
{context}

[USER QUESTION]
{message}

[ANSWER]
""".strip()

