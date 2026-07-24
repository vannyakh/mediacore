# Platform modules

One folder per platform from `providers/data/providers_index.json`.

- **Direct media** URLs on a module's hosts: metadata + download via `PlatformModule`.
- **Page/watch** URLs: `not_configured` until you implement permitted/official access.
- Runtime loads modules via `providers.platforms.factory` (fast index).
- To upgrade a platform: edit `providers/modules/<slug>/provider.py` (or add
  `providers/<name>/`) and register early in `packages/registry/providers.py`.

Regenerate:

```bash
uv run python scripts/sync_platform_catalog.py --offline
uv run python scripts/materialize_catalog_providers.py
```
