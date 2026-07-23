# Upgrade loop reference

## Queue file

`providers/data/upgrade_backlog.json` — generated/updated by `scripts/provider_upgrade_queue.py`.

Statuses:

| Status | Meaning |
|--------|---------|
| `pending` | Not started |
| `done` | Working provider registered |
| `hosts_only` | Host detection improved; still stub |
| `skipped_no_api` | No permitted API found |
| `blocked` | Needs credentials / human decision |

## Already working (skip)

Parsed from early registration in `packages/registry/providers.py` plus builtins:

`filesystem`, `generic`, `example`, `vimeo`, and every module listed before catalog stubs.

## yt-dlp research cheat sheet

| Need | Where |
|------|--------|
| List of IE modules | `yt_dlp/extractor/_extractors.py` |
| URL hosts | `_VALID_URL` regex in `yt_dlp/extractor/<site>.py` |
| IE id | `IE_NAME` or class `FooIE` → often `Foo` |

Example raw URL pattern:

```
https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/dailymotion.py
```

Extract host suffixes into MediaCore `supports()` / `hosts.py` only.

## oEmbed provider template

Mirror `providers/dailymotion/provider.py`:

- `status = "metadata_only"`
- `capabilities`: metadata/manifest/formats/thumbnail true; download false
- `download` → `ProviderNotConfiguredError`

## Docs UI

After each batch:

1. `DOCS_WORKING_STATUS` in `scripts/generate_providers.py`
2. `WORKING` array in `PlatformCatalog.vue`
3. Tables in `docs/platforms/index.md` + `docs/plugins/providers.md`
4. Regenerate `docs/public/platforms.json`
