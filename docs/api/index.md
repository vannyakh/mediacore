# MediaCore REST API

Base: `http://localhost:8000`  
Auth: `X-API-Key: <key>`

## Endpoints

| Method | Path | Notes |
|--------|------|-------|
| GET | `/health` | Liveness |
| POST | `/v1/analyze` | Sync metadata + formats + manifest |
| POST | `/v1/download` | Async job |
| POST | `/v1/audio` | Extract audio (FFmpeg plugin) |
| POST | `/v1/video` | Video download job |
| POST | `/v1/subtitles` | Subtitle extraction job |
| POST | `/v1/thumbnail` | Thumbnail job |
| POST | `/v1/convert` | Format conversion |
| POST | `/v1/clip` | Clip with `options.start` / `options.duration` |
| POST | `/v1/jobs` | Create job (download alias) |
| GET | `/v1/jobs` | List jobs for the API key (newest first) |
| GET | `/v1/jobs/{id}` | Job status |
| GET | `/v1/providers` | Registered providers (active + all catalog stubs) |
| GET | `/v1/providers/catalog` | Platform catalog summary |
| GET | `/v1/providers/catalog/search?q=` | Search extractors |
| GET | `/v1/plugins` | Plugin list (see [plugins](/plugins/)) |
| GET | `/v1/system` | System info |
| GET | `/metrics` | Prometheus |

Compatibility: `/api/v1/*` mirrors `/v1/*`.
