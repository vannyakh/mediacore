---
name: mediacore-provider
description: >-
  Add or upgrade a MediaCore media provider (working implementation or catalog stub).
  Use when creating providers, editing providers/, hosts maps, registry registration,
  or enabling platform metadata/download with permitted APIs.
---

# MediaCore Provider Skill

## Architecture

```
Provider
├── Metadata   → metadata(url) → MediaMetadata
├── Manifest   → manifest(url) → Manifest
├── Formats    → formats(url) → list[FormatInfo]
├── Download   → download(url, format_id, dest) → DownloadResult
├── Thumbnail  → thumbnail(url) → ThumbnailInfo | None
├── Subtitle   → subtitles(url) → list[SubtitleTrack]
└── Live       → live(url) → LiveInfo | None
```

Declare `capabilities = ProviderCapabilities(...)` for the stages you support.

## When adding a working provider

1. Create `providers/<name>/provider.py` implementing `packages.core.provider.Provider`.
2. Register the module **early** in `packages/registry/providers.py` (before catalog stubs).
3. Add host suffixes / URL rules; keep scrape-free / ToS-safe.
4. Add contract tests with `packages.testkit.contracts.run_provider_contract`.
5. Run `uv run pytest -m provider -q`.

## When adding host detection for a stub

1. Edit `providers/platforms/hosts.py` (`MAJOR_PLATFORMS`).
2. Regenerate: `uv run python scripts/generate_providers.py` (or `sync_platform_catalog.py --offline`).
3. Confirm `supports()` via registry resolve in a unit test.

## Stub pattern

```python
from providers.base_stub import StubProvider

class MyProvider(StubProvider):
    name = "myplatform"
    host_suffixes = ("myplatform.com", "www.myplatform.com")
```

Catalog stubs use `status="not_configured"` and raise `ProviderNotConfiguredError` until permitted access is wired.

## Do not

- Add third-party scraper libraries to extract/download.
- Put platform-specific scrape logic in `packages/core`.

## See also

- [docs/plugins/providers.md](../../../docs/plugins/providers.md)
- [reference.md](reference.md)
- Skill `mediacore-upgrade-loop` — batch auto-upgrade + queue (`scripts/provider_upgrade_queue.py`)
