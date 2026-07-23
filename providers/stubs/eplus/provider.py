"""Auto-generated MediaCore catalog stub for `eplus`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class EplusProvider(StubProvider):
    name = 'eplus'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('eplus',)
    source = "catalog"
    description = 'e+ (イープラス)'
