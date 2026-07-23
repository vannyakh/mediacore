"""Auto-generated MediaCore catalog stub for `orf`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class OrfProvider(StubProvider):
    name = 'orf'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('orf:\u200bfm4:story', 'orf:iptv', 'orf:on', 'orf:podcast', 'orf:radio')
    source = "catalog"
    description = 'fm4.orf.at stories'
