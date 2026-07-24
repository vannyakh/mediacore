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
  → metadata (oEmbed / official or public API)
  → download (direct media / share links / public recording APIs only)
  → plugins (ffmpeg convert, whisper, storage)
```

| Provider status | CLI expectation |
|-----------------|-----------------|
| `active` | `mediacore URL` can fetch a file |
| `metadata_only` | `mediacore -s URL` works; download fails with `provider_not_configured` |
| catalog / `not_configured` | Direct media on known hosts may download; watch pages do not |

CLI shortcuts (usage style only — not a yt-dlp port):

- `mediacore URL` / `-F` / `-s` / `-o` / `-a urls.txt` — analyze or permitted download
- `mediacore providers list --download-only` — what can fetch a file today
- `mediacore process URL` — download → convert (ffmpeg plugin) for **permitted** sources only

Not scrape+ffmpeg. No promise of “download every site.”

Page/watch URLs without a permitted API return `provider_not_configured`. yt-dlp extractors are used only for **host / `_VALID_URL` research** — never ported.
