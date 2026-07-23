# Providers

MediaCore core never hardcodes platform logic. Built-ins under `providers/`:

| Provider | Role |
|----------|------|
| `generic` | Direct media HTTP(S) URLs |
| `filesystem` | `file://` and local paths |
| `vimeo` | Public oEmbed metadata |
| `example` | `mediacore://example/...` demo |

## Adding a provider

1. Create `providers/<name>/provider.py`
2. Implement `packages.core.provider.Provider`
3. Register the module in `packages/registry/providers.py`

Community providers should eventually live in separate repos/crates implementing the same interface — keep the core stable.
