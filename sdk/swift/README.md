# MediaCore Swift SDK (future)

Planned surface:

```swift
let client = MediaCore(apiKey: "…")
try await client.media.analyze(url: url)
try await client.media.download(url: url, format: "original")
try await client.media.convert(path: path)
try await client.media.thumbnail(url: url)
try await client.jobs.list()
try await client.plugins.list()
```

Not implemented yet — contributions welcome under `sdk/swift/`.
