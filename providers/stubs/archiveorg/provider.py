"""Catalog stub for `archiveorg` (overridden at runtime).

Working implementation: ``providers.archiveorg.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ArchiveorgProvider(StubProvider):
    name = 'archiveorg'
    status = 'not_configured'
    host_suffixes = ('archive.org', 'www.archive.org')
    ie_names = ('archive.org', 'ArchiveOrg')
    source = "catalog"
    description = 'archive.org video and audio'
