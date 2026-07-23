"""Auto-generated MediaCore catalog stub for `sky.it`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SkyItProvider(StubProvider):
    name = 'sky.it'
    status = 'not_configured'
    host_suffixes = ('sky.it',)
    ie_names = ('sky.it',)
    source = "catalog"
    description = 'Catalog stub for sky.it'
