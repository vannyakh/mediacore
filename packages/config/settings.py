"""Shared MediaCore configuration (used by API, worker, CLI)."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class MediaCoreSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "MediaCore"
    environment: str = "development"
    debug: bool = True

    database_url: str = "postgresql+psycopg://mediacore:mediacore@localhost:5432/mediacore"
    database_url_fallback: str = "sqlite+pysqlite:///./data/mediacore.db"
    use_sqlite: bool = True

    redis_url: str = "redis://localhost:6379/0"
    # Off by default for local SQLite/dev (no Redis required). Set true for multi-process events.
    events_redis_enabled: bool = False
    api_key_header: str = "X-API-Key"
    seed_api_key: str = "dev-api-key-change-me"
    jwt_secret: str = "dev-jwt-secret-change-me"
    jwt_algorithm: str = "HS256"

    storage_root: str = "./data/files"
    # local (default) | s3 | r2 | gdrive | azure | dropbox | onedrive | ftp | webdav
    storage_backend: str = "local"
    job_ttl_hours: int = 24
    allow_private_urls: bool = False
    sync_download: bool = True
    cors_origins: str = "*"

    # Optional cloud storage (only used when STORAGE_BACKEND != local)
    s3_bucket: str | None = None
    s3_region: str = "us-east-1"
    s3_access_key: str | None = None
    s3_secret_key: str | None = None
    s3_endpoint_url: str | None = None
    s3_public_base_url: str | None = None
    s3_prefix: str = "mediacore/"

    r2_account_id: str | None = None
    r2_bucket: str | None = None
    r2_access_key: str | None = None
    r2_secret_key: str | None = None
    r2_public_base_url: str | None = None

    azure_storage_connection_string: str | None = None
    azure_storage_container: str | None = None
    azure_public_base_url: str | None = None

    gdrive_credentials_json: str | None = None
    gdrive_folder_id: str | None = None

    dropbox_access_token: str | None = None
    onedrive_access_token: str | None = None

    ftp_host: str | None = None
    ftp_port: int = 21
    ftp_username: str = "anonymous"
    ftp_password: str = ""
    ftp_remote_root: str = "/mediacore"
    ftp_public_base_url: str | None = None

    webdav_url: str | None = None
    webdav_username: str = ""
    webdav_password: str = ""

    webhook_url: str | None = None
    telegram_bot_token: str | None = None
    telegram_chat_id: str | None = None
    discord_webhook_url: str | None = None

    log_level: str = "INFO"
    otel_enabled: bool = False
    cache_ttl_seconds: int = 300


_settings_override: MediaCoreSettings | None = None


@lru_cache
def _cached_settings() -> MediaCoreSettings:
    return MediaCoreSettings()


def get_settings() -> MediaCoreSettings:
    if _settings_override is not None:
        return _settings_override
    return _cached_settings()


def _clear_settings_cache() -> None:
    global _settings_override
    _settings_override = None
    _cached_settings.cache_clear()


# Tests and callers historically used get_settings.cache_clear()
get_settings.cache_clear = _clear_settings_cache  # type: ignore[attr-defined]


def load_settings(**overrides: object) -> MediaCoreSettings:
    """Reload settings; optional kwargs override env/.env for tests and tooling."""
    global _settings_override
    _cached_settings.cache_clear()
    if overrides:
        _settings_override = MediaCoreSettings(**overrides)  # type: ignore[arg-type]
        return _settings_override
    _settings_override = None
    return _cached_settings()
