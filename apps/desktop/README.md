# MediaCore Desktop

Tauri (Rust + React) desktop app.

## Events

The scaffold polls the shared MediaCore event API:

- `GET /v1/events` — recent lifecycle events
- `GET /v1/events/stream` — SSE live stream (CLI / future native client)

Envelope: `{ type, payload, at }` with types `JobCreated` → … → `Completed` | `Failed` | `Cancelled`.

Configure with `VITE_API_BASE` and `VITE_API_KEY`.

## Roadmap

Planned features: drag & drop, batch jobs, download queue, processing pipeline, plugin manager, optional local API server.

Scaffold only in v0.1 — targeted for roadmap v0.4.
