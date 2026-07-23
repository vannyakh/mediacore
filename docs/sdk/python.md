# Python SDK

**Status:** Ready · **Package:** `mediacore_sdk` · **Path:** `sdk/python`

Synchronous [httpx](https://www.python-httpx.org/) client for scripts, workers, and services.

## Install

```bash
# From repo root (dev)
export PYTHONPATH=sdk/python:$PYTHONPATH
# httpx is already in the MediaCore workspace deps
```

```python
from mediacore_sdk import MediaCore
```

## Runtime

- Python 3.12+
- Dependency: `httpx`
- Context-manager safe (`with MediaCore(...) as client:`)

## Surface

| Method | HTTP |
|--------|------|
| `client.media.analyze(url)` | `POST /v1/analyze` |
| `client.media.download(url, format="original")` | `POST /v1/download` |
| `client.media.convert(path, **options)` | `POST /v1/convert` |
| `client.media.thumbnail(url, **options)` | `POST /v1/thumbnail` |
| `client.jobs.list(limit=50)` | `GET /v1/jobs` |
| `client.jobs.get(job_id)` | `GET /v1/jobs/{id}` |
| `client.plugins.list()` | `GET /v1/plugins` |

## Example

```python
from mediacore_sdk import MediaCore

client = MediaCore("dev-api-key-change-me")
meta = client.media.analyze("https://example.com/video.mp4")
job = client.media.download(meta["url"], meta["formats"][0]["id"])
client.media.convert("/tmp/out.mp4", container="webm")
client.media.thumbnail(meta["url"])
jobs = client.jobs.list()
plugins = client.plugins.list()
client.close()
```

Constructor: `MediaCore(api_key, base_url="http://localhost:8000")`.

## See also

- [REST API](/api/)
- [SDK overview](./)
