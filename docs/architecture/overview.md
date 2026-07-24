---
title: Architecture overview
---

<script setup>
const links = [
  { title: "Plugins", href: "/plugins/", hint: "Capabilities", icon: "https://cdn.simpleicons.org/npm/CB3837" },
  { title: "Platforms", href: "/platforms/", hint: "Providers", icon: "https://cdn.simpleicons.org/youtube/FF0000" },
  { title: "API events", href: "/api/", hint: "SSE & history", icon: "https://cdn.simpleicons.org/fastapi/009688" },
  { title: "Deploy", href: "/deployment/", hint: "Local → K8s", icon: "https://cdn.simpleicons.org/kubernetes/326CE5" },
]
</script>

<DocHero
  eyebrow="Deep dive"
  title="Architecture overview"
  lead="Layout, engine vs runtime, request flow, and the event bus that ties jobs together."
/>

## Vision

**The Open Media Infrastructure Platform** — Extract • Process • Automate • Deliver.

```mermaid
flowchart LR
  MediaCore --> PluginSystem[Plugin_System]
  PluginSystem --> Providers
  Providers --> MediaPipeline[Media_Pipeline]
  MediaPipeline --> SDK
  SDK --> Application
```

Full product story: [Vision](/getting-started/vision).

## Layout

Full path table: [Repository layout](./layout).

```text
apps/        api · worker · cli · dashboard · scheduler · desktop · studio · gateway
packages/    core · engine · registry · queue · storage · events · plugins · …
providers/   <name>/ working  ·  modules/ catalog  ·  platforms/ hosts
plugins/     ffmpeg · whisper · storage-* · webhook · …
sdk/ · docs/ · tests/ · scripts/ · docker/ · helm/ · benchmarks/ · crates/ · mediacore/
```

Legacy roots removed: `extractor/`, top-level `ffmpeg/` / `storage/` / `queue/` / `jobqueue/`.

Contributor map: [MediaCore vs yt-dlp](./mediacore-vs-ytdlp) · [`providers/README.md`](../../providers/README.md).

## Engine vs runtime

| Layer | Responsibility |
|-------|----------------|
| **Engine** | Generic: URL, HTTP, cache, queue, pipeline, jobs, events, config, storage interface, plugins, scheduler, logging, metrics, security, telemetry |
| **Runtime** | Execute jobs: Queue → Worker → Pipeline → Events (local, Docker, K8s, server, desktop, embedded) |

No platform-specific code in the engine.

## Core principles

1. **Core first** — small, stable, provider-agnostic.
2. **Plugins for everything else** — storage, AI, auth, notifications, integrations.
3. **Same pipeline everywhere** — API, CLI, Desktop, Studio share jobs and events.
4. **SDK consistency** — same concepts across languages.
5. **Deployment modes** — CLI, desktop, docker, k8s, embedded, local-only.

## Request flow

```mermaid
flowchart TD
  Client[SDK_CLI_Dashboard] --> API[apps_api]
  API --> Engine[packages_engine]
  Engine --> Registry[packages_registry]
  Registry --> Provider[providers_*]
  API --> Queue[packages_queue]
  Queue --> Worker[apps_worker]
  Worker --> Engine
  Worker --> PluginRuntime[packages_plugins_runtime]
  PluginRuntime --> Storage[packages_storage]
  PluginRuntime --> Media[packages_media]
  Engine --> Events[packages_events]
  Events --> PluginRuntime
  API --> Plugins[packages_plugins]
```

## Events

`JobCreated` → `AnalyzeStarted` → `MetadataReady` → `DownloadStarted` → `Progress` → `ProcessingStarted` → `Completed` | `Failed` | `Cancelled`

### Envelope

```json
{
  "type": "Progress",
  "payload": { "job_id": "…", "percent": 42 },
  "at": "2026-07-23T12:00:00+00:00"
}
```

### Fan-out

- In-process `EventBus`
- Redis channel `mediacore:events` when `EVENTS_REDIS_ENABLED`
- `GET /v1/events` · `GET /v1/events/stream` · webhook / bot plugins

## Continue

<DocLinks :items="links" />
