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
    api_key_header: str = "X-API-Key"
    seed_api_key: str = "dev-api-key-change-me"
    jwt_secret: str = "dev-jwt-secret-change-me"
    jwt_algorithm: str = "HS256"

    storage_root: str = "./data/files"
    job_ttl_hours: int = 24
    allow_private_urls: bool = False
    sync_download: bool = True
    cors_origins: str = "*"

    log_level: str = "INFO"
    otel_enabled: bool = False
    cache_ttl_seconds: int = 300


@lru_cache
def get_settings() -> MediaCoreSettings:
    return MediaCoreSettings()


def load_settings(**overrides: object) -> MediaCoreSettings:
    get_settings.cache_clear()
    if overrides:
        return MediaCoreSettings(**overrides)  # type: ignore[arg-type]
    return get_settings()
