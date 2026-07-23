#!/usr/bin/env python3
"""Sync MediaCore platform catalog snapshot and regenerate provider index.

Usage:
  python scripts/sync_platform_catalog.py --offline
  python scripts/sync_platform_catalog.py --file path/to/sites.md
  python scripts/sync_platform_catalog.py --url https://example.com/sites.md
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "providers" / "data" / "sites_snapshot.json"
BASES = ROOT / "providers" / "data" / "site_bases.json"


def parse_sites_markdown(text: str) -> list[dict]:
    pat = re.compile(r"^\s*-\s+\*\*(.+?)\*\*(?::\s*(.*))?$", re.M)
    entries = []
    for m in pat.finditer(text):
        raw_name = m.group(1).strip()
        rest = (m.group(2) or "").strip()
        broken = "Currently broken" in rest
        desc = re.sub(r"\[\*.*?\*\]\([^)]*\)\s*", "", rest)
        desc = re.sub(r"\(\*\*Currently broken\*\*\)", "", desc).strip(" :")
        entries.append(
            {
                "ie_name": raw_name,
                "description": desc,
                "broken": broken,
                "source": "catalog",
            }
        )
    return entries


def write_snapshot(text: str, source: str) -> None:
    entries = parse_sites_markdown(text)
    bases = sorted({e["ie_name"].split(":")[0] for e in entries})
    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": source,
        "count": len(entries),
        "base_count": len(bases),
        "extractors": entries,
    }
    SNAPSHOT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    BASES.write_text(json.dumps(bases, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {SNAPSHOT.name} ({len(entries)} extractors, {len(bases)} bases)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync MediaCore platform catalog")
    parser.add_argument("--offline", action="store_true", help="Skip fetch; regenerate only")
    parser.add_argument("--file", type=Path, default=None, help="Local sites markdown file")
    parser.add_argument("--url", default=None, help="Remote sites markdown URL")
    args = parser.parse_args()

    if not args.offline:
        if args.file:
            write_snapshot(args.file.read_text(encoding="utf-8"), str(args.file))
        elif args.url:
            with urllib.request.urlopen(args.url, timeout=60) as resp:  # noqa: S310
                text = resp.read().decode("utf-8")
            write_snapshot(text, args.url)
        elif SNAPSHOT.exists():
            print(f"Using existing {SNAPSHOT.name} (pass --url/--file to refresh)")
        else:
            print(
                "No snapshot found. Provide --file or --url, or run with an existing snapshot.",
                file=sys.stderr,
            )
            return 1

    subprocess.check_call([sys.executable, str(ROOT / "scripts" / "generate_providers.py")])
    print("MediaCore platform catalog ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
