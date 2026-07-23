# Java SDK

**Status:** Stub · **Package:** `io.mediacore` · **Path:** `sdk/java`

Scaffold only — not a working HTTP client yet. Contributions welcome under `sdk/java/`.

## Planned install

Maven / Gradle coordinates TBD. Entry stub:

`sdk/java/src/main/java/io/mediacore/MediaCore.java`

## Planned surface

| Method | HTTP |
|--------|------|
| `client.media().analyze(url)` | `POST /v1/analyze` |
| `client.media().download(url, format)` | `POST /v1/download` |
| `client.media().convert(path, options)` | `POST /v1/convert` |
| `client.media().thumbnail(url)` | `POST /v1/thumbnail` |
| `client.jobs().list()` | `GET /v1/jobs` |
| `client.plugins().list()` | `GET /v1/plugins` |

## Planned example

```java
var client = new MediaCore("api-key");
client.media().analyze(url);
client.media().download(url, "original");
client.media().convert(path, options);
client.media().thumbnail(url);
client.jobs().list();
client.plugins().list();
```

## See also

- [Kotlin SDK](./kotlin) (also stub)
- [SDK overview](./)
- [REST API](/api/)
