# C# SDK

**Status:** Ready · **Package:** `MediaCore` · **Path:** `sdk/csharp`

Async .NET client. `MediaCoreClient` remains a compatibility alias.

## Install

NuGet publish comes later. For now, include the sources under `sdk/csharp` (e.g. `MediaCoreClient.cs`) in your .NET project:

::: code-group

```bash [files]
# Copy or link sdk/csharp/*.cs into your .NET project
ls ../sdk/csharp
```

```xml [csproj]
<ItemGroup>
  <Compile Include="..\sdk\csharp\*.cs" Link="MediaCore\%(Filename)%(Extension)" />
</ItemGroup>
```

:::

```csharp
using MediaCore; // or project namespace
```

::: tip
Path layout may vary — point at `sdk/csharp` in your MediaCore checkout until a NuGet package ships.
:::

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
