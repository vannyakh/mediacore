# Changelog

All notable changes to MediaCore are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Hardened CLI (`analyze`, `download`, `convert`, `subtitle`, `plugin list|install`, `worker start`, `doctor`) with `--wait`, env overrides, and unit tests
- Documentation layout: concise root README plus `docs/{getting-started,architecture,api,sdk,plugins,deployment}/`
- VitePress docs site (`docs/` — `npm run dev` / `build` / `preview`)
- Root OSS files: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `ARCHITECTURE.md`, `ROADMAP.md`, `LICENSE` (Apache-2.0)
- `providers/README.md` — working vs catalog layout, registration order, and yt-dlp research-only policy
- README “What works today / what does not” table for permitted-access downloads
- `dropbox` / `google_drive` / `media.ccc.de` working providers (permitted share-link / public recording download)
- CLI `mediacore providers` / `providers list` / `providers search` plus `provider_not_configured` hints
- CLI `mediacore process` — permitted download → ffmpeg convert pipeline
- CLI URL-first UX (`mediacore URL`, `-F`, `-s`, `-o`, `-a` batch) — permitted paths only
- Architecture map: `docs/architecture/mediacore-vs-ytdlp.md`
- Thin download SDKs under `sdk/` with install docs: Python (`pip`), JS/TS (`npm`), PHP (`composer`), Go (`go mod`)
- Direct HLS/DASH stream download for permitted playlist URLs (`.m3u8` / `.mpd`) via ffmpeg in `packages/core/downloader/`

### Changed

- Align `packages/core` with [yt-dlp `yt_dlp` layout](https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp): `networking/` + `downloader/` subpackages (compat `http.py` re-export; no scraper ports)
- Slim download-tool core: keep `apps/api|cli|worker`, providers (extractors), `plugins/ffmpeg` + `storage-local`; remove dashboard/desktop/studio/gateway/scheduler, benchmarks, crates, helm, cloud storage backends, and extra plugins (SDKs restored as thin clients)
- Clarify extractor path = `providers/`; core = `packages/core` (no top-level `extractor/`)
- Canonical path guide: `docs/architecture/layout.md`; removed empty `providers/facebook` / `providers/instagram` shells (catalog modules remain)
- Permitted download-tool clarity: CLI groups providers as `download` vs `metadata`, adds `--download-only`, and docs/README lead with a working download example (YouTube-class = `-s` only)
- `DOCS_WORKING_STATUS` aligned to runtime `active` for Dropbox / Google Drive / media.ccc.de
- Local default: `EVENTS_REDIS_ENABLED=false`; doctor reports Redis as optional
- Clarified permitted-access model across README, platforms, vision, and providers README
- Aligned `WORKING_SKIP` / registry early-register list; regenerated offline catalog
- Agent rules: catalog modules intentional — do not mass-delete; no stub shims

### Removed

- `providers/base_stub.py` deprecated shim (use `providers.base_module.PlatformModule`)
- `StubProvider` alias from `providers/base_module.py`
- Optional `YOUTUBE_API_KEY` / `META_ACCESS_TOKEN` metadata wiring (YouTube stays public oEmbed; Facebook/Instagram stay catalog/`blocked`)

## [0.1.0] — 2026-07-23

### Added

- Initial MediaCore foundation: engine packages, REST `/v1`, workers, CLI, plugin loader, provider catalog, multi-language SDKs, TestKit, Docker/Helm scaffolds
