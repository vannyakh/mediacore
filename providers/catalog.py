"""Platform extractor catalog (synced snapshot → MediaCore index)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent / "data"
EXTRACTORS = DATA_DIR / "extractors.json"
INDEX = DATA_DIR / "providers_index.json"


@lru_cache
def load_extractors_catalog() -> dict[str, Any]:
    if not EXTRACTORS.exists():
        return {"count": 0, "extractors": []}
    return json.loads(EXTRACTORS.read_text(encoding="utf-8"))


@lru_cache
def load_providers_index() -> dict[str, Any]:
    if not INDEX.exists():
        return {"count": 0, "providers": []}
    return json.loads(INDEX.read_text(encoding="utf-8"))


def list_extractors(*, include_broken: bool = True) -> list[dict[str, Any]]:
    items = load_extractors_catalog().get("extractors") or []
    if include_broken:
        return list(items)
    return [e for e in items if not e.get("broken")]


def catalog_summary() -> dict[str, Any]:
    extractors = load_extractors_catalog()
    index = load_providers_index()
    broken = sum(1 for e in (extractors.get("extractors") or []) if e.get("broken"))
    return {
        "source": extractors.get("synced_from"),
        "extractors": extractors.get("count", 0),
        "base_platforms": extractors.get("base_count") or index.get("count", 0),
        "providers_indexed": index.get("count", 0),
        "providers_with_hosts": index.get("with_hosts", 0),
        "broken": broken,
        "note": (
            "Full platform catalog is implemented as MediaCore platform modules. "
            "Direct media URLs on a module's hosts support metadata + download; "
            "page/watch URLs need official or permitted APIs — "
            "no third-party scraper runtime is bundled."
        ),
    }


def search_extractors(query: str, *, limit: int = 50) -> list[dict[str, Any]]:
    q = query.lower().strip()
    if not q:
        return []
    hits = []
    for item in list_extractors():
        name = str(item.get("id") or item.get("ie_name") or "").lower()
        desc = str(item.get("description") or "").lower()
        if q in name or q in desc:
            # Normalize for API schema (ie_name)
            hits.append(
                {
                    "ie_name": item.get("id") or item.get("ie_name"),
                    "description": item.get("description") or "",
                    "broken": bool(item.get("broken")),
                    "source": "catalog",
                }
            )
            if len(hits) >= limit:
                break
    return hits
