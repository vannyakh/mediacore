"""Auto-generated MediaCore catalog stub for `onet.pl`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class OnetPlProvider(StubProvider):
    name = 'onet.pl'
    status = 'not_configured'
    host_suffixes = ('onet.pl',)
    ie_names = ('onet.pl',)
    source = "catalog"
    description = 'Catalog stub for onet.pl'
