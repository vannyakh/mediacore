"""Auto-generated MediaCore catalog stub for `rtve.es`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtveEsProvider(StubProvider):
    name = 'rtve.es'
    status = 'not_configured'
    host_suffixes = ('rtve.es',)
    ie_names = ('rtve.es:alacarta', 'rtve.es:audio', 'rtve.es:live', 'rtve.es:program', 'rtve.es:television')
    source = "catalog"
    description = 'RTVE a la carta and Play'
