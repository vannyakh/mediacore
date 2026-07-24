"""Normalize and enrich MediaMetadata after analyze."""

from __future__ import annotations

from typing import Any

from packages.core.models import MediaMetadata
from packages.plugins.services import MetadataNormalizer

PLUGIN = {
    "name": "mediacore-plugin-metadata",
    "version": "0.1.0",
    "kind": "metadata",
    "description": "Normalize and lightly enrich media metadata",
    "status": "available",
    "capabilities": ["enrich", "normalize"],
}


def create(settings: Any | None = None) -> MetadataNormalizer:
    del settings
    return MetadataNormalizer()


def normalize(meta: MediaMetadata) -> MediaMetadata:
    return MetadataNormalizer().normalize(meta)


def enrich(meta: MediaMetadata) -> MediaMetadata:
    return MetadataNormalizer().enrich(meta)
