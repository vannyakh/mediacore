# MediaCore C# SDK

```csharp
var client = new MediaCore("dev-api-key-change-me");
var meta = await client.Media.AnalyzeAsync("https://example.com/video.mp4");
var job = await client.Media.DownloadAsync("https://example.com/video.mp4");
await client.Media.ConvertAsync("/tmp/out.mp4");
await client.Media.ThumbnailAsync("https://example.com/video.mp4");
var jobs = await client.Jobs.ListAsync();
var plugins = await client.Plugins.ListAsync();
```

`MediaCoreClient` remains as a compatibility alias. See [docs/sdk/](../../docs/sdk/).
