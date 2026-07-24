---
name: mediacore-catalog
description: >-
  Sync and regenerate the MediaCore platform provider catalog from sites_snapshot
  and hosts maps. Use when updating providers_index.json, extractors.json,
  sync_platform_catalog, or generate_providers scripts.
---

# MediaCore Catalog Skill

## Offline regenerate (default)

```bash
uv run python scripts/sync_platform_catalog.py --offline
```

This runs `scripts/generate_providers.py` against `providers/data/sites_snapshot.json`.

## Refresh snapshot from a file

```bash
uv run python scripts/sync_platform_catalog.py --file ./sites.md
```

## Outputs

| File | Purpose |
|------|---------|
| `providers/data/sites_snapshot.json` | Snapshot input |
| `providers/data/extractors.json` | Clean extractor list |
| `providers/data/providers_index.json` | Platform module index |
| `docs/public/platforms.json` | Docs `/platforms/` full list UI |
| `docs/public/plugins.json` | Docs `/plugins/` catalog UI (`scripts/generate_plugins_docs.py`) |
| `providers/modules/<slug>/` | On-disk platform module per catalog entry |
| `providers/modules/_manifest.json` | Slug → module map |
| `providers/data/upgrade_backlog.json` | Auto-upgrade queue (`provider_upgrade_queue.py`) |

## After regenerate

1. Ensure filenames/docs stay MediaCore-branded (no foreign brand paths).
2. Run `uv run pytest -m provider -q`.
3. Spot-check `GET /v1/providers/catalog`.

## Do not

- Reintroduce foreign brand filenames (`*ytdlp*`, `*apidownloader*`).
- Add scraper runtimes as part of catalog sync.
