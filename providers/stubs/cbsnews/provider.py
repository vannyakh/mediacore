"""Auto-generated MediaCore catalog stub for `cbsnews`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CbsnewsProvider(StubProvider):
    name = 'cbsnews'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('cbsnews', 'cbsnews:embed', 'cbsnews:live', 'cbsnews:livevideo')
    source = "catalog"
    description = 'CBS News'
