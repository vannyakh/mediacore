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

```bash
curl -s http://localhost:8000/health
curl -s -H "X-API-Key: dev-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/video.mp4"}' \
  http://localhost:8000/v1/analyze

uv run mediacore doctor
uv run mediacore analyze https://example.com/video.mp4
```

Docker:

```bash
cd docker && docker compose up --build
```

---

## CLI

```bash
mediacore analyze URL
mediacore download URL [--wait]
mediacore convert file.mp4 [--wait]
mediacore subtitle file.mp4 [--wait]
mediacore plugin list
mediacore plugin install NAME|PATH
mediacore worker start
mediacore doctor
```

Flags: `--base`, `--key` (or `MEDIACORE_BASE` / `MEDIACORE_API_KEY`).

---

## Project layout

```text
mediacore/
  apps/         api, worker, cli, dashboard, desktop, studio, …
  packages/     core, engine, registry, plugins, events, queue, testkit, mediacore_benchmark, …
  providers/    platform extractors (independent of core)
  plugins/      storage, ffmpeg, webhooks, AI, …
  sdk/          JS, TS, Python, Rust, Go, Dart, C#, …
  benchmarks/   standalone Criterion + Python performance suite
  crates/       Rust engine foundation
  docs/         guides (getting started, architecture, API, …)
  tests/        unit → load / chaos / benchmark
  docker/       local compose stack
  scripts/      catalog + developer tooling
```

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
