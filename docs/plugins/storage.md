# Storage

Slim MediaCore persists job outputs with **local storage only**.

```bash
STORAGE_BACKEND=local
STORAGE_ROOT=./data/files
```

| Backend | Plugin |
|---------|--------|
| Local | `mediacore-plugin-storage-local` |

Files are written under `STORAGE_ROOT` and served at `/files/{job_id}/{name}`.
