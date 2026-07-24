# Available platforms

MediaCore **never hardcodes scrape logic in core**. Platforms live under `providers/` and are resolved by the registry. The table below lists the **full catalog** (search + filter).

```mermaid
flowchart LR
  URL[Media_URL] --> Registry[ProviderRegistry]
  Registry --> Working[Working_builtins]
  Registry --> Modules[Platform_modules]
  Working --> Engine[packages_engine]
  Modules -->|direct_media| Engine
  Modules -->|page_url_not_configured| Engine
```

<PlatformCatalog />

## Catalog at runtime

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/providers` | Working + platform modules (with capabilities) |
| `GET /v1/providers/catalog` | Catalog summary counts |
| `GET /v1/providers/catalog/search?q=` | Search extractors by name |

```bash
curl -s -H "X-API-Key: dev-api-key-change-me" \
  http://localhost:8000/v1/providers | head

curl -s -H "X-API-Key: dev-api-key-change-me" \
  "http://localhost:8000/v1/providers/catalog/search?q=youtube"
```

Regenerate modules (`providers/modules/<slug>/`) and docs list:

```bash
uv run python scripts/sync_platform_catalog.py --offline
# also writes providers/modules/_manifest.json (~1360 module folders)
```

## Working builtins (metadata / download)

| Provider | Status | Access |
|----------|--------|--------|
| `filesystem` | `active` | Local `file://` paths |
| `generic` | `active` | Direct HTTP(S) media URLs |
| `example` | `example` | Demo `mediacore://` URLs |
| `vimeo` | `metadata_only` | Public oEmbed |
| `dailymotion` | `metadata_only` | Public oEmbed |
| `soundcloud` | `metadata_only` | Public oEmbed |
| `reddit` | `metadata_only` | Public oEmbed |
| `ted` | `metadata_only` | Public oEmbed |
| `wikimedia.org` | `metadata_only` | MediaWiki REST summary API |
| `bandcamp` | `metadata_only` | Public oEmbed |
| `mixcloud` | `metadata_only` | Public oEmbed |
| `streamable` | `metadata_only` | Public oEmbed |
| `imgur` | `metadata_only` | Public oEmbed |
| `archiveorg` | `metadata_only` | Public oEmbed |

Catalog modules with the same `name` are skipped when these working providers register first.

## Status meanings

| Status | Meaning |
|--------|---------|
| `available` / `active` | Safe to use in local/dev workflows |
| `metadata` / `metadata_only` | Metadata only (no download of page URLs) |
| `not_configured` | Catalog module — direct media OK; page URLs need official APIs |

## Next

- [Register an extractor](./register)
- [Providers vs plugins](/plugins/providers)
- [Compliance](/plugins/providers#compliance)
