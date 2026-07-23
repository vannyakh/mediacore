"""Auto-generated MediaCore catalog stub for `ctsnews`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CtsnewsProvider(StubProvider):
    name = 'ctsnews'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CtsNews',)
    source = "catalog"
    description = '華視新聞'
