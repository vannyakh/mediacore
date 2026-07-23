# C# SDK

**Status:** Ready · **Package:** `MediaCore` · **Path:** `sdk/csharp`

Async .NET client. `MediaCoreClient` remains a compatibility alias.

## Install

Add a project or file reference to `sdk/csharp` (e.g. `MediaCoreClient.cs`).

```csharp
using MediaCore; // or project namespace
```

## Runtime

- .NET 8+
- Async / await surface (`*Async` methods)
- Auth: `X-API-Key`

## Surface

| Method | HTTP |
|--------|------|
| `client.Media.AnalyzeAsync(url)` | `POST /v1/analyze` |
| `client.Media.DownloadAsync(url, format?)` | `POST /v1/download` |
| `client.Media.ConvertAsync(path, options?)` | `POST /v1/convert` |
| `client.Media.ThumbnailAsync(url)` | `POST /v1/thumbnail` |
| `client.Jobs.ListAsync()` | `GET /v1/jobs` |
| `client.Jobs.GetAsync(id)` | `GET /v1/jobs/{id}` |
| `client.Plugins.ListAsync()` | `GET /v1/plugins` |

## Example

```csharp
var client = new MediaCore("dev-api-key-change-me");
var meta = await client.Media.AnalyzeAsync("https://example.com/video.mp4");
var job = await client.Media.DownloadAsync("https://example.com/video.mp4");
await client.Media.ConvertAsync("/tmp/out.mp4");
await client.Media.ThumbnailAsync("https://example.com/video.mp4");
var jobs = await client.Jobs.ListAsync();
var plugins = await client.Plugins.ListAsync();
```

## See also

- [REST API](/api/)
- [SDK overview](./)
