"""Auto-generated MediaCore catalog stub for `playvids`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PlayvidsProvider(StubProvider):
    name = 'playvids'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PlayVids',)
    source = "catalog"
    description = 'Catalog stub for playvids'
