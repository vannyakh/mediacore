"""Compatibility shim — prefer `packages.engine` / `mediacore`."""

from mediacore import __version__
from packages.engine.engine import MediaCoreEngine as ExtractorEngine

__all__ = ["ExtractorEngine", "__version__"]
