"""Plugin loader — MediaCore stays small; capabilities come from plugins."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger("mediacore.plugins")


@dataclass
class PluginInfo:
    name: str
    version: str = "0.1.0"
    kind: str = "generic"
    description: str = ""
    status: str = "available"
    path: str | None = None
    capabilities: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "kind": self.kind,
            "description": self.description,
            "status": self.status,
            "path": self.path,
            "capabilities": self.capabilities,
        }


class PluginLoader:
    """Discovers plugin manifests under ./plugins/*/plugin.py."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(__file__).resolve().parents[2] / "plugins"
        self._plugins: dict[str, PluginInfo] = {}

    def discover(self) -> list[PluginInfo]:
        self._plugins.clear()
        if not self.root.exists():
            return []
        for entry in sorted(self.root.iterdir()):
            if not entry.is_dir():
                continue
            manifest = entry / "plugin.py"
            if not manifest.exists():
                # Placeholder directory without implementation
                info = PluginInfo(
                    name=f"mediacore-plugin-{entry.name}",
                    kind=entry.name.split("-")[0] if "-" in entry.name else entry.name,
                    description=f"Scaffold for {entry.name}",
                    status="stub",
                    path=str(entry),
                )
                self._plugins[info.name] = info
                continue
            try:
                info = self._load_manifest(entry)
                self._plugins[info.name] = info
            except Exception as exc:  # noqa: BLE001
                logger.warning("Failed to load plugin %s: %s", entry.name, exc)
                info = PluginInfo(
                    name=f"mediacore-plugin-{entry.name}",
                    status="error",
                    description=str(exc),
                    path=str(entry),
                )
                self._plugins[info.name] = info
        return list(self._plugins.values())

    def _load_manifest(self, entry: Path) -> PluginInfo:
        ns: dict[str, Any] = {}
        code = (entry / "plugin.py").read_text(encoding="utf-8")
        exec(compile(code, str(entry / "plugin.py"), "exec"), ns, ns)  # noqa: S102
        meta = ns.get("PLUGIN") or ns.get("plugin") or {}
        if hasattr(meta, "to_dict"):
            return meta
        return PluginInfo(
            name=meta.get("name", f"mediacore-plugin-{entry.name}"),
            version=meta.get("version", "0.1.0"),
            kind=meta.get("kind", "generic"),
            description=meta.get("description", ""),
            status=meta.get("status", "available"),
            path=str(entry),
            capabilities=list(meta.get("capabilities") or []),
        )

    def list(self) -> list[PluginInfo]:
        if not self._plugins:
            self.discover()
        return list(self._plugins.values())

    def get(self, name: str) -> PluginInfo | None:
        if not self._plugins:
            self.discover()
        return self._plugins.get(name)


_loader: PluginLoader | None = None


def get_plugin_loader() -> PluginLoader:
    global _loader
    if _loader is None:
        _loader = PluginLoader()
        _loader.discover()
    return _loader
