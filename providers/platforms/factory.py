"""Build StubProvider instances for every extractor in the providers index."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from providers.base_stub import StubProvider

INDEX = Path(__file__).resolve().parents[1] / "data" / "providers_index.json"


@lru_cache
def load_providers_index() -> dict:
    if not INDEX.exists():
        return {"count": 0, "providers": []}
    return json.loads(INDEX.read_text(encoding="utf-8"))


def _make_stub(
    *,
    name: str,
    hosts: tuple[str, ...],
    ie_names: tuple[str, ...],
    broken: bool = False,
    description: str = "",
) -> StubProvider:
    class _PlatformStub(StubProvider):
        pass

    safe = "".join(ch if ch.isalnum() else "_" for ch in name.title())
    _PlatformStub.__name__ = f"{safe}Provider"
    instance = _PlatformStub()
    instance.name = name
    instance.status = "broken" if broken else "not_configured"
    instance.host_suffixes = hosts
    instance.ie_names = ie_names
    instance.source = "catalog"
    instance.description = description
    return instance


def build_all_providers() -> list[StubProvider]:
    """All catalog extractors as MediaCore stub providers."""
    data = load_providers_index()
    out: list[StubProvider] = []
    seen: set[str] = set()
    for item in data.get("providers") or []:
        name = str(item.get("name") or "").strip()
        if not name or name in seen:
            continue
        seen.add(name)
        hosts = tuple(item.get("hosts") or ())
        ie_names = tuple(item.get("ie_names") or ())
        out.append(
            _make_stub(
                name=name,
                hosts=hosts,
                ie_names=ie_names,
                broken=bool(item.get("broken")),
                description=str(item.get("description") or ""),
            )
        )
    return out


# Back-compat alias
def build_platform_stubs() -> list[StubProvider]:
    """Providers that can match URLs (have host suffixes)."""
    return [p for p in build_all_providers() if p.host_suffixes]
