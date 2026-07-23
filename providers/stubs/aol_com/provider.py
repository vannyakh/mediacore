"""Auto-generated MediaCore catalog stub for `aol.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AolComProvider(StubProvider):
    name = 'aol.com'
    status = 'broken'
    host_suffixes = ('aol.com',)
    ie_names = ('aol.com',)
    source = "catalog"
    description = 'Catalog stub for aol.com'
