# Open Source Roadmap

Aligned with the [vision](./vision): MediaCore as open media infrastructure.

Also summarized at the repository root [`ROADMAP.md`](https://github.com/mediacore/mediacore/blob/main/ROADMAP.md).

```text
v0.1 Foundation → v0.2 Platform Surfaces → v0.3 Desktop & Studio → v1.0 Stable Ecosystem
```

Statuses: **done** · **partial** · **planned**

---

## v0.1 — Foundation

| Item | Status | Notes |
|------|--------|-------|
| Engine | partial | Python `packages/engine`; Rust crate scaffold |
| Runtime | partial | Local workers; Docker/K8s paths expanding |
| CLI | done | `mediacore` |
| SDK | partial | Multi-language clients; unify surface |
| Local storage | done | Default backend + storage interface |
| TestKit | partial | `packages/testkit` mocks, contracts, fixtures |

Also in tree: plugin loader, HTTP helpers, job system, provider architecture.

---

## v0.2 — Platform surfaces

| Item | Status | Notes |
|------|--------|-------|
| Dashboard | partial | Next.js scaffold + jobs/events views |
| Event system | done | Bus, Redis fan-out, SSE `/v1/events`, webhook/bots |
| Pipeline | partial | Analyze → download → process stages |
| Workers | done | Dramatiq job runtime |
| Plugin system | partial | Loader + storage/ffmpeg/webhook plugins |
| REST API | done | `/v1/*` (+ `/api/v1/*` alias) |

---

## v0.3 — Desktop, Studio & quality

| Item | Status | Notes |
|------|--------|-------|
| Desktop (Tauri) | planned | `apps/desktop` scaffold |
| Studio | planned | Visual workflow editor (`apps/studio`) |
| Benchmark suite | partial | Standalone `benchmarks/` + `packages/mediacore_benchmark` + Criterion |
| Marketplace (experimental) | planned | Plugin discovery / publish |

---

## v1.0 — Stable ecosystem

| Item | Status | Notes |
|------|--------|-------|
| Stable plugin API | planned | Versioned contracts + compatibility tests |
| Long-term SDK compatibility | planned | Shared method names across languages |
| Comprehensive documentation | planned | Docs site + cookbook + deployment |
| Production deployment guides | planned | Docker, Helm, K8s runbooks |

Supporting tracks: plugin registry, examples, community templates, CI/CD hardening.

---

## Guiding principles

- **Core first** — small, stable, provider-agnostic engine.
- **Plugins for everything else** — providers, storage, AI, integrations.
- **SDK consistency** — same concepts in every language.
- **DX is product** — docs, TestKit, benchmarks, examples.
- **Open governance** — versioned APIs and automated compatibility checks.
- **Compliance** — official/permitted access only; no ToS bypass.
