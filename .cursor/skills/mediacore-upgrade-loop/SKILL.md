---
name: mediacore-upgrade-loop
description: >-
  Auto-upgrade MediaCore catalog stubs into working providers in batches.
  Use when the user asks to implement all platforms, continue the upgrade loop,
  process the provider queue, or research a platform against yt-dlp for hosts only.
---

# MediaCore provider upgrade loop

Upgrade catalog stubs **one batch at a time** into working `providers/<name>/` packages.

## Hard rules (never violate)

1. **No scrapers.** Do not port yt-dlp / third-party extractor download or HTML scrape logic.
2. **No access-control bypass.** Working metadata/download only via official or clearly permitted public APIs (oEmbed, documented REST, licensed SDKs).
3. **yt-dlp is research-only** for `_VALID_URL` / host patterns / IE names — never copy extract methods into MediaCore.
4. Brand stays **MediaCore** only.

If no permitted API exists → improve host detection on the stub (or leave stub) and mark the queue item `skipped_no_api`. Do **not** invent a scraper.

## When to use

- User: “implement all platforms”, “next batch”, “continue upgrade”, “auto implement”
- After a batch finishes and user says continue

## Loop (each agent turn)

```bash
# 1) See next candidates
uv run python scripts/provider_upgrade_queue.py next --limit 5

# 2) After implementing a batch
uv run python scripts/provider_upgrade_queue.py mark --names a,b,c --status done
# or: --status skipped_no_api --note "no public oEmbed/API"

# 3) Refresh docs statuses + tests
# (update DOCS_WORKING_STATUS in scripts/generate_providers.py)
uv run python scripts/generate_providers.py
uv run pytest -m provider -q --benchmark-disable
```

Default batch size: **5** platforms.

## Decision tree per platform

```
Has public oEmbed?     → metadata_only provider via providers/oembed.py
Has official public API? → metadata_only (or active if download is permitted)
Only hosts known?      → ensure hosts in hosts.py / stub; status stays not_configured
Nothing permitted?     → skipped_no_api; do not scrape
```

### Research (when unsure)

Use yt-dlp **source listing** only for hosts / URL shape:

- Tree: https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp/extractor
- Extractor registry: https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/_extractors.py
- Per-site file: `https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/<module>.py`

From that file, read only:

- `IE_NAME` / class name
- `_VALID_URL` (host suffixes, path patterns)
- Comments mentioning official API / oEmbed

**Do not** copy `_real_extract`, download URL decryption, or player parsing.

Also search the open web for `{platform} oEmbed` / `{platform} public API`.

Known oEmbed hints live in `scripts/provider_upgrade_queue.py` (`KNOWN_OEMBED`).

## Implement checklist (working provider)

1. Create `providers/<name>/__init__.py` + `provider.py` (same `name` as catalog entry).
2. Prefer `fetch_oembed` / `metadata_from_oembed` from [`providers/oembed.py`](../../../providers/oembed.py).
3. Register early in [`packages/registry/providers.py`](../../../packages/registry/providers.py) before factory stubs.
4. Add mocked contract test in `tests/providers/test_provider_contract.py`.
5. Update stub docstring under `providers/stubs/<slug>/` → points at working module.
6. Add name → `metadata_only` in `DOCS_WORKING_STATUS` in `scripts/generate_providers.py`.
7. Update `docs/platforms/index.md`, `docs/plugins/providers.md`, and `WORKING` in `docs/.vitepress/theme/components/PlatformCatalog.vue`.
8. `uv run python scripts/generate_providers.py` then provider pytest.
9. Queue: `mark --status done`.

## Host-only upgrade (no API)

1. Add/fix hosts in `providers/platforms/hosts.py`.
2. `uv run python scripts/sync_platform_catalog.py --offline`.
3. Queue: `mark --status hosts_only`.

## See also

- [reference.md](reference.md)
- Skill `mediacore-provider` for single-provider details
- Skill `mediacore-catalog` for sync/regenerate
