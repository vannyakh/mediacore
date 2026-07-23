# JavaScript SDK

**Status:** Ready · **Package:** `@mediacore/sdk` · **Path:** `sdk/javascript`

Browser and Node client using native `fetch`. Same surface as TypeScript / Python.

## Install

```bash
npm install ./sdk/javascript
# or
pnpm add ./sdk/javascript
```

```js
import { MediaCore } from "@mediacore/sdk";
```

## Runtime

- Node 18+ or any modern browser with `fetch`
- Auth: `X-API-Key`
- Default base URL: `http://localhost:8000`

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

```js
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url, meta.formats[0].id);
await client.media.convert("/path/out.mp4", { container: "webm" });
await client.media.thumbnail(meta.url);
const jobs = await client.jobs.list();
const plugins = await client.plugins.list();
```

Constructor: `new MediaCore(apiKey, baseUrl?)`.

## See also

- [TypeScript SDK](./typescript)
- [REST API](/api/)
- [SDK overview](./)
