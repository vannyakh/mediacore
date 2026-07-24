# packages/core — MediaCore runtime (inspired by yt-dlp layout)

Concept map from [yt-dlp/`yt_dlp`](https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp) → MediaCore.
**yt-dlp is host/URL research only** — we do not port scrapers or `_real_extract`.

| yt-dlp | MediaCore |
|--------|-----------|
| `YoutubeDL.py` | `packages/engine` |
| `extractor/` | `providers/` + `providers/modules/` |
| `downloader/` | `packages/core/downloader/` |
| `networking/` | `packages/core/networking/` |
| `postprocessor/` | `packages/core/postprocess.py` + `plugins/ffmpeg` |
| `utils/` | `packages/core/parser.py`, `validator.py`, `format_select.py` |
| CLI entry | `apps/cli` |

## This package

```
packages/core/
  networking/     # session · retry · client
  downloader/     # http · stream · resume · progress
  postprocess.py  # remux / extract_audio
  format_select.py
  models.py       # MediaMetadata, FormatInfo, …
  provider.py     # Provider protocol
  pipeline.py     # analyze → download → process stages
  parser.py       # URL / content-type helpers
  exceptions.py
  http.py         # re-export of networking (compat)
```
