"""Auto-generated MediaCore catalog stub for `kuaishou`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KuaishouProvider(StubProvider):
    name = 'kuaishou'
    status = 'not_configured'
    host_suffixes = ('kuaishou.com', 'www.kuaishou.com', 'v.kuaishou.com')
    ie_names = ('Kuaishou',)
    source = "catalog"
    description = 'Catalog stub for kuaishou'
