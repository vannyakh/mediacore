# Providers

MediaCore resolves media URLs through a **provider registry**. Core stays platform-agnostic; all site knowledge lives here.

## One-screen map (whole repo)

```text
providers/<name>/     Working site logic (must have provider.py)
providers/modules/    ~1300 catalog packages — host detect + direct media only
packages/core/        downloader.py · http.py · models · provider protocol
packages/engine/      Orchestration
packages/registry/    URL → provider resolve
plugins/              ffmpeg · storage-local
apps/cli · apps/api · apps/worker
```

Canonical paths: [docs/architecture/layout.md](../docs/architecture/layout.md).  
vs yt-dlp folders: [docs/architecture/mediacore-vs-ytdlp.md](../docs/architecture/mediacore-vs-ytdlp.md).

## Layout (this folder)

```text
providers/
  <name>/           Working provider package (register early)
  modules/<slug>/   Catalog platform modules (~1300) — host detection + direct media
  platforms/        hosts.py, factory.py (catalog load)
  data/             sites_snapshot, extractors.json, providers_index.json, upgrade backlog
  base_module.py    PlatformModule base (catalog modules)
  direct_media.py   Shared direct-file metadata/download
  oembed.py         Shared public oEmbed helpers
  catalog.py        Catalog summary/search helpers
```

| Path | Role |
|------|------|
| `providers/<name>/provider.py` | Working implementation (`metadata_only` or `active`) |
| `providers/modules/<slug>/` | Catalog module — intentional; **do not mass-delete** |
| `providers/platforms/hosts.py` | Curated host maps merged into the index |
| `scripts/provider_upgrade_queue.py` | Batch upgrade queue |
| `packages/core/downloader.py` | HTTP fetch used by providers |
| `packages/core/http.py` | Shared networking client |
| `plugins/ffmpeg` | Convert/remux after a permitted download |

## Registration order

1. Working providers listed early in `packages/registry/providers.py`
2. Catalog modules from `providers.platforms.factory` (skip if `name` already registered)
3. `generic` + `example` last

When you add a working provider, also add its folder name to `WORKING_SKIP` in `scripts/materialize_catalog_providers.py` so materialize does not recreate a competing module package.

## What “supports a platform” means

1. **Detect** — module/working provider `supports(url)` via hosts
2. **Metadata** — public oEmbed / official or permitted API when available
3. **Download** — direct media on known hosts, or authorized/permitted APIs only

Page/watch URLs without a permitted API return `provider_not_configured`. That is expected, not a bug.

## Download capability matrix

| Capability | Status | Behavior |
|------------|--------|----------|
| **download** | `active` (legacy `available`) | Permitted file fetch (direct media, share links, public recording APIs) |
| **metadata** | `metadata_only` | Analyze / oEmbed / public API metadata; page download blocked |
| **catalog** | `not_configured` | Host detect + direct media on that host; watch pages not configured |

CLI: `mediacore providers list --download-only`

## Adding a working provider

1. Create `providers/<name>/__init__.py` + `provider.py` (same `name` as catalog entry)
2. Prefer `providers.oembed` or a documented public API
3. Register early in `packages/registry/providers.py`
4. Add folder to `WORKING_SKIP` in `scripts/materialize_catalog_providers.py`
5. Set `DOCS_WORKING_STATUS` in `scripts/generate_providers.py`
6. Contract test in `tests/providers/test_provider_contract.py`
7. Sync: `uv run python scripts/sync_platform_catalog.py --offline`

See skill `mediacore-provider` and `mediacore-upgrade-loop`.

## yt-dlp policy

Use [yt-dlp extractors](https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp/extractor) **only** to research:

- Host suffixes / `_VALID_URL` shape
- IE names

**Never** copy `_real_extract`, download URL decryption, HTML scrape, or login bypass into MediaCore. No yt-dlp runtime dependency for platform extraction.

## Regenerate catalog

```bash
uv run python scripts/sync_platform_catalog.py --offline
uv run python scripts/materialize_catalog_providers.py
uv run pytest -m provider -q --benchmark-disable
```
