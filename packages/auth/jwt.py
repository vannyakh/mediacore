"""JWT helpers for admin sessions."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import jwt

from packages.config.settings import get_settings


def create_access_token(subject: str, *, expires_minutes: int = 60) -> str:
    settings = get_settings()
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(minutes=expires_minutes),
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict:
    settings = get_settings()
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
