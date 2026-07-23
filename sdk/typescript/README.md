# MediaCore TypeScript SDK

```ts
import { MediaCore } from "./src/client";

const client = new MediaCore("dev-api-key-change-me");
const info = await client.media.analyze(url);
await client.media.download(url, info.formats[0].id);
await client.plugins.list();
```
