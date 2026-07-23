"""Auto-generated MediaCore catalog stub for `lcpplay`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LcpplayProvider(StubProvider):
    name = 'lcpplay'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('LcpPlay',)
    source = "catalog"
    description = 'Catalog stub for lcpplay'
