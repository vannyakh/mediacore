"""Auto-generated MediaCore catalog stub for `iq.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IqComProvider(StubProvider):
    name = 'iq.com'
    status = 'not_configured'
    host_suffixes = ('iq.com',)
    ie_names = ('iq.com', 'iq.com:album')
    source = "catalog"
    description = 'International version of iQiyi'
