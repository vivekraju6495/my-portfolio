PHASE 1 — AI Backend Foundation
1. Add AI config (model, keys, settings)
2. Create AI service layer (LLM + embeddings)
3. Add pgvector setup (vector column + index)
4. Build document loader (resume → chunks → embeddings)

PHASE 2 — AI Endpoints
1. Resume Q&A API
2. Job Description Analyzer API
3. Skills Gap Insights API
4. Personal Chatbot API

PHASE 3 — Observability & Safety
1. Rate limiting for AI endpoints
2. Logging (prompt, tokens, latency)
3. Error handling

PHASE 4 — Frontend Integration
1. Build AI tools UI
2. Connect to backend
3. Add loading states
4. Add rate limit UI

PHASE 5 — Final Polish
1. Analytics
2. Caching
3. Deployment



Reduce AI cost:
- Use gpt-4.1-mini
- Limit max tokens
- Cache responses in Redis
- Use embeddings before LLM
- Avoid long prompts

Use cheaper models:
- gpt-4.1-mini for everything
- Switch to bigger models only when needed

Cache responses:
- Redis caching for Q&A, JD analysis, skills gap
- 1–24 hour TTL

Avoid unnecessary LLM calls:
- Use vector search first
- Precompute embeddings
- Validate input
- Use short prompts

Use local models (free):
- Ollama
- LM Studio
- GPT4All
- Switch provider via env variables
