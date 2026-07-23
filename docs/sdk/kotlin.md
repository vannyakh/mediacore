# Kotlin SDK

**Status:** Stub · **Package:** `io.mediacore` · **Path:** `sdk/kotlin`

Scaffold for Android / JVM. Not implemented yet — contributions welcome under `sdk/kotlin/`.

## Planned surface

| Method | HTTP |
|--------|------|
| `client.media.analyze(url)` | `POST /v1/analyze` |
| `client.media.download(url, format)` | `POST /v1/download` |
| `client.media.convert(path)` | `POST /v1/convert` |
| `client.media.thumbnail(url)` | `POST /v1/thumbnail` |
| `client.jobs.list()` | `GET /v1/jobs` |
| `client.plugins.list()` | `GET /v1/plugins` |

## Planned example

```kotlin
val client = MediaCore("api-key")
client.media.analyze(url)
client.media.download(url, "original")
client.media.convert(path)
client.media.thumbnail(url)
client.jobs.list()
client.plugins.list()
```

Entry: `src/main/kotlin/io/mediacore/MediaCore.kt`.

## See also

- [Java SDK](./java) (also stub)
- [SDK overview](./)
- [REST API](/api/)
