"""Auto-generated MediaCore catalog stub for `tv5unis`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv5unisProvider(StubProvider):
    name = 'tv5unis'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('tv5unis', 'tv5unis:video')
    source = "catalog"
    description = 'Catalog stub for tv5unis'
