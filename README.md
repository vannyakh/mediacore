<p align="center">
  <img src="assets/logo.png" alt="MediaCore" width="160" />
</p>

<h1 align="center">MediaCore</h1>

<p align="center">
  <strong>The Open Source Media Infrastructure Platform</strong>
</p>

<p align="center">
  Extract · Process · Automate · Deliver
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.1.0-0ea5e9?style=flat-square" alt="Version 0.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Open%20Source-yes-22c55e?style=flat-square" alt="Open Source" /></a>
</p>

<p align="center">
  MediaCore is infrastructure for building media applications — not a single-purpose downloader.<br />
  Use it as a foundation for converters, AI pipelines, desktop apps, cloud services, REST APIs, CLIs, SDKs, and plugin marketplaces.
</p>

<p align="center">
  <em>Build once. Run everywhere.</em>
</p>

<p align="center">
  MediaCore គឺជា Open Source Media Infrastructure Platform ដែលត្រូវបានរចនាឡើងសម្រាប់ Developer<br />
  ក្នុងការបង្កើត Media Applications ដោយមិនចាំបាច់សរសេរ Media Engine ពីដំបូង។
</p>

---

## Quick start (≈5 minutes)

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
```

Dev API key: `dev-api-key-change-me`

Primary local workflow: **permitted download** (direct media / share links / public APIs).

```bash
curl -s http://localhost:8000/health
uv run mediacore doctor
# Working download (generic direct media):
uv run mediacore https://example.com/video.mp4 -o './out/{title}.mp4'
# Metadata only for YouTube-class pages (no page scrape download):
uv run mediacore -s 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
uv run mediacore providers list --download-only
```

Docker:

```bash
cd docker && docker compose up --build
```

---

## CLI

URL-first (yt-dlp-like UX, **permitted sources only** — not a scraper clone):

```bash
mediacore URL                      # download + wait when permitted
mediacore -F URL                   # list formats (analyze)
mediacore -s URL                   # simulate / analyze only
mediacore -o './out/{title}.mp4' URL
mediacore -a urls.txt              # batch file (# comments ok)
```

Subcommands:

```bash
mediacore analyze URL
mediacore download URL [--wait]
mediacore process URL [--container mp4]   # download → ffmpeg convert
mediacore convert file.mp4 [--wait]
mediacore subtitle file.mp4 [--wait]
mediacore providers              # download vs metadata groups + catalog
mediacore providers list [--status STATUS] [--download-only]
mediacore providers search QUERY
mediacore plugin list
mediacore plugin install NAME|PATH
mediacore worker start
mediacore doctor
```

Flags: `--base`, `--key`, `-q`/`-v` (or `MEDIACORE_BASE` / `MEDIACORE_API_KEY`).

---

## Project layout

```text
apps/         api · worker · cli · dashboard · scheduler · desktop · studio · gateway
packages/     core · engine · registry · queue · storage · media · plugins · events · …
providers/    <name>/ working providers  ·  modules/ catalog (~1300)
plugins/      ffmpeg · whisper · storage-* · webhook · …
sdk/          JS, TS, Python, Rust, Go, Dart, C#, …
docs/         VitePress  ·  tests/  ·  scripts/  ·  docker/  ·  helm/
benchmarks/   crates/   mediacore/ (__version__)
```

| Path | Put new code here |
|------|-------------------|
| Download / HTTP / models | `packages/core/` |
| Jobs / orchestration | `packages/engine/`, `packages/queue/` |
| Site detect + permitted fetch | `providers/<name>/` or `providers/modules/` |
| Convert / AI / storage plugins | `plugins/` |
| CLI / API | `apps/cli/`, `apps/api/` |

Full path table: [`docs/architecture/layout.md`](docs/architecture/layout.md).  
Providers: [`providers/README.md`](providers/README.md).  
vs yt-dlp folders: [`docs/architecture/mediacore-vs-ytdlp.md`](docs/architecture/mediacore-vs-ytdlp.md).

Do not recreate removed roots: `extractor/`, top-level `ffmpeg/` / `storage/` / `queue/` / `jobqueue/`.

### What works today / what does not

| Works | Does not (by design) |
|-------|----------------------|
| Analyze many platforms (host detection via catalog modules) | Scraping watch pages like a generic video downloader |
| Metadata via public oEmbed / permitted APIs (YouTube, TikTok, Vimeo, …) | Bypassing platform access controls or Terms of Service |
| Download **direct media**, Dropbox/`dl=1`, Google Drive public shares, media.ccc.de recordings | Unofficial stream extraction for every site |
| Jobs, plugins, SDKs, pipeline around permitted media | Shipping yt-dlp (or any scraper runtime) as a dependency |

Page/watch URLs without a permitted API return `provider_not_configured` until an official path is wired. Use `mediacore -s URL` for metadata; `mediacore providers list --download-only` for what can fetch a file today.

---

## Documentation

Docs are a [VitePress](https://vitepress.dev/) site under [`docs/`](docs/).

```bash
cd docs
npm install
npm run dev      # http://localhost:5173
npm run build
npm run preview
```

| Doc | Description |
|-----|-------------|
| [Getting started](docs/getting-started/) | Install, first analyze, CLI |
| [Platforms](docs/platforms/) | Available extractors + how to register |
| [Plugins](docs/plugins/) | Plugin catalog + how to register |
| [Architecture](docs/architecture/) | Engine, runtime, events, pipeline |
| [API](docs/api/) | REST `/v1/*` |
| [SDK](docs/sdk/) | Multi-language clients |
| [Deployment](docs/deployment/) | Docker, Helm, config |
| [Vision](docs/getting-started/vision.md) | Product positioning |
| [Testing](docs/getting-started/testing.md) | TestKit and CI layers |
| [Benchmarks](docs/benchmarks/) | Latency, memory, regressions |
| [Roadmap](ROADMAP.md) | Version plan |
| [Contributing](CONTRIBUTING.md) | How to contribute |
| [Security](SECURITY.md) | Vulnerability reporting |
| [Changelog](CHANGELOG.md) | Release notes |

---

## Compliance

Providers must use official/supported APIs or content you have permission to access. MediaCore does not bypass platform access controls or Terms of Service.

---

## License

[Apache License 2.0](LICENSE)

<p align="center">
  Made by the MediaCore community — <strong>One Core • Infinite Media Workflows</strong>
</p>
