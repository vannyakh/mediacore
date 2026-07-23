# MediaCore TypeScript SDK

```ts
import { MediaCore } from "./src/client.js";

const client = new MediaCore("dev-api-key-change-me");
const meta = await client.media.analyze("https://example.com/video.mp4");
const job = await client.media.download(meta.url!, meta.formats[0].id);
await client.jobs.list();
await client.plugins.list();
```

Same surface as JavaScript / Python / Go / Rust / Dart / C#. See [docs/sdk/](../../docs/sdk/).
