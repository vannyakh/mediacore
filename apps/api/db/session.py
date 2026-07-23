"""Database engine and session helpers."""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from apps.api.config import get_settings
from apps.api.db.base import Base
from apps.api.db.models import ApiKey, User
from apps.api.security import hash_api_key


def _database_url() -> str:
    settings = get_settings()
    if settings.use_sqlite:
        Path("data").mkdir(parents=True, exist_ok=True)
        return settings.database_url_fallback
    return settings.database_url


def create_db_engine():
    url = _database_url()
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, future=True, connect_args=connect_args)


engine = create_db_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    seed_dev_data()


def seed_dev_data() -> None:
    settings = get_settings()
    with SessionLocal() as db:
        existing = db.scalar(select(ApiKey).where(ApiKey.key_prefix == settings.seed_api_key[:12]))
        if existing:
            return
        user = User(email="admin@localhost", name="Admin", is_admin=True)
        db.add(user)
        db.flush()
        key = ApiKey(
            user_id=user.id,
            name="development",
            key_hash=hash_api_key(settings.seed_api_key),
            key_prefix=settings.seed_api_key[:12],
            is_active=True,
        )
        db.add(key)
        db.commit()
