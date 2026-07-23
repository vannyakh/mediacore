"""Auto-generated MediaCore catalog stub for `archiveorg`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
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
