# MediaCore Dart SDK

```dart
final client = MediaCore('dev-api-key-change-me');
final meta = await client.media.analyze('https://example.com/video.mp4');
final job = await client.media.download(meta['url'] as String, 'original');
await client.jobs.list();
await client.plugins.list();
```

See [docs/sdk/](../../docs/sdk/).
