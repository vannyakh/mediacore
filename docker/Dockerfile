FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY mediacore ./mediacore
COPY packages ./packages
COPY providers ./providers
COPY plugins ./plugins
COPY apps ./apps
COPY extractor ./extractor
COPY ffmpeg ./ffmpeg
COPY storage ./storage
COPY jobqueue ./jobqueue
COPY alembic ./alembic
COPY alembic.ini ./
COPY main.py ./

RUN pip install --no-cache-dir -e .

ENV PYTHONUNBUFFERED=1 \
    USE_SQLITE=false \
    DATABASE_URL=postgresql+psycopg://mediacore:mediacore@postgres:5432/mediacore \
    REDIS_URL=redis://redis:6379/0 \
    STORAGE_ROOT=/data/files \
    APP_NAME=MediaCore

EXPOSE 8000

CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
