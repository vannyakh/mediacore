# MediaCore SDKs

Every official SDK exposes the **same surface** against the REST API (`X-API-Key`).

## Unified API

```text
client.media.analyze(url)
client.media.download(url, format?)
client.media.convert(path|url, options?)
client.media.thumbnail(url)

client.jobs.list()
client.jobs.get(id)          # convenience; not required for parity checklist

client.plugins.list()
```

Language-idiomatic naming is allowed (`AnalyzeAsync` in C#, `analyze` in JS) as long as the namespace layout stays `media` / `jobs` / `plugins`.

## Supported

| SDK | Path | Status |
|-----|------|--------|
| JavaScript | `sdk/javascript` | Ready |
| TypeScript | `sdk/typescript` | Ready |
| Python | `sdk/python` | Ready |
| Rust | `sdk/rust` | Ready |
| Go | `sdk/go` | Ready |
| Dart | `sdk/dart` | Ready |
| C# | `sdk/csharp` | Ready |
| Java | `sdk/java` | Future stub |
| Swift | `sdk/swift` | Future stub |
| Kotlin | `sdk/kotlin` | Future stub |

## Example (Python)

```python
from mediacore_sdk import MediaCore

client = MediaCore("dev-api-key-change-me")
meta = client.media.analyze("https://example.com/video.mp4")
job = client.media.download(meta["url"], meta["formats"][0]["id"])
jobs = client.jobs.list()
plugins = client.plugins.list()
```

## Example (JavaScript)

```js
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url, meta.formats[0].id);
const jobs = await client.jobs.list();
const plugins = await client.plugins.list();
```

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
