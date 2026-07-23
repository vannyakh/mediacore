"""Auto-generated MediaCore catalog stub for `tvcarticle`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TvcarticleProvider(StubProvider):
    name = 'tvcarticle'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TVCArticle',)
    source = "catalog"
    description = 'Catalog stub for tvcarticle'
