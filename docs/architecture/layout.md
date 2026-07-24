---
title: Repository layout
---

# Repository layout

Slim MediaCore download-tool layout. Prefer these paths in new code.

## Top level

| Path | Role |
|------|------|
| `apps/api` | REST `/v1` analyze / download / jobs |
| `apps/cli` | `mediacore` permitted download CLI |
| `apps/worker` | Dramatiq worker for async jobs |
| `packages/core` | Downloader, HTTP, models, provider protocol |
| `packages/engine` | Orchestration |
| `packages/registry` | URL → provider |
| `packages/queue` | Job queue (never top-level `queue/`) |
| `packages/storage` | Local (+ optional cloud backends in package) |
| `providers/` | Working providers + `modules/` catalog |
| `plugins/ffmpeg` | Convert / remux after download |
| `plugins/storage-local` | Default artifact storage |
| `sdk/` | Thin clients: Python, JS/TS, PHP, Go |
| `docs/` | VitePress site |
| `tests/` · `scripts/` · `docker/` · `alembic/` · `mediacore/` | Support |

## Providers

| Path | Role |
|------|------|
| `providers/<name>/provider.py` | Working provider (must exist) |
| `providers/modules/<slug>/` | Catalog host detect + direct media |
| `providers/platforms/` | Host maps + factory |

## Removed (do not recreate)

`apps/dashboard` · `desktop` · `studio` · `gateway` · `scheduler` · `benchmarks/` · `crates/` · `helm/` · extra notification/AI/cloud storage plugins · top-level `extractor/` / `ffmpeg/` / `storage/` / `queue/`

## Related

- [Overview](./overview)
- [MediaCore vs yt-dlp](./mediacore-vs-ytdlp)
- [`providers/README.md`](../../providers/README.md)
