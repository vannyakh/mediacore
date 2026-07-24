# Provider reference

## Registry resolve order

1. Working providers registered early in `packages/registry/providers.py` (filesystem, oEmbed batch, …)
2. All catalog platform modules (`build_all_providers()`), skipping names already registered
3. `generic`, `example`

## Key paths

| Path | Role |
|------|------|
| `packages/core/provider.py` | Interface |
| `providers/base_module.py` | PlatformModule (direct media + not_configured pages) |
| `providers/direct_media.py` | Shared direct metadata/download |
| `providers/platforms/hosts.py` | Curated hosts |
| `providers/platforms/factory.py` | Load index → modules |
| `providers/modules/<slug>/` | On-disk catalog packages |
| `providers/data/providers_index.json` | Generated index |
| `packages/registry/providers.py` | Registration |

## API

- `GET /v1/providers`
- `GET /v1/providers/catalog`
- `GET /v1/providers/catalog/search?q=`
