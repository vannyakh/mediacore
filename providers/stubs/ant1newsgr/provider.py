"""Auto-generated MediaCore catalog stub for `ant1newsgr`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Ant1newsgrProvider(StubProvider):
    name = 'ant1newsgr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ant1newsgr:article', 'ant1newsgr:embed')
    source = "catalog"
    description = 'ant1news.gr articles'
