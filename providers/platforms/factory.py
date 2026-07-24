"""Build PlatformModule instances for every extractor in the providers index.

Folder modules live under ``providers/modules/<slug>/`` (see
``scripts/materialize_catalog_providers.py``). Runtime registration uses the
JSON index for speed; each platform still has an on-disk package to upgrade.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from providers.base_module import PlatformModule

INDEX = Path(__file__).resolve().parents[1] / "data" / "providers_index.json"
CATALOG_MANIFEST = Path(__file__).resolve().parents[1] / "modules" / "_manifest.json"


@lru_cache
def load_providers_index() -> dict:
    if not INDEX.exists():
        return {"count": 0, "providers": []}
    return json.loads(INDEX.read_text(encoding="utf-8"))


@lru_cache
def load_catalog_manifest() -> dict:
    if not CATALOG_MANIFEST.exists():
        return {"count": 0, "providers": []}
    return json.loads(CATALOG_MANIFEST.read_text(encoding="utf-8"))


def _make_module(
    *,
    name: str,
    hosts: tuple[str, ...],
    ie_names: tuple[str, ...],
    broken: bool = False,
    description: str = "",
    module: str | None = None,
) -> PlatformModule:
    class _PlatformModule(PlatformModule):
        pass

    safe = "".join(ch if ch.isalnum() else "_" for ch in name.title())
    _PlatformModule.__name__ = f"{safe}Provider"
    instance = _PlatformModule()
    instance.name = name
    instance.status = "broken" if broken else "not_configured"
    instance.host_suffixes = hosts
    instance.ie_names = ie_names
    instance.source = "catalog"
    instance.description = description
    if module:
        instance.catalog_module = module  # type: ignore[attr-defined]
    return instance


def build_all_providers() -> list[PlatformModule]:
    """All catalog extractors as MediaCore platform modules."""
    data = load_providers_index()
    manifest = {p["name"]: p for p in (load_catalog_manifest().get("providers") or [])}
    out: list[PlatformModule] = []
    seen: set[str] = set()
    for item in data.get("providers") or []:
        name = str(item.get("name") or "").strip()
        if not name or name in seen:
            continue
        seen.add(name)
        hosts = tuple(item.get("hosts") or ())
        ie_names = tuple(item.get("ie_names") or [])
        meta = manifest.get(name) or {}
        out.append(
            _make_module(
                name=name,
                hosts=hosts,
                ie_names=ie_names,
                broken=bool(item.get("broken")),
                description=str(item.get("description") or ""),
                module=meta.get("module"),
            )
        )
    return out


def build_platform_stubs() -> list[PlatformModule]:
    """Back-compat: modules that can match URLs (have host suffixes)."""
    return [p for p in build_all_providers() if p.host_suffixes]


def build_platform_modules() -> list[PlatformModule]:
    return build_platform_stubs()


def catalog_package_count() -> int:
    """Number of materialized packages under providers/modules/."""
    return int(load_catalog_manifest().get("count") or 0)
