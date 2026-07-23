"""Auto-generated MediaCore catalog stub for `ruv.is`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RuvIsProvider(StubProvider):
    name = 'ruv.is'
    status = 'not_configured'
    host_suffixes = ('ruv.is',)
    ie_names = ('ruv.is:spila',)
    source = "catalog"
    description = 'Catalog stub for ruv.is'
