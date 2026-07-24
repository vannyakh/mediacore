#!/usr/bin/env python3
"""Provider upgrade queue for the MediaCore auto-upgrade agent loop.

Lists next catalog platform modules to upgrade, classifies known oEmbed candidates, and
records done / skipped outcomes. yt-dlp is never invoked — research URLs only.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "providers" / "data" / "providers_index.json"
BACKLOG = ROOT / "providers" / "data" / "upgrade_backlog.json"
REGISTRY = ROOT / "packages" / "registry" / "providers.py"

# Public oEmbed (or equivalent) endpoints — agent should prefer these first.
KNOWN_OEMBED: dict[str, dict[str, str]] = {
    "youtube": {
        "endpoint": "https://www.youtube.com/oembed",
        "note": "format=json; metadata_only (no download)",
    },
    "tiktok": {
        "endpoint": "https://www.tiktok.com/oembed",
        "note": "official public oEmbed; metadata_only",
    },
    "flickr": {
        "endpoint": "https://www.flickr.com/services/oembed",
        "note": "format=json",
    },
    "tumblr": {
        "endpoint": "https://www.tumblr.com/oembed/1.0",
        "note": "deprecated/unavailable (2024+); prefer hosts_only or Tumblr API credentials",
    },
    "smugmug": {
        "endpoint": "https://api.smugmug.com/services/oembed/",
        "note": "public oEmbed",
    },
    "slideshare": {
        "endpoint": "https://www.slideshare.net/api/oembed/2",
        "note": "oEmbed deprecated by SlideShare; hosts_only only",
    },
    "scribd": {
        "endpoint": "https://www.scribd.com/services/oembed",
        "note": "public oEmbed",
    },
    "speakerdeck": {
        "endpoint": "https://speakerdeck.com/oembed.json",
        "note": "public oEmbed",
    },
    "giphy": {
        "endpoint": "https://giphy.com/services/oembed",
        "note": "public oEmbed",
    },
    "gfycat": {
        "endpoint": "https://api.gfycat.com/v1/oembed",
        "note": "may be deprecated; verify before shipping",
    },
    "twitch": {
        "endpoint": "https://api.twitch.tv/v5/oembed",
        "note": "v5 oEmbed gone; Helix needs OAuth — skipped_no_api without credentials",
    },
    "spotify": {
        "endpoint": "https://open.spotify.com/oembed",
        "note": "metadata oEmbed only",
    },
    "applepodcasts": {
        "endpoint": "https://itunes.apple.com/lookup",
        "note": "use iTunes Lookup API (oEmbed 404); metadata_only",
    },
}

YTDLP_EXTRACTOR_TREE = "https://github.com/yt-dlp/yt-dlp/tree/master/yt_dlp/extractor"
YTDLP_EXTRACTORS_PY = (
    "https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/_extractors.py"
)
YTDLP_RAW_TMPL = (
    "https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/{module}.py"
)

BUILTIN_ALWAYS = frozenset({"filesystem", "generic", "example", "vimeo"})


def _parse_early_registry_names() -> set[str]:
    """Module tails registered before catalog modules → likely working providers."""
    text = REGISTRY.read_text(encoding="utf-8")
    # Rough: providers.X.provider strings in the first for-loop of build_default_registry
    names = set(BUILTIN_ALWAYS)
    for match in re.finditer(r'"providers\.([a-z0-9_]+)\.provider"', text):
        names.add(match.group(1))
    # Wikimedia registers as wikimedia.org
    if "wikimedia" in names:
        names.add("wikimedia.org")
    return names


def _load_index() -> list[dict]:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    return list(data.get("providers") or [])


def _load_backlog() -> dict:
    if BACKLOG.exists():
        return json.loads(BACKLOG.read_text(encoding="utf-8"))
    return {"version": 1, "items": {}}


def _save_backlog(data: dict) -> None:
    BACKLOG.parent.mkdir(parents=True, exist_ok=True)
    BACKLOG.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _research_urls(name: str) -> dict[str, str]:
    module = re.sub(r"[^a-z0-9]", "", name.lower().split(".")[0]) or "generic"
    return {
        "ytdlp_extractor_tree": YTDLP_EXTRACTOR_TREE,
        "ytdlp_extractors_index": YTDLP_EXTRACTORS_PY,
        "ytdlp_raw_guess": YTDLP_RAW_TMPL.format(module=module),
        "note": "Research hosts/_VALID_URL only; never port scrape/download logic",
    }


def sync_backlog() -> dict:
    """Ensure every index provider has a backlog row; mark done if already working."""
    working = _parse_early_registry_names()
    backlog = _load_backlog()
    items: dict = backlog.setdefault("items", {})
    for p in _load_index():
        name = str(p.get("name") or "").strip()
        if not name:
            continue
        row = items.get(name) or {
            "status": "pending",
            "hosts": p.get("hosts") or [],
            "hint": None,
            "note": "",
        }
        row["hosts"] = p.get("hosts") or []
        if name in working or name.replace(".", "_") in working:
            row["status"] = "done"
            row["hint"] = row.get("hint") or "registered_early"
        elif name in KNOWN_OEMBED and row.get("status") == "pending":
            row["hint"] = "oembed"
            row["oembed"] = KNOWN_OEMBED[name]
        elif row.get("status") == "pending" and row.get("hosts"):
            row["hint"] = row.get("hint") or "has_hosts_research_api"
        elif row.get("status") == "pending":
            row["hint"] = row.get("hint") or "catalog_only"
        items[name] = row
    backlog["items"] = items
    backlog["counts"] = _counts(items)
    _save_backlog(backlog)
    return backlog


def _counts(items: dict) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in items.values():
        st = str(row.get("status") or "pending")
        out[st] = out.get(st, 0) + 1
    return out


def cmd_sync(_: argparse.Namespace) -> int:
    data = sync_backlog()
    print(json.dumps(data.get("counts"), indent=2))
    print(f"Wrote {BACKLOG.relative_to(ROOT)}")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    data = sync_backlog()
    items = data["items"]
    prefer_oembed = not args.any

    def sort_key(name: str) -> tuple:
        row = items[name]
        hosts = 0 if row.get("hosts") else 1
        oembed = 0 if row.get("hint") == "oembed" else 1
        return (oembed if prefer_oembed else 0, hosts, name.lower())

    pending = [
        n
        for n, row in items.items()
        if row.get("status") == "pending"
        and (not prefer_oembed or row.get("hint") == "oembed" or bool(row.get("hosts")))
    ]
    if not pending and prefer_oembed:
        pending = [n for n, row in items.items() if row.get("status") == "pending"]

    pending.sort(key=sort_key)
    batch = pending[: max(1, args.limit)]
    out = []
    for name in batch:
        row = items[name]
        entry = {
            "name": name,
            "status": row.get("status"),
            "hint": row.get("hint"),
            "hosts": row.get("hosts") or [],
            "oembed": row.get("oembed"),
            "research": _research_urls(name),
            "actions": {
                "if_oembed": f"Create providers/{name.replace('.', '_')}/ using providers.oembed",
                "if_no_api": "hosts_only or skipped_no_api — do not scrape",
                "mark": f"uv run python scripts/provider_upgrade_queue.py mark --names {name} --status done",
            },
        }
        out.append(entry)

    print(
        json.dumps(
            {
                "batch_size": len(out),
                "counts": data.get("counts"),
                "ytdlp_policy": "hosts/_VALID_URL research only — never port extractors",
                "next": out,
            },
            indent=2,
        )
    )
    return 0


def cmd_mark(args: argparse.Namespace) -> int:
    data = sync_backlog()
    items = data["items"]
    names = [n.strip() for n in args.names.split(",") if n.strip()]
    for name in names:
        row = items.get(name) or {"hosts": [], "hint": None}
        row["status"] = args.status
        if args.note:
            row["note"] = args.note
        items[name] = row
        print(f"{name} -> {args.status}")
    data["items"] = items
    data["counts"] = _counts(items)
    _save_backlog(data)
    return 0


def cmd_status(_: argparse.Namespace) -> int:
    data = sync_backlog()
    print(json.dumps(data.get("counts"), indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_sync = sub.add_parser("sync", help="Rebuild backlog from providers_index.json")
    p_sync.set_defaults(func=cmd_sync)

    p_next = sub.add_parser("next", help="Print next upgrade batch as JSON")
    p_next.add_argument("--limit", type=int, default=5)
    p_next.add_argument(
        "--any",
        action="store_true",
        help="Do not prefer oEmbed/host candidates",
    )
    p_next.set_defaults(func=cmd_next)

    p_mark = sub.add_parser("mark", help="Update status for one or more names")
    p_mark.add_argument("--names", required=True, help="Comma-separated catalog names")
    p_mark.add_argument(
        "--status",
        required=True,
        choices=("pending", "done", "hosts_only", "skipped_no_api", "blocked"),
    )
    p_mark.add_argument("--note", default="")
    p_mark.set_defaults(func=cmd_mark)

    p_status = sub.add_parser("status", help="Print backlog counts")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
