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
- `dropbox` working provider — shared file download via official `dl=1`
- `google_drive` working provider — public file download via `uc?export=download`
- CLI `mediacore providers` / `providers list` / `providers search` plus `provider_not_configured` hints
- CLI `mediacore process` — permitted download → ffmpeg convert pipeline
- Architecture map: `docs/architecture/mediacore-vs-ytdlp.md` (folder concepts vs yt-dlp)
- `media.ccc.de` working provider (public API + recording download)

### Changed

- README focused on 5-minute onboarding; deep guides moved under `docs/`
- README hero: centered title, tagline, and version badge (`0.1.0`)
- Clarified permitted-access provider model across README, platforms docs, providers plugin docs, and vision (detect many; metadata/download only when allowed; no scraper runtime)
- Aligned `WORKING_SKIP` / `RESERVED` in `scripts/materialize_catalog_providers.py` with early-register list in `packages/registry/providers.py`
- Agent rules (`AGENTS.md`, `.cursor/rules`): catalog modules are intentional — do not mass-delete; do not reintroduce stub shims
- Regenerated offline platform catalog / materialized modules to match working providers
- Upgrade queue batches: Dropbox/Google Drive `done`; several platforms `hosts_only` (daum, douyin, espn, …)
- Roadmap v0.2 notes permitted-provider growth and CLI providers UX

### Removed

- `providers/base_stub.py` deprecated shim (use `providers.base_module.PlatformModule`)
- `StubProvider` alias from `providers/base_module.py`
- Optional `YOUTUBE_API_KEY` / `META_ACCESS_TOKEN` metadata wiring (YouTube stays public oEmbed; Facebook/Instagram stay catalog/`blocked`)

## [0.1.0] — 2026-07-23

### Added

- Initial MediaCore foundation: engine packages, REST `/v1`, workers, CLI, plugin loader, provider catalog, multi-language SDKs, TestKit, Docker/Helm scaffolds
