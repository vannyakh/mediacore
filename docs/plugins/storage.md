# Storage Plugins

Storage persists job outputs. **Cloud storage is optional** — a local-only workflow works with zero cloud credentials or SDKs.

## Default

```bash
STORAGE_BACKEND=local   # default
STORAGE_ROOT=./data/files
```

`mediacore-plugin-storage-local` is always available. Workers write under `STORAGE_ROOT` and serve files at `/files/{job_id}/{name}`.

## Plugins

| Backend | Plugin | Status | Extra deps |
|---------|--------|--------|------------|
| Local | `mediacore-plugin-storage-local` | available | none |
| Amazon S3 | `mediacore-plugin-storage-s3` | available* | `uv sync --extra storage-s3` |
| Cloudflare R2 | `mediacore-plugin-storage-r2` | available* | `uv sync --extra storage-s3` |
| Google Drive | `mediacore-plugin-storage-gdrive` | stub | OAuth |
| Azure Blob | `mediacore-plugin-storage-azure` | stub | `uv sync --extra storage-azure` |
| Dropbox | `mediacore-plugin-storage-dropbox` | stub | OAuth |
| OneDrive | `mediacore-plugin-storage-onedrive` | stub | OAuth |
| FTP | `mediacore-plugin-storage-ftp` | available* | none (stdlib) |
| WebDAV | `mediacore-plugin-storage-webdav` | available* | none (httpx) |

\* Available when selected **and** configured. Unconfigured cloud backends raise a clear error; they never block local mode.

## Contract

Every backend implements `packages.storage.base.StorageBackend`:

```text
job_dir(job_id) → Path          # local staging (required for FFmpeg)
path_for(job_id, filename)
public_url(job_id, filename)
publish(job_id, path) → url     # upload/finalize (local: no-op upload)
delete_job(job_id)
```

Remote backends stage files locally, then `publish()` uploads them.

## Selecting a backend

```bash
# Local only (recommended for CLI / desktop / air-gapped)
STORAGE_BACKEND=local

# S3
STORAGE_BACKEND=s3
S3_BUCKET=my-bucket
S3_ACCESS_KEY=…
S3_SECRET_KEY=…
S3_REGION=us-east-1
# optional: S3_ENDPOINT_URL, S3_PUBLIC_BASE_URL

# Cloudflare R2
STORAGE_BACKEND=r2
R2_ACCOUNT_ID=…
R2_BUCKET=…
R2_ACCESS_KEY=…
R2_SECRET_KEY=…

# FTP / WebDAV
STORAGE_BACKEND=ftp
FTP_HOST=ftp.example.com
FTP_USERNAME=…
FTP_PASSWORD=…

STORAGE_BACKEND=webdav
WEBDAV_URL=https://dav.example.com/remote.php/dav/files/user
WEBDAV_USERNAME=…
WEBDAV_PASSWORD=…
```

## Runtime

`packages.plugins.runtime.get_storage()` → `packages.storage.factory.resolve_storage()`.

- `STORAGE_BACKEND=local` → never imports boto3 / cloud SDKs
- Other backends load the matching plugin’s `create(settings)` factory

## Add a storage plugin

1. Create `plugins/storage-<name>/plugin.py` with `PLUGIN` + `create(settings, *, root=None)`.
2. Implement `StorageBackend` under `packages/storage/` (or inside the plugin).
3. Register the backend name in `packages/storage/factory.py` → `BACKEND_PLUGINS`.
4. Keep `status: "stub"` until credentials + client work end-to-end.
5. Run `uv run pytest -m storage`.
