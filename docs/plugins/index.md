# MediaCore Plugins

MediaCore itself stays small. Capabilities beyond the core pipeline come from plugins under `plugins/`.

## Naming

```text
mediacore-plugin-<area>[-<impl>]
```

Examples: `mediacore-plugin-storage-local`, `mediacore-plugin-storage-gdrive`, `mediacore-plugin-telegram`, `mediacore-plugin-whisper`, `mediacore-plugin-translate`.

## Kinds

| Kind | Purpose |
|------|---------|
| `metadata` | Enrich / normalize media metadata |
| `provider` | Optional bridge to platform extractors (see below) |
| `storage` | Persist job outputs ([storage](./storage)) |
| `authentication` | Auth adapters |
| `ai` | Speech-to-text and related AI |
| `ffmpeg` | Convert, audio, thumbnail, clip |
| `translation` | Subtitle / text translation |
| `notifications` | Telegram, Discord, etc. |
| `analytics` | Usage / job metrics sinks |
| `webhooks` | HTTP event forwarding |

## Providers vs plugins

Platform extractors live under `providers/` and are registered via `packages/registry`. They are **not** migrated into `plugins/`.

Kind `provider` exists for optional `mediacore-plugin-provider-*` wrappers later. The stub `mediacore-plugin-provider` documents that boundary.

## Manifest

Each plugin directory contains `plugin.py` with a `PLUGIN` dict:

```python
PLUGIN = {
    "name": "mediacore-plugin-storage-local",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Local filesystem storage for MediaCore jobs",
    "status": "available",  # available | stub | disabled | error
    "capabilities": ["store", "delete", "public_url"],
}
```

Optional runtime hooks in the same module:

- `create(settings, *, root=None)` — factory for a handler (`storage`, etc.)
- `on_event(event)` — receive job lifecycle events (`notifications` / `webhooks`)

## Runtime

`packages.plugins.runtime` resolves capabilities:

- `get_storage()` — default **local**; cloud only when `STORAGE_BACKEND` is set ([storage](./storage))
- `ensure_ffmpeg()` — requires `mediacore-plugin-ffmpeg` plus the `ffmpeg` binary
- `dispatch_event(event)` — called from the event bus for notification/webhook plugins that define `on_event`

Discovery: `PluginLoader` scans `plugins/*/plugin.py`. List via `GET /v1/plugins` or `mediacore plugin list`.

## Storage plugins

Local · Google Drive · S3 · Cloudflare R2 · Azure Blob · Dropbox · OneDrive · FTP · WebDAV

Storage is **optional**. Local-only workflows never require cloud credentials. See [storage](./storage).

## Add a plugin

1. Create `plugins/<name>/plugin.py` with a valid `PLUGIN` kind.
2. Use `status: "stub"` until the implementation is ready.
3. Optionally add `on_event` / `create`.
4. Run `uv run pytest -m plugin`.

Local install: `mediacore plugin install NAME|PATH` (copy + validate manifest). Remote marketplace remains on the roadmap.
