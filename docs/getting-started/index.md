# Getting started

Get MediaCore running locally in a few minutes.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Optional: Docker, FFmpeg (for convert / thumbnail / clip), Redis (async workers)

## Install & run API

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
```

Dev API key: `dev-api-key-change-me`

## First request

```bash
curl -s -H "X-API-Key: dev-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/video.mp4"}' \
  http://localhost:8000/v1/analyze
```

## CLI

```bash
uv run mediacore doctor
uv run mediacore analyze https://example.com/video.mp4
uv run mediacore download https://example.com/video.mp4 --wait
uv run mediacore convert ./movie.mp4 --container webm
uv run mediacore subtitle ./movie.mp4
uv run mediacore plugin list
uv run mediacore plugin install storage-local
uv run mediacore worker start
```

Global flags: `--base`, `--key` (env: `MEDIACORE_BASE`, `MEDIACORE_API_KEY`).

## Next steps

- [Vision](./vision) — why MediaCore exists
- [Architecture](/architecture/) — how the stack fits together
- [API](/api/) — full REST surface
- [SDK](/sdk/) — language clients
- [Plugins](/plugins/) — extend storage, media, notifications
- [Deployment](/deployment/) — Docker and Helm
- [Testing](./testing) — TestKit and CI layers
