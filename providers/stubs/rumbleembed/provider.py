"""Auto-generated MediaCore catalog stub for `rumbleembed`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RumbleembedProvider(StubProvider):
    name = 'rumbleembed'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('RumbleEmbed',)
    source = "catalog"
    description = 'Catalog stub for rumbleembed'
