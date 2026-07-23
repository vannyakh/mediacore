---
name: mediacore-dev
description: >-
  Run and verify the MediaCore local stack (API, tests, catalog regenerate, CLI doctor).
  Use when starting the server, running pytest, syncing the platform catalog, or
  checking MediaCore developer workflow.
---

# MediaCore Dev Workflow

## Setup

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
```

Dev API key: `dev-api-key-change-me`

## Run API

```bash
uv run uvicorn apps.api.main:app --reload --port 8000
# or
./scripts/dev.sh
```

## Tests

```bash
uv run pytest --ignore=tests/load --benchmark-disable
# or marker suite
uv run pytest -m "unit or api or provider or plugin or storage or regression" -q
```

## Catalog

```bash
uv run python scripts/sync_platform_catalog.py --offline
```

## CLI smoke

```bash
uv run mediacore doctor
uv run mediacore analyze https://example.com/video.mp4
```

## Checklist

- [ ] Brand text remains MediaCore-only
- [ ] No scraper runtime deps added for providers
- [ ] `/v1/health` and `/v1/providers` behave as expected
