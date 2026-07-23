# Architecture

MediaCore is **The Open Source Media Infrastructure Platform** — Extract • Process • Automate • Deliver.

It is not a video downloader; it is reusable media infrastructure (engine, runtime, plugins, SDKs, Studio).

```text
                    MediaCore
        ┌────────────────────────────┐
        │            SDK             │
        └────────────┬───────────────┘
                     │
              REST / gRPC API
                     │
             MediaCore Runtime
                     │
       ┌─────────────┼─────────────┐
       │             │             │
    Pipeline      Worker       Scheduler
       │             │             │
       └─────────────┼─────────────┘
              Plugin System
       ┌─────────────┼─────────────┐
   Providers      Storage       AI Plugin
```

## Deep dive

- [Overview](./overview) — layout, engine vs runtime, events, request flow
- [Vision](/getting-started/vision) — product positioning
- [Plugins](/plugins/) — extension model
- [Deployment](/deployment/) — run modes

## Ecosystem

```text
Engine · Runtime · API · SDK · CLI · Dashboard · Desktop · Studio
Plugin Registry · Marketplace · Docs · Benchmark · TestKit
```
