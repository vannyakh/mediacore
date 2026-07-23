"""Auto-generated MediaCore catalog stub for `crowdbunker`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CrowdbunkerProvider(StubProvider):
    name = 'crowdbunker'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CrowdBunker',)
    source = "catalog"
    description = 'Catalog stub for crowdbunker'
