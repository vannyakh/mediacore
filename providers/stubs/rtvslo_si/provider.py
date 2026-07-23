"""Auto-generated MediaCore catalog stub for `rtvslo.si`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtvsloSiProvider(StubProvider):
    name = 'rtvslo.si'
    status = 'not_configured'
    host_suffixes = ('rtvslo.si',)
    ie_names = ('rtvslo.si', 'rtvslo.si:show')
    source = "catalog"
    description = 'Catalog stub for rtvslo.si'
