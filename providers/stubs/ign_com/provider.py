"""Auto-generated MediaCore catalog stub for `ign.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IgnComProvider(StubProvider):
    name = 'ign.com'
    status = 'not_configured'
    host_suffixes = ('ign.com',)
    ie_names = ('ign.com',)
    source = "catalog"
    description = 'Catalog stub for ign.com'
