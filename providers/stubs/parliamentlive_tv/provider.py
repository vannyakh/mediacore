"""Auto-generated MediaCore catalog stub for `parliamentlive.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ParliamentliveTvProvider(StubProvider):
    name = 'parliamentlive.tv'
    status = 'not_configured'
    host_suffixes = ('parliamentlive.tv',)
    ie_names = ('parliamentlive.tv',)
    source = "catalog"
    description = 'UK parliament videos'
