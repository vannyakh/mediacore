"""Auto-generated MediaCore catalog stub for `gdcvault`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GdcvaultProvider(StubProvider):
    name = 'gdcvault'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('GDCVault',)
    source = "catalog"
    description = 'Catalog stub for gdcvault'
