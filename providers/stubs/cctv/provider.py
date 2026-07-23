"""Auto-generated MediaCore catalog stub for `cctv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CctvProvider(StubProvider):
    name = 'cctv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CCTV',)
    source = "catalog"
    description = '央视网'
