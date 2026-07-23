"""Auto-generated MediaCore catalog stub for `tv4`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv4Provider(StubProvider):
    name = 'tv4'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TV4',)
    source = "catalog"
    description = 'tv4.se and tv4play.se'
