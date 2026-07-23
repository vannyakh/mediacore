# MediaCore JavaScript SDK

```js
import { MediaCore } from "@mediacore/sdk";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url, meta.formats[0].id);
await client.media.convert("/path/out.mp4", { container: "webm" });
await client.media.thumbnail(meta.url);
const jobs = await client.jobs.list();
const plugins = await client.plugins.list();
```

See [docs/sdk/](../../docs/sdk/) for the shared SDK surface.
