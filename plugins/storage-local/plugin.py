"""Local filesystem storage — always available; no cloud services required."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.local import LocalStorage

PLUGIN = {
    "name": "mediacore-plugin-storage-local",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Local filesystem storage for MediaCore jobs (default; no cloud required)",
    "status": "available",
    "capabilities": ["store", "delete", "public_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> LocalStorage:
    return LocalStorage(root=root or getattr(settings, "storage_root", None))
