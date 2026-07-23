"""Auto-generated MediaCore catalog stub for `nick.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NickComProvider(StubProvider):
    name = 'nick.com'
    status = 'not_configured'
    host_suffixes = ('nick.com',)
    ie_names = ('nick.com',)
    source = "catalog"
    description = 'Catalog stub for nick.com'
