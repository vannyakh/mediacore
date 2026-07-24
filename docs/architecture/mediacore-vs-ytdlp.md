---
title: MediaCore vs yt-dlp layout
---

# Where things live (vs yt-dlp concepts)

MediaCore is **not** a yt-dlp fork. Concepts map to different folders — there is no top-level `extractor/`.

| yt-dlp idea | MediaCore path | Role |
|-------------|----------------|------|
| `extractor/` | [`providers/`](../../providers/README.md) + `providers/modules/` | Site detection + permitted metadata/download |
| `YoutubeDL.py` | `packages/engine` + `packages/core/pipeline.py` | Orchestration |
| `downloader/` | `packages/core/downloader.py` | HTTP file fetch |
| `networking/` | `packages/core/http.py` | Shared httpx client / headers |
| `postprocessor/` | `plugins/ffmpeg`, `whisper`, `metadata`, … | Convert / AI / enrich after download |
| CLI / options | `apps/cli` | User-facing commands |
| Self-update | Releases / docs (no `update.py` runtime) | — |

## One-screen repo map

```text
apps/          api · worker · cli · dashboard · …
packages/
  core/        downloader, http, models, provider protocol, pipeline
  engine/      job orchestration
  registry/    resolve URL → provider
  queue/       Dramatiq jobs
providers/
  <name>/      working providers (register early)
  modules/     ~1300 catalog packages — host detect + direct media
plugins/       ffmpeg, storage-*, whisper, webhook, …
sdk/           language clients
```

## Pipeline (honest)

```text
URL → Registry → Provider
  → metadata (oEmbed / official API / token)
  → download (direct media or permitted share links only)
  → plugins (ffmpeg convert, whisper, storage)
```

CLI shortcut: `mediacore process URL` runs download → convert (ffmpeg plugin) for **permitted** sources only — not scrape+ffmpeg.

Page/watch URLs without a permitted API return `provider_not_configured`. yt-dlp extractors are used only for **host / `_VALID_URL` research** — never ported.
