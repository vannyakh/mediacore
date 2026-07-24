---
title: Roadmap
---

<script setup>
const links = [
  { title: "Vision", href: "/getting-started/vision", hint: "North star", icon: "https://cdn.simpleicons.org/rocket/FF4438" },
  { title: "Benchmarks", href: "/benchmarks/", hint: "v1.0 targets", icon: "https://cdn.simpleicons.org/prometheus/E6522C" },
  { title: "Architecture", href: "/architecture/", hint: "How it ships", icon: "https://cdn.simpleicons.org/python/3776AB" },
  { title: "GitHub ROADMAP", href: "https://github.com/vannyakh/mediacore/blob/main/ROADMAP.md", hint: "Root summary", icon: "https://cdn.simpleicons.org/github/ffffff" },
]
const phases = [
  { value: "v0.1", label: "Foundation" },
  { value: "v0.2", label: "Surfaces" },
  { value: "v0.3", label: "Desktop" },
  { value: "v1.0", label: "Stable" },
]
</script>

<DocHero
  eyebrow="Plan"
  title="Roadmap"
  lead="v0.1 Foundation → v0.2 Platform surfaces → v0.3 Desktop & Studio → v1.0 Stable ecosystem."
/>

<DocStats :items="phases" />

Statuses: **done** · **partial** · **planned**

```mermaid
flowchart LR
  v01[v0.1_Foundation] --> v02[v0.2_Surfaces]
  v02 --> v03[v0.3_Desktop_Studio]
  v03 --> v10[v1.0_Stable]
```

## v0.1 — Foundation

| Item | Status | Notes |
|------|--------|-------|
| Engine | partial | Python `packages/engine`; Rust crate scaffold |
| Runtime | partial | Local workers; Docker/K8s expanding |
| CLI | done | `mediacore` |
| SDK | partial | Multi-language clients |
| Local storage | done | Default backend |
| TestKit | partial | Mocks, contracts, fixtures |

## v0.2 — Platform surfaces

| Item | Status | Notes |
|------|--------|-------|
| Dashboard | partial | Next.js + jobs/events |
| Event system | done | Bus, Redis, SSE, webhooks |
| Pipeline | partial | Analyze → download → process |
| Workers | done | Dramatiq |
| Plugin system | partial | Loader + storage/ffmpeg/webhook |
| REST API | done | `/v1/*` |
| Permitted providers | partial | Upgrade loop; Dropbox/Google Drive shared-file download; many `metadata_only` |
| CLI providers UX | done | `mediacore providers list\|search` + honest `not_configured` hints |

## v0.3 — Desktop, Studio & quality

| Item | Status | Notes |
|------|--------|-------|
| Desktop (Tauri) | planned | `apps/desktop` |
| Studio | planned | Visual workflows |
| Benchmark suite | partial | Python + Criterion |
| Marketplace | planned | Plugin discovery |

## v1.0 — Stable ecosystem

| Item | Status | Notes |
|------|--------|-------|
| Stable plugin API | planned | Versioned contracts |
| SDK compatibility | planned | Shared method names |
| Docs & deploy guides | planned | Site + runbooks |

## Principles

- Core first · Plugins for everything else · SDK consistency  
- DX is product · Open governance · Official/permitted access only  

## Related

<DocLinks :items="links" />
