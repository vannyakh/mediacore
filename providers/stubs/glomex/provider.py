"""Auto-generated MediaCore catalog stub for `glomex`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GlomexProvider(StubProvider):
    name = 'glomex'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('glomex', 'glomex:embed')
    source = "catalog"
    description = 'Glomex videos'
