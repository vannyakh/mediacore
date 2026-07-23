# Open Source Roadmap

### v0.1 — Foundation (current Python scaffold)

- Core packages (pipeline, events, plugin loader, registry)
- REST API `/v1`
- Job system + workers
- CLI + local storage
- Dashboard scaffold
- Built-in providers: generic, filesystem, example, vimeo (metadata)
- Testing platform: layered `tests/`, `packages/testkit`, PR CI

### v0.2 — Media Pipeline

- Full FFmpeg plugin
- Thumbnail / audio / convert / clip hardening
- Progress events
- Raise core coverage toward ≥95%; expand storage/provider contracts

### v0.3 — SDKs

- TypeScript, Python, Go, Rust, Dart (unified client surface)

### v0.4 — Desktop & Studio

- Tauri desktop
- Visual workflow editor (React Flow)

### v0.5 — Ecosystem

- Plugin registry / marketplace
- Docs site, examples, Helm
- Nightly load/chaos/benchmark gates + dashboard history
- Rust engine (`crates/mediacore-engine`) production path + Criterion benches
