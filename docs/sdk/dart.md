# Dart SDK

**Status:** Ready · **Package:** `mediacore` · **Path:** `sdk/dart`

Dart / Flutter client for mobile and desktop apps.

## Install

From your app directory (pub.dev publish comes later):

::: code-group

```bash [dart]
dart pub add --path ../sdk/dart
```

```yaml [pubspec.yaml]
dependencies:
  mediacore:
    path: ../sdk/dart
```

:::

```dart
import 'package:mediacore/mediacore.dart';
```

::: tip
Adjust the relative path to your MediaCore checkout. Registry publish is deferred.
:::

## Runtime

- Dart 3+
- Works with Flutter
- Auth: `X-API-Key`

## Surface

| Method | HTTP |
|--------|------|
| `client.media.analyze(url)` | `POST /v1/analyze` |
| `client.media.download(url, format)` | `POST /v1/download` |
| `client.media.convert(path, options?)` | `POST /v1/convert` |
| `client.media.thumbnail(url)` | `POST /v1/thumbnail` |
| `client.jobs.list()` | `GET /v1/jobs` |
| `client.jobs.get(id)` | `GET /v1/jobs/{id}` |
| `client.plugins.list()` | `GET /v1/plugins` |

## Example

```dart
final client = MediaCore('dev-api-key-change-me');
final meta = await client.media.analyze('https://example.com/video.mp4');
final job = await client.media.download(meta['url'] as String, 'original');
await client.jobs.list();
await client.plugins.list();
```

## See also

- [REST API](/api/)
- [SDK overview](./)
