# Deployment

## Local (dev)

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
# optional worker
uv run mediacore worker start
```

Useful env vars (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `SYNC_DOWNLOAD` | Run downloads in-process (no Redis worker) |
| `USE_SQLITE` | Use SQLite instead of PostgreSQL |
| `REDIS_URL` | Queue / event fan-out |
| `STORAGE_BACKEND` | `local` (default) or cloud plugin |
| `STORAGE_ROOT` | Local files root |
| `EVENTS_REDIS_ENABLED` | Cross-process event bus |

## Docker Compose

```bash
cd docker && docker compose up --build
```

Includes API and supporting services (see `docker/docker-compose.yml`). Prometheus/Grafana provisioning lives under `docker/`.

## Helm / Kubernetes

Scaffold chart lives in the repo at `helm/mediacore/` (see `helm/README.md` on GitHub).

## Runtime modes

| Mode | Notes |
|------|-------|
| CLI + local API | Fastest feedback loop |
| Docker Compose | Shared team / CI-like stack |
| Helm | Production-oriented K8s path |
| Desktop | Tauri app talks to local/remote API (`apps/desktop`) |

## Health checks

- `GET /health` — liveness (public)
- `GET /v1/system` — version, plugins, ffmpeg (API key)
- `uv run mediacore doctor` — CLI aggregate check
