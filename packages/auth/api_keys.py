"""API key hashing helpers."""

from __future__ import annotations

import hashlib
import hmac


def hash_api_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()


def verify_api_key(raw_key: str, key_hash: str) -> bool:
    return hmac.compare_digest(hash_api_key(raw_key), key_hash)
