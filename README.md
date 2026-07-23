# MediaCore

> The open-source media extraction, processing, and automation platform.

Build media workflows from a single modular foundation — APIs, SDKs, CLI, dashboard, workers, and a plugin ecosystem.

**Principle:** MediaCore is the **platform**, not a pile of provider scrapers. The core provides pipelines, jobs, events, plugins, APIs, and config. Providers stay independent.

## Quick start

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
```

Dev API key: `dev-api-key-change-me`

```bash
curl -s http://localhost:8000/health
curl -s -H "X-API-Key: dev-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/video.mp4"}' \
  http://localhost:8000/v1/analyze

uv run mediacore doctor
uv run mediacore analyze https://example.com/video.mp4
```

## Ecosystem

| Component | Path | Status |
|-----------|------|--------|
| Engine | `packages/engine` | Python foundation (Rust core planned in `crates/`) |
| API | `apps/api` | REST `/v1/*` |
| Worker | `apps/worker` | Dramatiq queues |
| CLI | `apps/cli` | `mediacore` |
| Dashboard | `apps/dashboard` | Next.js |
| Studio | `apps/studio` | Scaffold |
| Desktop | `apps/desktop` | Tauri scaffold |
| Providers | `providers/` | generic, filesystem, vimeo, example |
| Plugins | `plugins/` | storage-local, ffmpeg, webhook, … |
| SDKs | `sdk/` | JS/TS/Python (+ stubs) |

## Pipeline

```text
URL → Analyze → Metadata → Manifest → Formats → Download → Processing → Export → Events
```

## API (v1)

`POST /v1/analyze` · `download` · `audio` · `video` · `subtitles` · `thumbnail` · `convert` · `clip` · `jobs`  
`GET /v1/jobs/{id}` · `providers` · `plugins` · `system` · `GET /health`

`/api/v1/*` remains as a compatibility alias.

## Docker

```bash
cd docker && docker compose up --build
```

## Docs

- [Architecture](docs/architecture.md)
- [API](docs/api.md)
- [Providers](docs/providers.md)
- [Testing](docs/testing.md)
- [Roadmap](docs/roadmap.md)

## Compliance

Providers must use official/supported APIs or content you have permission to access. MediaCore does not bypass platform access controls or Terms of Service.

## Tests

```bash
uv sync --extra dev
# PR-critical suite
uv run pytest -m "not load and not stress and not chaos and not benchmark"
# Coverage
uv run pytest --cov=packages --cov=providers --cov=apps
```

See [docs/testing.md](docs/testing.md) for layers, markers, contracts, and load tests.
