"""Auto-generated MediaCore catalog stub for `udnembed`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class UdnembedProvider(StubProvider):
    name = 'udnembed'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('UDNEmbed',)
    source = "catalog"
    description = '聯合影音'
