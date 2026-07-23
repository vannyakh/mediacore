"""Auto-generated MediaCore catalog stub for `ninegag`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NinegagProvider(StubProvider):
    name = 'ninegag'
    status = 'not_configured'
    host_suffixes = ('9gag.com', 'www.9gag.com')
    ie_names = ('9gag',)
    source = "catalog"
    description = '9GAG'
