"""API key authentication adapter — wraps packages.auth helpers."""

from __future__ import annotations

from typing import Any

from packages.plugins.services import ApiKeyAuthAdapter

PLUGIN = {
    "name": "mediacore-plugin-auth-apikey",
    "version": "0.1.0",
    "kind": "authentication",
    "description": "API key hash/verify adapter (core HTTP auth remains in apps.api)",
    "status": "available",
    "capabilities": ["api_key", "verify", "hash"],
}


def create(settings: Any | None = None) -> ApiKeyAuthAdapter:
    del settings
    return ApiKeyAuthAdapter()


def hash_key(raw_key: str) -> str:
    return ApiKeyAuthAdapter().hash(raw_key)


def verify(raw_key: str, key_hash: str) -> bool:
    return ApiKeyAuthAdapter().verify(raw_key, key_hash)
