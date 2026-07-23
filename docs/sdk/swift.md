# Swift SDK

**Status:** Stub · **Package:** `MediaCore` · **Path:** `sdk/swift`

Scaffold for Apple platforms. Not implemented yet — contributions welcome under `sdk/swift/`.

## Planned surface

| Method | HTTP |
|--------|------|
| `client.media.analyze(url:)` | `POST /v1/analyze` |
| `client.media.download(url:format:)` | `POST /v1/download` |
| `client.media.convert(path:)` | `POST /v1/convert` |
| `client.media.thumbnail(url:)` | `POST /v1/thumbnail` |
| `client.jobs.list()` | `GET /v1/jobs` |
| `client.plugins.list()` | `GET /v1/plugins` |

## Planned example

```swift
let client = MediaCore(apiKey: "…")
try await client.media.analyze(url: url)
try await client.media.download(url: url, format: "original")
try await client.media.convert(path: path)
try await client.media.thumbnail(url: url)
try await client.jobs.list()
try await client.plugins.list()
```

Entry: `Sources/MediaCore/MediaCore.swift`.

## See also

- [SDK overview](./)
- [REST API](/api/)
