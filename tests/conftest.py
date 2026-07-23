"""Shared pytest fixtures for MediaCore."""

from __future__ import annotations

import os

import pytest
from fastapi.testclient import TestClient

# Defaults for import-time broker/config side effects
os.environ.setdefault("USE_SQLITE", "true")
os.environ.setdefault("SYNC_DOWNLOAD", "true")
os.environ.setdefault("DRAMATIQ_STUB", "true")
os.environ.setdefault("SEED_API_KEY", "test-key")


@pytest.fixture()
def api_headers() -> dict[str, str]:
    return {"X-API-Key": "test-key"}


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("USE_SQLITE", "true")
    monkeypatch.setenv("DATABASE_URL_FALLBACK", f"sqlite+pysqlite:///{tmp_path}/test.db")
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path / "files"))
    monkeypatch.setenv("SEED_API_KEY", "test-key")
    monkeypatch.setenv("SYNC_DOWNLOAD", "true")
    monkeypatch.setenv("DRAMATIQ_STUB", "true")

    import apps.api.db.session as session_mod
    import apps.api.main as main_mod
    from apps.api.config import get_settings
    from apps.api.db.session import create_db_engine, init_db

    get_settings.cache_clear()
    engine = create_db_engine()
    session_mod.engine = engine
    session_mod.SessionLocal.configure(bind=engine)
    init_db()

    app = main_mod.create_app()
    with TestClient(app) as c:
        yield c
    get_settings.cache_clear()


@pytest.fixture()
def storage_root(tmp_path, monkeypatch):
    root = tmp_path / "storage"
    root.mkdir()
    monkeypatch.setenv("STORAGE_ROOT", str(root))
    from apps.api.config import get_settings

    get_settings.cache_clear()
    yield root
    get_settings.cache_clear()
