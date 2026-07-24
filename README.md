<p align="center">
  <img src="assets/logo.png" alt="MediaCore" width="160" />
</p>

<h1 align="center">MediaCore</h1>

<p align="center">
  <strong>Permitted media download CLI &amp; API</strong>
</p>

<p align="center">
  Extract · Process · Deliver
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.1.0-0ea5e9?style=flat-square" alt="Version 0.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /></a>
</p>

<p align="center">
  Analyze and download media from <strong>permitted</strong> sources (direct media, share links, public APIs).<br />
  Not a scraper / yt-dlp clone — watch-page stream extraction is out of scope.
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

```bash
uv run mediacore doctor
uv run mediacore https://example.com/video.mp4 -o './out/{title}.mp4'
uv run mediacore -s 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'   # metadata only
uv run mediacore providers list --download-only
```

Docker: `cd docker && docker compose up --build` (api + worker + postgres + redis).

---

## CLI

```bash
mediacore URL                      # download + wait when permitted
mediacore -F URL                   # list formats (analyze)
mediacore -s URL                   # simulate / analyze only
mediacore -o './out/{title}.mp4' URL
mediacore -a urls.txt              # batch file
mediacore download URL [--wait]
mediacore process URL [--container mp4]   # download → ffmpeg
mediacore providers list [--download-only]
mediacore doctor
```

Flags: `--base`, `--key`, `-q`/`-v` (or `MEDIACORE_BASE` / `MEDIACORE_API_KEY`).

---

## Project layout

```text
apps/api · apps/cli · apps/worker
packages/     core · engine · registry · queue · storage · events · …
providers/    <name>/ working  ·  modules/ catalog
plugins/      ffmpeg · storage-local
sdk/          python · javascript · typescript · php · go
docs/ · tests/ · scripts/ · docker/ · mediacore/
```

## SDKs (install)

```bash
pip install -e sdk/python                 # Python
npm install ./sdk/javascript              # Node
npm install ./sdk/typescript              # TypeScript
# PHP: composer path repo → sdk/php
# Go:  go mod replace → sdk/go
```

See [`sdk/README.md`](sdk/README.md) and [docs/sdk](docs/sdk/).

Full path table: [`docs/architecture/layout.md`](docs/architecture/layout.md).

### What works / what does not

| Works | Does not (by design) |
|-------|----------------------|
| Direct media download (`generic`, `filesystem`) | Watch-page scraping (YouTube/etc.) |
| Direct HLS/DASH stream URLs (`.m3u8` / `.mpd` via ffmpeg) | Extracting streams from watch pages |
| Dropbox / Google Drive public share download | Bypassing platform ToS |
| media.ccc.de public recordings | yt-dlp as a dependency |
| Metadata via oEmbed / public APIs | Universal “download any site” |

Use `mediacore -s URL` for metadata; `providers list --download-only` for file fetch.

---

## Documentation

```bash
cd docs && npm install && npm run dev   # http://localhost:5173
```

| Doc | Description |
|-----|-------------|
| [Getting started](docs/getting-started/) | Install + first download |
| [Platforms](docs/platforms/) | Providers / catalog |
| [API](docs/api/) | REST `/v1/*` |
| [SDKs](docs/sdk/) | Python · npm · PHP · Go |
| [Architecture](docs/architecture/) | Layout + engine |
| [Changelog](CHANGELOG.md) | Release notes |

---

## Compliance

Providers must use official/supported APIs or content you have permission to access.

## License

[Apache License 2.0](LICENSE)
