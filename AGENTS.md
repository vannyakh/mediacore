# MediaCore agent guide

This repository is **MediaCore** — a **permitted media download CLI/API** (plus convert via ffmpeg). Not a scraper / yt-dlp clone. See [docs/getting-started/vision.md](docs/getting-started/vision.md). Docs: [`docs/`](docs/) (`npm run dev`).

## Cursor config

- Rules: [`.cursor/rules/`](.cursor/rules/)
- Skills: [`.cursor/skills/`](.cursor/skills/)

## Layout (canonical)

`apps/api` · `apps/cli` · `apps/worker` · `packages/` · `providers/` · `plugins/ffmpeg` · `plugins/storage-local` · `sdk/` · `docs/` · `tests/` · `scripts/` · `docker/`

Path roles: [`docs/architecture/layout.md`](docs/architecture/layout.md).  
**Extractor = `providers/`** · **Core = `packages/core`** · SDKs under `sdk/`.

Do **not** recreate: top-level `extractor/` / `ffmpeg/` / `storage/` / `queue/`, `dashboard/`, `helm/`, `benchmarks/`, `crates/`, cloud storage backends.

## Hard constraints

1. Brand: MediaCore only (no legacy/foreign product names in new code or docs).
2. No access-control bypass / scraper-based platform extractors.
3. Core (`packages/`) must not depend on specific providers.
4. Prefer official/permitted APIs for working providers.

## Quick commands

```bash
uv sync --extra dev
uv run uvicorn apps.api.main:app --reload --port 8000
uv run pytest tests/unit/cli tests/providers -q --benchmark-disable
uv run python scripts/sync_platform_catalog.py --offline
```

## Skills to use

| Skill | When |
|-------|------|
| `mediacore-dev` | Run/test/doctor local stack |
| `mediacore-provider` | Add/upgrade a single provider |
| `mediacore-upgrade-loop` | Auto-implement platforms in batches (queue + yt-dlp host research only) |
| `mediacore-catalog` | Sync/regenerate platform catalog |

### Upgrade platforms (agent loop)

```bash
uv run python scripts/provider_upgrade_queue.py next --limit 5
# implement batch → mark done / skipped_no_api → regenerate docs → pytest -m provider
```

yt-dlp is **host/URL research only** — never port scrapers.
Catalog modules under `providers/modules/` are intentional for URL detection — do not mass-delete.
See [`providers/README.md`](providers/README.md).
