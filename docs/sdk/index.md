---
title: SDKs
---

# SDKs

Install a thin client for MediaCore’s permitted download API. Same surface across languages: **analyze → download → wait for job**.

## Install

::: code-group

```bash [Python]
pip install -e sdk/python
# or: uv pip install -e sdk/python
```

```bash [Node / npm]
npm install ./sdk/javascript
```

```bash [TypeScript]
npm install ./sdk/typescript
```

```bash [PHP]
composer config repositories.mediacore path ./sdk/php
composer require mediacore/sdk:@dev
```

```bash [Go]
go mod edit -replace=github.com/mediacore/sdk-go=./sdk/go
go get github.com/mediacore/sdk-go@v0.0.0
```

```bash [curl / other]
# No SDK required — call REST directly
curl -s -H "X-API-Key: dev-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/video.mp4"}' \
  http://localhost:8000/v1/analyze
```

:::

## Quick examples

::: code-group

```python [Python]
from mediacore_sdk import MediaCore

with MediaCore("dev-api-key-change-me") as client:
    meta = client.media.analyze("https://example.com/video.mp4")
    job = client.media.download(meta["url"])
    print(client.jobs.wait(job["job_id"]))
```

```js [JavaScript]
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url);
console.log(await client.jobs.wait(job.job_id));
```

```php [PHP]
$client = new \MediaCore\Client('dev-api-key-change-me');
$meta = $client->analyze('https://example.com/video.mp4');
$job = $client->download($meta['url']);
print_r($client->wait($job['job_id']));
```

```go [Go]
c := mediacore.New("dev-api-key-change-me")
meta, _ := c.Media.Analyze("https://example.com/video.mp4")
job, _ := c.Media.Download(meta["url"].(string), "original")
done, _ := c.Jobs.Wait(job["job_id"].(string), 0)
fmt.Println(done["status"])
```

:::

## API surface (all SDKs)

| Method | Endpoint |
|--------|----------|
| analyze | `POST /v1/analyze` |
| download | `POST /v1/download` |
| job get / wait | `GET /v1/jobs/{id}` |
| providers | `GET /v1/providers` |
| plugins | `GET /v1/plugins` |

Full REST: [API](/api/). Repo packages: [`sdk/`](https://github.com/vannyakh/mediacore/tree/master/sdk).
