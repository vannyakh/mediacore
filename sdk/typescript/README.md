# MediaCore TypeScript SDK

## Install

```bash
npm install ./sdk/typescript
```

## Usage

```ts
import { MediaCore } from "@mediacore/sdk-ts";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url ?? "https://example.com/video.mp4");
const done = await client.jobs.wait(job.job_id);
```
