"""Auto-generated MediaCore catalog stub for `tvp`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TvpProvider(StubProvider):
    name = 'tvp'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('tvp', 'tvp:embed', 'tvp:stream', 'tvp:vod', 'tvp:\u200bvod:series')
    source = "catalog"
    description = 'Telewizja Polska'
