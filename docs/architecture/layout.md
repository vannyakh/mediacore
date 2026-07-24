---
title: Repository layout
---

# Repository layout

Canonical MediaCore paths. Prefer these names in new code and docs — do not recreate removed legacy roots.

## Top level

| Path | Role |
|------|------|
| `apps/` | User surfaces: `api`, `cli`, `worker`, `dashboard`, `scheduler`, `desktop`, `studio`, `gateway` |
| `packages/` | Shared libraries: `core`, `engine`, `registry`, `queue`, `storage`, `events`, `plugins`, … |
| `providers/` | Site knowledge only (working packages + `modules/` catalog) |
| `plugins/` | Optional capabilities: `ffmpeg`, `whisper`, `storage-*`, webhooks, … |
| `sdk/` | Language clients |
| `docs/` | VitePress site (`npm run dev`) |
| `tests/` | Pytest suites |
| `scripts/` | Catalog sync, provider queue, tooling |
| `docker/` | Compose stack (root `docker-compose.yml` includes it) |
| `helm/` | Kubernetes chart |
| `benchmarks/` | Performance suite |
| `crates/` | Rust engine foundation |
| `mediacore/` | Package version (`__version__`) |
| `alembic/` | DB migrations |
| `examples/` | Small sample scripts |
| `main.py` | Thin local entry → `apps.api.main` |

## Providers (detail)

| Path | Role |
|------|------|
| `providers/<name>/` | Working provider (`provider.py`) — register early in `packages/registry` |
| `providers/modules/<slug>/` | Catalog modules (~1300) — host detect + direct media |
| `providers/platforms/` | `hosts.py`, factory |
| `providers/data/` | Snapshot, index, upgrade backlog |
| `providers/base_module.py` | Catalog base class |
| `providers/direct_media.py` / `oembed.py` | Shared helpers |

Do **not** leave empty `providers/<name>/` folders (no `provider.py`). Catalog coverage for Facebook/Instagram lives under `providers/modules/`.

## Packages vs plugins

| Concern | Path |
|---------|------|
| HTTP download helper | `packages/core/downloader.py` |
| Orchestration | `packages/engine/` |
| URL → provider | `packages/registry/` |
| Job queue | `packages/queue/` (never top-level `queue/`) |
| Blob storage backends | `packages/storage/` |
| FFmpeg convert plugin | `plugins/ffmpeg/` (never top-level `ffmpeg/`) |

## Removed (do not recreate)

`extractor/` · top-level `ffmpeg/` · top-level `storage/` · `jobqueue/` · top-level `queue/` · `providers/stubs/` · empty working provider shells

## Related

- [Overview](./overview)
- [MediaCore vs yt-dlp](./mediacore-vs-ytdlp)
- Repository [`providers/README.md`](../../providers/README.md)
