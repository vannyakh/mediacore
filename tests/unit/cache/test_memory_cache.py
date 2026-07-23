import pytest

from packages.cache.memory import MemoryCache

pytestmark = pytest.mark.unit


def test_memory_cache_ttl():
    cache = MemoryCache(default_ttl=60)
    cache.set("a", 1)
    assert cache.get("a") == 1
    cache.delete("a")
    assert cache.get("a") is None
