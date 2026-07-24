---
title: MediaCore vs yt-dlp layout
---

# Where things live (vs yt-dlp concepts)

MediaCore is **not** a yt-dlp fork. There is no top-level `extractor/`.

Inspired by the [yt_dlp package tree](https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp) — same roles, MediaCore names, **no scraper ports**.

| yt-dlp | MediaCore | Role |
|--------|-----------|------|
| `extractor/` | `providers/` + `providers/modules/` | Site detect + permitted metadata/download |
| `YoutubeDL.py` | `packages/engine` | Orchestration |
| `downloader/` | `packages/core/downloader/` | HTTP + HLS (ffmpeg) fetch |
| `networking/` | `packages/core/networking/` | Shared httpx client |
| `postprocessor/` | `plugins/ffmpeg` + `packages/media` | Convert / stream fetch |
| `utils/` | `packages/core/parser.py`, `validator.py` | Shared helpers |
| CLI | `apps/cli` | User commands |

```text
URL → packages/registry → providers/<extractor>
  → packages/core/networking · packages/core/downloader
  → packages/engine
  → plugins/ffmpeg (optional)
```

| Extractor status | Expectation |
|------------------|-------------|
| `active` | File download permitted |
| `metadata_only` | Analyze only (`-s`) |
| catalog `not_configured` | Host detect + direct media on that host |

yt-dlp extractors are **host / `_VALID_URL` research only** — never port `_real_extract` scrapers.
