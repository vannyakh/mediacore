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

### Changed

- README focused on 5-minute onboarding; deep guides moved under `docs/`

## [0.1.0] — 2026-07-23

### Added

- Initial MediaCore foundation: engine packages, REST `/v1`, workers, CLI, plugin loader, provider catalog, multi-language SDKs, TestKit, Docker/Helm scaffolds
