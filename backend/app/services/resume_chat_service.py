from typing import List, Dict
from app.services.llm_client import LLMClient
from app.services.resume_vector_store import ResumeVectorStore


class ResumeChatService:
    def __init__(self):
        self.llm = LLMClient()
        self.vector_store = ResumeVectorStore()
        self.history: List[Dict[str, str]] = []

    async def chat(self, message: str, mode: str = "default") -> str:
        # retrieve relevant chunks
        context_chunks = await self.vector_store.search(message)
        context = "\n\n".join(context_chunks)

        # append to history
        self.history.append({"role": "user", "content": message})

        reply = await self.llm.resume_chat(
            message=message,
            context=context,
            history=self.history,
            mode=mode,
        )

        self.history.append({"role": "assistant", "content": reply})
        return reply
