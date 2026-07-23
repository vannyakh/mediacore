# TypeScript SDK

**Status:** Ready · **Package:** `@mediacore/sdk-ts` · **Path:** `sdk/typescript`

Typed client (`src/client.ts`) with the same surface as JavaScript.

## Install

```bash
npm install ./sdk/typescript
```

```ts
import { MediaCore } from "@mediacore/sdk-ts";
// or local:
import { MediaCore } from "./src/client.js";
```

## Runtime

- TypeScript 5+ / Node 18+
- Types ship from `src/client.ts`
- Auth: `X-API-Key`

## Surface

| Method | HTTP |
|--------|------|
| `client.media.analyze(url)` | `POST /v1/analyze` |
| `client.media.download(url, format?)` | `POST /v1/download` |
| `client.media.convert(path, options?)` | `POST /v1/convert` |
| `client.media.thumbnail(url)` | `POST /v1/thumbnail` |
| `client.jobs.list(limit?)` | `GET /v1/jobs` |
| `client.jobs.get(id)` | `GET /v1/jobs/{id}` |
| `client.plugins.list()` | `GET /v1/plugins` |

## Example

```ts
import { MediaCore } from "./src/client.js";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url!, meta.formats[0].id);
await client.jobs.list();
await client.plugins.list();
```

## See also

- [JavaScript SDK](./javascript)
- [REST API](/api/)
- [SDK overview](./)
