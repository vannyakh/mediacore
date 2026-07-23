"""Auto-generated MediaCore catalog stub for `mbn`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MbnProvider(StubProvider):
    name = 'mbn'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('MBN',)
    source = "catalog"
    description = 'mbn.co.kr (매일방송)'
