FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (needed for psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose port
EXPOSE 8000

# 🔥 IMPORTANT:
# Run migrations + seeder BEFORE starting server
CMD ["sh", "-c", "python -m alembic upgrade head && python -m app.db.seeder && uvicorn app.main:app --host 0.0.0.0 --port 8000"]