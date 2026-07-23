# MediaCore Java SDK (future)

Planned surface (same as other SDKs):

```java
var client = new MediaCore("api-key");
client.media().analyze(url);
client.media().download(url, "original");
client.media().convert(path, options);
client.media().thumbnail(url);
client.jobs().list();
client.plugins().list();
```

Not implemented yet — contributions welcome under `sdk/java/`.
