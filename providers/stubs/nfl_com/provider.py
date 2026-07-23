"""Auto-generated MediaCore catalog stub for `nfl.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NflComProvider(StubProvider):
    name = 'nfl.com'
    status = 'not_configured'
    host_suffixes = ('nfl.com',)
    ie_names = ('nfl.com', 'nfl.com:article', 'nfl.com:\u200bplus:episode', 'nfl.com:\u200bplus:replay')
    source = "catalog"
    description = 'Catalog stub for nfl.com'
