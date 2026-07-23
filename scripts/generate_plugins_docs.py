#!/usr/bin/env python3
"""Generate docs/public/plugins.json from discovered plugin manifests."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "public" / "plugins.json"

# Simple Icons CDN slugs (+ optional color) keyed by short plugin dir name.
BRAND_ICONS: dict[str, tuple[str, str]] = {
    "storage-local": ("files", "0ea5e9"),
    "storage-s3": ("amazons3", "569A31"),
    "storage-r2": ("cloudflare", "F38020"),
    "storage-ftp": ("filezilla", "BF0000"),
    "storage-webdav": ("nextdotjs", "000000"),
    "storage-gdrive": ("googledrive", "4285F4"),
    "storage-azure": ("microsoftazure", "0078D4"),
    "storage-dropbox": ("dropbox", "0061FF"),
    "storage-onedrive": ("microsoftonedrive", "0078D4"),
    "ffmpeg": ("ffmpeg", "007808"),
    "webhook": ("webhook", "0ea5e9"),
    "telegram": ("telegram", "26A5E4"),
    "discord": ("discord", "5865F2"),
    "whisper": ("openai", "412991"),
    "translate": ("googletranslate", "4285F4"),
    "metadata": ("json", "000000"),
    "auth-apikey": ("auth0", "EB5424"),
    "analytics": ("googleanalytics", "E37400"),
    "provider": ("package", "0ea5e9"),
}

KIND_FALLBACK: dict[str, tuple[str, str]] = {
    "storage": ("googledrive", "4285F4"),
    "ffmpeg": ("ffmpeg", "007808"),
    "webhooks": ("webhook", "0ea5e9"),
    "notifications": ("bell", "0ea5e9"),
    "ai": ("openai", "412991"),
    "translation": ("googletranslate", "4285F4"),
    "metadata": ("json", "000000"),
    "authentication": ("auth0", "EB5424"),
    "analytics": ("googleanalytics", "E37400"),
    "provider": ("package", "0ea5e9"),
}


def short_name(full: str) -> str:
    prefix = "mediacore-plugin-"
    return full[len(prefix) :] if full.startswith(prefix) else full


def logo_for(short: str, kind: str) -> str:
    slug, color = BRAND_ICONS.get(short) or KIND_FALLBACK.get(kind) or ("puzzle", "0ea5e9")
    return f"https://cdn.simpleicons.org/{slug}/{color}"


def main() -> int:
    from packages.plugins.loader import PluginLoader, reset_plugin_loader

    reset_plugin_loader()
    plugins = PluginLoader(root=ROOT / "plugins").discover()
    rows = []
    for info in sorted(plugins, key=lambda p: p.name):
        short = short_name(info.name)
        rows.append(
            {
                "name": info.name,
                "short_name": short,
                "version": info.version,
                "kind": info.kind,
                "status": info.status,
                "description": info.description,
                "capabilities": list(info.capabilities or []),
                "logo": logo_for(short, info.kind),
            }
        )

    by_kind: dict[str, int] = {}
    for row in rows:
        by_kind[row["kind"]] = by_kind.get(row["kind"], 0) + 1

    payload = {
        "version": 1,
        "count": len(rows),
        "by_kind": by_kind,
        "plugins": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({payload['count']} plugins)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
