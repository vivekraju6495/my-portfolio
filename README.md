# My Portfolio — AI‑Powered Resume Website

This is my personal portfolio project built with **FastAPI**, **Next.js**, **PostgreSQL + pgvector**, and **Docker**.  
It is fully dynamic (database‑driven) and includes AI tools for resume Q&A, job fit analysis, skill insights, and more.

---

## 🚀 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![OpenAI API](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)

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

### 3. Personal Chatbot  
Chatbot trained on:
- My resume  
- My experience  
- My projects  
- My portfolio content  

---

## 📊 Data Processing & Analytics Features (Pandas + NumPy)
Your portfolio backend includes a lightweight data‑analysis layer powered by Pandas and NumPy, enabling structured insights and analytics directly from your API.

### ✔ Resume Insights API
Processes raw resume text and returns meaningful analytics:
- Word count
- Sentence count
- Top 10 most frequent words
- Average word length
- Text preprocessing using Pandas + NumPy

### ✔ Skills Analytics API
Analyzes your skill set using Pandas DataFrames:
- Skill categorization
- Grouping by category
- Total skill count
- Category‑wise breakdown
- Pandas DataFrame operations for fast analysis

These features demonstrate real data‑processing capabilities and prepare the backend for future AI/RAG enhancements.
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
