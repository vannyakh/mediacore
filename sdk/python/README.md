# MediaCore Python SDK

Thin client for the MediaCore permitted download API.

## Install

```bash
# from repo root
pip install -e sdk/python
# or
uv pip install -e sdk/python
```

## Usage

```python
from mediacore_sdk import MediaCore

with MediaCore("dev-api-key-change-me", base_url="http://localhost:8000") as client:
    meta = client.media.analyze("https://example.com/video.mp4")
    job = client.media.download(meta["url"], format="original")
    done = client.jobs.wait(job["job_id"])
    print(done.get("result_path"), done.get("status"))
    providers = client.providers.list()
```
