# Catalog provider stubs

One folder per platform from `providers/data/providers_index.json`.

- Status is `not_configured` (or `broken`) until you implement permitted/official access.
- Runtime still loads stubs via `providers.platforms.factory` (fast).
- To upgrade a platform: edit `providers/stubs/<slug>/provider.py` and register it early in `packages/registry/providers.py`.

Regenerate:

```bash
uv run python scripts/sync_platform_catalog.py --offline
uv run python scripts/materialize_catalog_providers.py
```
