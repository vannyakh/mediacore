# MediaCore Python SDK

```python
from mediacore_sdk import MediaCore

client = MediaCore("dev-api-key-change-me")
meta = client.media.analyze("https://example.com/video.mp4")
job = client.media.download(meta["url"], meta["formats"][0]["id"])
client.media.convert("/tmp/out.mp4", container="webm")
client.media.thumbnail(meta["url"])
jobs = client.jobs.list()
plugins = client.plugins.list()
```

Add `sdk/python` to `PYTHONPATH` during development. See [docs/sdk/](../../docs/sdk/).
