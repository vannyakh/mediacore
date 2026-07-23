"""Auto-generated MediaCore catalog stub for `1tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P1tvProvider(StubProvider):
    name = '1tv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('1tv', '1tv:live')
    source = "catalog"
    description = 'Первый канал'
