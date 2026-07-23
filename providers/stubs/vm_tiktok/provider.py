"""Auto-generated MediaCore catalog stub for `vm.tiktok`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VmTiktokProvider(StubProvider):
    name = 'vm.tiktok'
    status = 'not_configured'
    host_suffixes = ('vm.tiktok',)
    ie_names = ('vm.tiktok',)
    source = "catalog"
    description = 'Catalog stub for vm.tiktok'
