"""Auto-generated MediaCore catalog stub for `web.archive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WebArchiveProvider(StubProvider):
    name = 'web.archive'
    status = 'not_configured'
    host_suffixes = ('web.archive',)
    ie_names = ('web.archive:youtube',)
    source = "catalog"
    description = 'web.archive.org saved youtube videos, "ytarchive:" prefix'
