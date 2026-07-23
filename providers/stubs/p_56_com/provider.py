"""Auto-generated MediaCore catalog stub for `56.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P56ComProvider(StubProvider):
    name = '56.com'
    status = 'not_configured'
    host_suffixes = ('56.com',)
    ie_names = ('56.com',)
    source = "catalog"
    description = 'Catalog stub for 56.com'
