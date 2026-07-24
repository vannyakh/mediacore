# MediaCore JavaScript SDK

Thin client for the MediaCore permitted download API (Node 18+ / browsers with `fetch`).

## Install

```bash
# from repo root
npm install ./sdk/javascript

# or link locally
cd sdk/javascript && npm link
```

## Usage

```js
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me", "http://localhost:8000");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url, "original");
const done = await client.jobs.wait(job.job_id);
console.log(done.status, done.result_path);
```
