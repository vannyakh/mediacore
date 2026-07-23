# MediaCore Go SDK

```go
client := mediacore.New("dev-api-key-change-me")
meta, _ := client.Media.Analyze("https://example.com/video.mp4")
job, _ := client.Media.Download("https://example.com/video.mp4", "original")
_, _ = client.Media.Convert("/tmp/out.mp4", map[string]any{"container": "webm"})
_, _ = client.Media.Thumbnail("https://example.com/video.mp4")
jobs, _ := client.Jobs.List(50)
plugins, _ := client.Plugins.List()
_ = meta
_ = job
_ = jobs
_ = plugins
```

See [docs/sdk/](../../docs/sdk/).
