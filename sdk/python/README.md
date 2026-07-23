# Python SDK

```python
from apidownloader_sdk import VideoExtractor

api = VideoExtractor("dev-api-key-change-me")
info = api.analyze("https://example.com/video.mp4")
job = api.download("https://example.com/video.mp4", info["formats"][0]["id"])
status = api.job(job["job_id"])
```

Add `sdk/python` to `PYTHONPATH` or install locally during development.
