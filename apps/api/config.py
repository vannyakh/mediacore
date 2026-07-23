"""API settings — re-exports shared MediaCore config."""

from packages.config.settings import MediaCoreSettings as Settings
from packages.config.settings import get_settings, load_settings

__all__ = ["Settings", "get_settings", "load_settings"]
