# MediaCore agent guide

This repository is **MediaCore** — **The Open Media Infrastructure Platform** (Extract • Process • Automate • Deliver). Not a single-purpose downloader: engine + plugins + pipeline + SDKs for building media applications. See [docs/getting-started/vision.md](docs/getting-started/vision.md). Docs site: VitePress in [`docs/`](docs/) (`npm run dev`).

## Cursor config

- Rules: [`.cursor/rules/`](.cursor/rules/)
- Skills: [`.cursor/skills/`](.cursor/skills/)

## Layout (canonical)

`apps/` · `packages/` · `providers/` · `plugins/` · `sdk/` · `benchmarks/` · `crates/` · `mediacore/` · `docs/` · `tests/` · `scripts/` · `docker/`

Do **not** recreate: `extractor/`, top-level `ffmpeg/`, `storage/`, `jobqueue/`, or a top-level `queue/` package (stdlib shadow).

## Hard constraints

1. Brand: MediaCore only (no legacy/foreign product names in new code or docs).
2. No access-control bypass / scraper-based platform extractors.
3. Core (`packages/`) must not depend on specific providers.
4. Prefer official/permitted APIs for working providers.

## Quick commands

```bash
uv sync --extra dev
uv run uvicorn apps.api.main:app --reload --port 8000
uv run pytest --ignore=tests/load --benchmark-disable
uv run python scripts/sync_platform_catalog.py --offline
```

## Skills to use

| Skill | When |
|-------|------|
| `mediacore-dev` | Run/test/doctor local stack |
| `mediacore-provider` | Add/upgrade a single provider |
| `mediacore-upgrade-loop` | Auto-implement platforms in batches (queue + yt-dlp host research only) |
| `mediacore-catalog` | Sync/regenerate platform catalog |

### Upgrade all platforms (agent loop)

```bash
uv run python scripts/provider_upgrade_queue.py next --limit 5
# implement batch → mark done / skipped_no_api → regenerate docs → pytest -m provider
```

yt-dlp (`github.com/yt-dlp/yt-dlp`) is **host/URL research only** — never port scrapers.
