---
title: Deployment
---

<script setup>
const modes = [
  { title: "Local API", href: "#local-dev", hint: "Fastest loop", icon: "https://cdn.simpleicons.org/python/3776AB" },
  { title: "Docker", href: "#docker-compose", hint: "api + worker", icon: "https://cdn.simpleicons.org/docker/2496ED" },
]
const checks = [
  { value: "/health", label: "Liveness" },
  { value: "/v1/system", label: "Version & plugins" },
  { value: "doctor", label: "CLI aggregate" },
]
</script>

<DocHero
  eyebrow="Run"
  title="Deployment"
  lead="Local sync mode for day-one DX; Docker Compose for api + worker + postgres + redis."
/>

<DocLinks :items="modes" compact />

## Local (dev)

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
uv run mediacore worker start   # optional when SYNC_DOWNLOAD=false
```

| Variable | Purpose |
|----------|---------|
| `SYNC_DOWNLOAD` | In-process downloads (no Redis worker) |
| `USE_SQLITE` | SQLite instead of PostgreSQL |
| `REDIS_URL` | Queue when not sync |
| `STORAGE_ROOT` | Local files root |
| `EVENTS_REDIS_ENABLED` | Cross-process event bus (default false) |

## Docker Compose

```bash
cd docker && docker compose up --build
```

Services: `api`, `worker`, `postgres`, `redis`.

## Health checks

<DocStats :items="checks" />

```bash
curl -s http://localhost:8000/health
curl -s -H "X-API-Key: dev-api-key-change-me" http://localhost:8000/v1/system
uv run mediacore doctor
```
