# Contributing to MediaCore

Thanks for helping build **The Open Source Media Infrastructure Platform**.

## Ways to contribute

- Bug fixes and features
- Providers and plugins
- Documentation and examples
- Tests, benchmarks, and translations

## Development setup

```bash
cp .env.example .env
uv sync --extra dev
export SYNC_DOWNLOAD=true USE_SQLITE=true
uv run uvicorn apps.api.main:app --reload --port 8000
uv run pytest -m "not load and not stress and not chaos and not benchmark"
```

CLI smoke:

```bash
uv run mediacore doctor
uv run mediacore analyze https://example.com/video.mp4
```

## Project rules

1. **Brand:** MediaCore only in code, docs, logs, and package names.
2. **No access-control bypass** / scraper-based platform extractors.
3. **Core stays provider-agnostic** — platform logic belongs in `providers/` or plugins.
4. Prefer official or user-permitted APIs for working providers.
5. Follow existing layout: `apps/`, `packages/`, `providers/`, `plugins/`, `sdk/`, `docs/`.

## Docs

Keep [README.md](README.md) short (onboarding). Put deep material under [`docs/`](docs/) (VitePress).

```bash
cd docs && npm install && npm run dev
```

## Pull requests

- Prefer focused PRs with tests for behavior changes.
- Run `uv run ruff check .` and the PR pytest marker suite before submitting.
- Do not commit secrets (`.env`, credentials).

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security

See [SECURITY.md](SECURITY.md) — please do not open public issues for vulnerabilities.
