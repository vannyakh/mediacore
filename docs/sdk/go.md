# Go SDK

**Status:** Ready · **Package:** `mediacore` · **Path:** `sdk/go`

Idiomatic Go client with exported `Media`, `Jobs`, and `Plugins` namespaces.

## Install

```bash
# From a module that vendors or replaces the path
go get ./sdk/go
```

```go
import mediacore "path/to/sdk/go"

client := mediacore.New("dev-api-key-change-me")
```

## Runtime

- Go 1.22+
- Stdlib `net/http` (60s timeout by default)
- Constructor: `mediacore.New(apiKey, optionalBaseURL...)`

## Surface

| Method | HTTP |
|--------|------|
| `client.Media.Analyze(url)` | `POST /v1/analyze` |
| `client.Media.Download(url, format)` | `POST /v1/download` |
| `client.Media.Convert(path, options)` | `POST /v1/convert` |
| `client.Media.Thumbnail(url)` | `POST /v1/thumbnail` |
| `client.Jobs.List(limit)` | `GET /v1/jobs` |
| `client.Jobs.Get(id)` | `GET /v1/jobs/{id}` |
| `client.Plugins.List()` | `GET /v1/plugins` |

## Example

```go
client := mediacore.New("dev-api-key-change-me")
meta, err := client.Media.Analyze("https://example.com/video.mp4")
if err != nil {
    panic(err)
}
job, _ := client.Media.Download("https://example.com/video.mp4", "original")
_, _ = client.Media.Convert("/tmp/out.mp4", map[string]any{"container": "webm"})
_, _ = client.Media.Thumbnail("https://example.com/video.mp4")
jobs, _ := client.Jobs.List(50)
plugins, _ := client.Plugins.List()
_, _, _, _ = meta, job, jobs, plugins
```

## See also

- [REST API](/api/)
- [SDK overview](./)
