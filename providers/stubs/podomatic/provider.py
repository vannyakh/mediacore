"""Auto-generated MediaCore catalog stub for `podomatic`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PodomaticProvider(StubProvider):
    name = 'podomatic'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('podomatic',)
    source = "catalog"
    description = 'Catalog stub for podomatic'
