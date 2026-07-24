# packages/core — MediaCore runtime (inspired by yt-dlp layout)

Concept map from [yt-dlp/`yt_dlp`](https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp) → MediaCore.
**yt-dlp is host/URL research only** — we do not port scrapers or `_real_extract`.

| yt-dlp | MediaCore |
|--------|-----------|
| `YoutubeDL.py` | `packages/engine` |
| `extractor/` | `providers/` + `providers/modules/` |
| `downloader/` | `packages/core/downloader/` |
| `networking/` | `packages/core/networking/` |
| `postprocessor/` | `plugins/ffmpeg` + `packages/media` |
| `utils/` | `packages/core/parser.py`, `validator.py`, … |
| CLI entry | `apps/cli` |

## This package

```
packages/core/
  networking/     # HTTP client helpers
  downloader/     # progressive file + direct HLS/DASH
  models.py       # MediaMetadata, FormatInfo, …
  provider.py     # Provider protocol
  pipeline.py     # extract → download → store stages
  parser.py       # URL / content-type helpers
  exceptions.py
  http.py         # re-export of networking (compat)
```
