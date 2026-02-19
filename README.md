# My Portfolio — AI‑Powered Resume Website

This is my personal portfolio project built with **FastAPI**, **Next.js**, **PostgreSQL + pgvector**, and **Docker**.  
It is fully dynamic (database‑driven) and includes AI tools for resume Q&A, job fit analysis, and skill insights.

---

## 🚀 Tech Stack

### Backend
- FastAPI
- Python
- PostgreSQL
- pgvector (for embeddings)
- Redis (for Rate-Limiting)
- Docker

### Frontend
- Next.js
- React
- Tailwind CSS
- Docker

### AI Layer
- LLM + RAG
- Embeddings stored in pgvector
- Resume Q&A
- Job Description Analyzer
- Skills Gap Insights
- Personal Chatbot

---

## 🧠 AI Features

### 1. Resume Q&A  
Ask questions about my experience, skills, or projects.

### 2. Job Description Analyzer  
Paste a JD → get:
- Fit score  
- Matching skills  
- Missing skills  
- Suggestions  

### 3. Skills Gap Insights  
Compares my resume to a target role.

### 4. Personal Chatbot  
Chatbot trained on:
- My resume  
- My experience  
- My projects  
- My portfolio content  

---

## 🐳 Running the Project (Docker)
    docker-compose up --build

Backend → http://localhost:8000  
Frontend → http://localhost:3000  

---
## 🚀 API Documentation (Swagger UI)
FastAPI automatically generates interactive API documentation.

**Swagger UI:**  
http://localhost:8000/docs

**ReDoc:**  
http://localhost:8000/redoc

---

## 📡 API Base URL
All API endpoints follow this base structure:
http://localhost:8000/api/v1/{endpoint}

Example:

- **Profile:**  
  `GET http://localhost:8000/api/v1/profile`

- **Health Check:**  
  `GET http://localhost:8000/health`

---

## 📦 Common API Response Structure

Every API returns a consistent JSON structure:


    {
      "success": true,
      "message": "Description of the result",
      "status": 200,
      "data": { }
    }

---

## ⚡ Performance & Security Features

Redis‑Powered Rate Limiting
The backend uses Redis to enforce production‑grade rate limiting on sensitive endpoints such as:
- Resume download
- Contact form submissions
- Suggestions API
This protects the API from abuse and ensures fair usage.
Rate limiting is fully configurable via environment variables

  Example:
  - RATE_LIMIT_RESUME_TIMES=3
  - RATE_LIMIT_RESUME_SECONDS=60

    Users can download the resume 3 times per minute before receiving a 429 Too Many Requests response.

## 🩺 Health Check (with Redis Status)
The /health endpoint returns real‑time system status, including Redis connectivity:

 - `GET http://localhost:8000/health`

  {
    "success": true,
    "message": "Health check successful",
    "status": 200,
    "data": {
      "status": "ok",
      "redis": "connected"
    }
  }

  - If Redis Connection faild, Response show:
   
      - "redis": "failed"

## 🗄 Redis Integration
  Redis is used for:
  - Rate limiting counters
  - TTL‑based request tracking
  - Fast, in‑memory operations
  You can inspect Redis keys using RedisInsight, a GUI tool that visualizes:
  - Rate‑limit keys
  - TTL countdown
  - API usage patterns
  Redis runs inside Docker and is exposed on:


## 📞 Contact

If you're reviewing this project, feel free to reach out.
