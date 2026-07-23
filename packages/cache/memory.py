"""Simple TTL memory cache for analyze metadata."""

from __future__ import annotations

import time
from typing import Any


class MemoryCache:
    def __init__(self, default_ttl: int = 300) -> None:
        self.default_ttl = default_ttl
        self._store: dict[str, tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        item = self._store.get(key)
        if item is None:
            return None
        expires, value = item
        if time.time() > expires:
            self._store.pop(key, None)
            return None
        return value

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        self._store[key] = (time.time() + (ttl or self.default_ttl), value)

    def delete(self, key: str) -> None:
        self._store.pop(key, None)

    def clear(self) -> None:
        self._store.clear()


_cache: MemoryCache | None = None


def get_cache() -> MemoryCache:
    global _cache
    if _cache is None:
        from packages.config.settings import get_settings

        _cache = MemoryCache(default_ttl=get_settings().cache_ttl_seconds)
    return _cache
