# MediaCore Kotlin SDK (future)

Planned surface:

```kotlin
val client = MediaCore("api-key")
client.media.analyze(url)
client.media.download(url, "original")
client.media.convert(path)
client.media.thumbnail(url)
client.jobs.list()
client.plugins.list()
```

Not implemented yet — contributions welcome under `sdk/kotlin/`.
