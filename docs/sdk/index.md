---
outline: deep
---

<DocHero
  title="MediaCore SDKs"
  lead="One command from the repo — talk to /v1 with the same media, jobs, and plugins surface in every language."
>
  <SdkHeroActions />
</DocHero>

## Quick start

Install a client from the monorepo (registry publish / deploy comes later). Run these from the **repository root**.

### JavaScript / TypeScript

::: code-group

```bash [npm]
npm install ./sdk/javascript
# TypeScript:
npm install ./sdk/typescript
```

```bash [pnpm]
pnpm add ./sdk/javascript
# TypeScript:
pnpm add ./sdk/typescript
```

```bash [yarn]
yarn add ./sdk/javascript
# TypeScript:
yarn add ./sdk/typescript
```

```bash [bun]
bun add ./sdk/javascript
# TypeScript:
bun add ./sdk/typescript
```

:::

```js
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
```

::: tip Path install
Use the local `./sdk/...` path until packages are published. Prefer a fresh install from the repo checkout so you do not pick up a stale cached package name.
:::

### Python

::: code-group

```bash [uv]
# From MediaCore repo root — sdk on PYTHONPATH
export PYTHONPATH=sdk/python:$PYTHONPATH
uv run python -c "from mediacore_sdk import MediaCore; print(MediaCore)"
```

```bash [pip]
export PYTHONPATH=sdk/python:$PYTHONPATH
python -c "from mediacore_sdk import MediaCore; print(MediaCore)"
```

:::

```python
from mediacore_sdk import MediaCore

client = MediaCore("dev-api-key-change-me")
meta = client.media.analyze("https://example.com/video.mp4")
```

### Other languages

| Language | Install (from repo root) |
|----------|--------------------------|
| [Go](./go) | `go get ./sdk/go` |
| [Rust](./rust) | `cargo add --path sdk/rust` |
| [Dart](./dart) | `dart pub add --path sdk/dart` |
| [C#](./csharp) | Project reference → `sdk/csharp` |
| [Java](./java) / [Swift](./swift) / [Kotlin](./kotlin) | Stub scaffolds — not ready yet |

Full per-language guides below.

<SdkFeatures />

## Languages {#languages}

Pick a client tile for install details and examples.

<SdkCatalog />

## Unified API

```text
client.media.analyze(url)
client.media.download(url, format?)
client.media.convert(path|url, options?)
client.media.thumbnail(url)

client.jobs.list()
client.jobs.get(id)

client.plugins.list()
```

Language-idiomatic naming is fine (`AnalyzeAsync` in C#, `Media.Analyze` in Go) as long as namespaces stay `media` / `jobs` / `plugins`.

## REST mapping

| SDK method | HTTP |
|------------|------|
| `media.analyze` | `POST /v1/analyze` |
| `media.download` | `POST /v1/download` |
| `media.convert` | `POST /v1/convert` |
| `media.thumbnail` | `POST /v1/thumbnail` |
| `jobs.list` | `GET /v1/jobs` |
| `jobs.get` | `GET /v1/jobs/{id}` |
| `plugins.list` | `GET /v1/plugins` |

Full HTTP reference: [API](/api/).

## Deploy later

Publishing to npm, PyPI, crates.io, and friends is **not** part of this page yet. Until then:

1. Install from the git checkout paths above.
2. Point `baseUrl` at your MediaCore API (`http://localhost:8000` by default).
3. Use `X-API-Key` / the constructor API key argument.

## Language guides

| SDK | Status | Package |
|-----|--------|---------|
| [JavaScript](./javascript) | Ready | `@mediacore/sdk` |
| [TypeScript](./typescript) | Ready | `@mediacore/sdk-ts` |
| [Python](./python) | Ready | `mediacore_sdk` |
| [Go](./go) | Ready | `mediacore` |
| [Rust](./rust) | Ready | `mediacore_sdk` |
| [Dart](./dart) | Ready | `mediacore` |
| [C#](./csharp) | Ready | `MediaCore` |
| [Java](./java) | Stub | `io.mediacore` |
| [Swift](./swift) | Stub | `MediaCore` |
| [Kotlin](./kotlin) | Stub | `io.mediacore` |
