#!/usr/bin/env python3
"""Generate MediaCore provider index from the catalog snapshot.

Reads:  providers/data/sites_snapshot.json
Writes: providers/data/extractors.json
        providers/data/providers_index.json
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "providers" / "data" / "sites_snapshot.json"
OUT_EXTRACTORS = ROOT / "providers" / "data" / "extractors.json"
OUT_INDEX = ROOT / "providers" / "data" / "providers_index.json"

import ast


def _load_major_platforms() -> dict:
    """Parse MAJOR_PLATFORMS from hosts.py without importing the package tree."""
    path = ROOT / "providers" / "platforms" / "hosts.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "MAJOR_PLATFORMS":
                    return ast.literal_eval(node.value)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "MAJOR_PLATFORMS" and node.value is not None:
                return ast.literal_eval(node.value)
    raise RuntimeError("MAJOR_PLATFORMS not found")


MAJOR_PLATFORMS = _load_major_platforms()


def slug(name: str) -> str:
    s = name.strip()
    s = s.split(":")[0]
    s = re.sub(r"[^a-zA-Z0-9._-]+", "_", s)
    s = s.strip("_.").lower()
    return s or "unknown"


def curated_host_lookup() -> dict[str, tuple[str, tuple[str, ...], tuple[str, ...]]]:
    """Map ie/name keys -> (canonical_name, hosts, ie_names)."""
    lookup: dict[str, tuple[str, tuple[str, ...], tuple[str, ...]]] = {}
    for name, meta in MAJOR_PLATFORMS.items():
        hosts = tuple(meta.get("hosts") or ())
        ies = tuple(meta.get("ie_names") or ())
        lookup[name.lower()] = (name, hosts, ies)
        for ie in ies:
            lookup[ie.lower()] = (name, hosts, ies)
            lookup[slug(ie)] = (name, hosts, ies)
    return lookup


def main() -> int:
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    extractors = raw.get("extractors") or []

    clean = {
        "version": 1,
        "count": len(extractors),
        "base_count": raw.get("base_count"),
        "synced_from": raw.get("source"),
        "extractors": [
            {
                "id": e["ie_name"],
                "description": e.get("description") or "",
                "broken": bool(e.get("broken")),
            }
            for e in extractors
        ],
    }
    OUT_EXTRACTORS.parent.mkdir(parents=True, exist_ok=True)
    OUT_EXTRACTORS.write_text(json.dumps(clean, indent=2) + "\n", encoding="utf-8")

    lookup = curated_host_lookup()
    by_base: dict[str, dict] = {}

    for e in extractors:
        ie = e["ie_name"]
        base = ie.split(":")[0]
        key = slug(base)
        entry = by_base.setdefault(
            key,
            {
                "name": key,
                "ie_names": [],
                "hosts": [],
                "broken": False,
                "description": "",
                "status": "not_configured",
            },
        )
        if ie not in entry["ie_names"]:
            entry["ie_names"].append(ie)
        entry["broken"] = entry["broken"] or bool(e.get("broken"))
        if not entry["description"] and e.get("description"):
            entry["description"] = e["description"]

        # Apply curated hosts / canonical name
        for candidate in (key, base.lower(), ie.lower()):
            if candidate in lookup:
                canon, hosts, ies = lookup[candidate]
                entry["name"] = canon
                entry["hosts"] = list(hosts)
                for ie_name in ies:
                    if ie_name not in entry["ie_names"]:
                        entry["ie_names"].append(ie_name)
                break

        # Infer host if IE looks like a domain
        if not entry["hosts"] and "." in base and " " not in base:
            host = base.lower().lstrip(".")
            if host not in entry["hosts"]:
                entry["hosts"] = [host]

    # Ensure all curated platforms exist even if missing from snapshot
    for name, meta in MAJOR_PLATFORMS.items():
        hosts = list(meta.get("hosts") or [])
        if not hosts:
            continue
        key = name.lower()
        entry = by_base.setdefault(
            key,
            {
                "name": name,
                "ie_names": list(meta.get("ie_names") or []),
                "hosts": hosts,
                "broken": False,
                "description": "",
                "status": "not_configured",
            },
        )
        entry["name"] = name
        entry["hosts"] = hosts
        for ie_name in meta.get("ie_names") or []:
            if ie_name not in entry["ie_names"]:
                entry["ie_names"].append(ie_name)

    # Deduplicate by canonical name
    canonical: dict[str, dict] = {}
    for entry in by_base.values():
        name = entry["name"]
        existing = canonical.get(name)
        if existing is None:
            canonical[name] = entry
            continue
        # merge
        for ie_name in entry["ie_names"]:
            if ie_name not in existing["ie_names"]:
                existing["ie_names"].append(ie_name)
        if not existing["hosts"] and entry["hosts"]:
            existing["hosts"] = entry["hosts"]
        existing["broken"] = existing["broken"] or entry["broken"]

    providers = sorted(canonical.values(), key=lambda x: x["name"].lower())
    index = {
        "version": 1,
        "count": len(providers),
        "with_hosts": sum(1 for p in providers if p["hosts"]),
        "providers": providers,
    }
    OUT_INDEX.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT_EXTRACTORS.name} ({clean['count']} extractors) and "
        f"{OUT_INDEX.name} ({index['count']} providers, {index['with_hosts']} with hosts)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
