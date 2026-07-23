"""Auto-generated MediaCore catalog stub for `1news`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P1newsProvider(StubProvider):
    name = '1news'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('1News',)
    source = "catalog"
    description = '1news.co.nz article videos'
