---
title: Repository layout
---

# Repository layout

Minimized download-tool layout. **Extractor = `providers/`**. **Core = `packages/core`**.

## Keep

```text
apps/api · apps/cli · apps/worker
packages/core/
  networking/ · downloader/   # yt-dlp-shaped subpackages
  models · provider · pipeline · parser
packages/engine        # orchestration (YoutubeDL analog)
packages/registry      # URL → extractor/provider
packages/queue · storage · config · events · plugins · media · auth · cache · logging
providers/             # extractors (working + modules catalog)
plugins/ffmpeg · plugins/storage-local   # postprocessor analog
sdk/ · docs/ · tests/ · scripts/ · docker/
```

| Path | Role (yt-dlp analog) |
|------|----------------------|
| `packages/core/networking/` | `networking/` |
| `packages/core/downloader/` | `downloader/` (+ HLS via ffmpeg) |
| `providers/<name>/` | extractor (working) |
| `providers/modules/` | extractor catalog (host detect + direct media) |
| `packages/engine/` | YoutubeDL-like coordinator |
| `packages/registry/` | extractor registry |
| `plugins/ffmpeg` | `postprocessor/` |

## Implement an extractor

1. Add `providers/<name>/provider.py` (implements `packages.core.provider.Provider`)
2. Register early in `packages/registry/providers.py`
3. Add folder to `WORKING_SKIP` in `scripts/materialize_catalog_providers.py`
4. Contract test in `tests/providers/`
5. Prefer oEmbed / public API / direct media / share-link — **no scrapers**

## Removed

Dashboard · desktop · studio · gateway · scheduler · helm · benchmarks · crates · cloud storage backends · notification plugins · top-level `extractor/` / `ffmpeg/` / `queue/`
