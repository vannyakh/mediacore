#!/usr/bin/env python3
"""Materialize catalog stubs as providers/stubs/<slug>/provider.py.

Reads:  providers/data/providers_index.json
Writes: providers/stubs/<slug>/… + providers/stubs/_manifest.json

Note: do NOT use providers/catalog/ — that name is reserved for providers/catalog.py.

Runtime registration still uses the index/factory for speed; folders exist so
each platform has a concrete file to upgrade from stub → working provider.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "providers" / "data" / "providers_index.json"
OUT = ROOT / "providers" / "stubs"
MANIFEST = OUT / "_manifest.json"

# Top-level packages that must not collide with stub module names
RESERVED = frozenset(
    {
        "catalog",
        "platforms",
        "stubs",
        "data",
        "filesystem",
        "vimeo",
        "generic",
        "example",
        "base_stub",
    }
)

WORKING_SKIP = frozenset({"filesystem", "vimeo", "generic", "example"})


def module_slug(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9_]", "_", name.strip().lower())
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "unknown"
    if s[0].isdigit():
        s = f"p_{s}"
    if s in RESERVED or s.startswith("__"):
        s = f"plat_{s}"
    return s


def class_name(slug: str) -> str:
    parts = [p for p in slug.split("_") if p]
    base = "".join(p[:1].upper() + p[1:] for p in parts) or "Unknown"
    if not base.endswith("Provider"):
        base = f"{base}Provider"
    if not base[0].isalpha():
        base = f"P{base}"
    return base


def render_provider(
    *,
    slug: str,
    name: str,
    hosts: list[str],
    ie_names: list[str],
    broken: bool,
    description: str,
    status: str,
) -> str:
    cls = class_name(slug)
    st = "broken" if broken else (status or "not_configured")
    desc = description or f"Catalog stub for {name}"
    return f'''"""Auto-generated MediaCore catalog stub for `{name}`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class {cls}(StubProvider):
    name = {name!r}
    status = {st!r}
    host_suffixes = {tuple(hosts)!r}
    ie_names = {tuple(ie_names)!r}
    source = "catalog"
    description = {desc!r}
'''


def main() -> int:
    if not INDEX.exists():
        raise SystemExit(f"Missing {INDEX}; run sync_platform_catalog.py first")

    data = json.loads(INDEX.read_text(encoding="utf-8"))
    providers = data.get("providers") or []

    if OUT.exists():
        # Keep __init__.py pattern: wipe generated package dirs only
        for child in OUT.iterdir():
            if child.name.startswith(".") or child.name == "README.md":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            elif child.name in {"_manifest.json", "__init__.py"}:
                child.unlink(missing_ok=True)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "__init__.py").write_text(
        '"""Materialized catalog stub packages (one folder per platform)."""\n',
        encoding="utf-8",
    )

    manifest: list[dict] = []
    seen_slugs: dict[str, str] = {}
    written = 0

    for item in providers:
        name = str(item.get("name") or "").strip()
        if not name or name.lower() in WORKING_SKIP:
            continue

        slug = module_slug(name)
        if slug in seen_slugs:
            # Disambiguate collisions
            n = 2
            while f"{slug}_{n}" in seen_slugs:
                n += 1
            slug = f"{slug}_{n}"
        seen_slugs[slug] = name

        hosts = list(item.get("hosts") or [])
        ie_names = list(item.get("ie_names") or [])
        broken = bool(item.get("broken"))
        description = str(item.get("description") or "")
        status = str(item.get("status") or "not_configured")

        pkg = OUT / slug
        pkg.mkdir(parents=True, exist_ok=True)
        (pkg / "__init__.py").write_text("", encoding="utf-8")
        (pkg / "provider.py").write_text(
            render_provider(
                slug=slug,
                name=name,
                hosts=hosts,
                ie_names=ie_names,
                broken=broken,
                description=description,
                status=status,
            ),
            encoding="utf-8",
        )
        manifest.append(
            {
                "slug": slug,
                "name": name,
                "module": f"providers.stubs.{slug}.provider",
                "hosts": hosts,
                "broken": broken,
                "status": "broken" if broken else status,
            }
        )
        written += 1

    MANIFEST.write_text(
        json.dumps({"version": 1, "count": written, "providers": manifest}, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUT / "README.md").write_text(
        """# Catalog provider stubs

One folder per platform from `providers/data/providers_index.json`.

- Status is `not_configured` (or `broken`) until you implement permitted/official access.
- Runtime still loads stubs via `providers.platforms.factory` (fast).
- To upgrade a platform: edit `providers/stubs/<slug>/provider.py` and register it early in `packages/registry/providers.py`.

Regenerate:

```bash
uv run python scripts/sync_platform_catalog.py --offline
uv run python scripts/materialize_catalog_providers.py
```
""",
        encoding="utf-8",
    )

    print(f"Wrote {written} catalog packages under {OUT.relative_to(ROOT)}")
    print(f"Manifest: {MANIFEST.relative_to(ROOT)} ({written} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
