"""Auto-generated MediaCore catalog stub for `polskieradio`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PolskieradioProvider(StubProvider):
    name = 'polskieradio'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PolskieRadio', 'polskieradio:audition', 'polskieradio:category', 'polskieradio:legacy', 'polskieradio:player', 'polskieradio:podcast', 'polskieradio:\u200bpodcast:list')
    source = "catalog"
    description = 'Catalog stub for polskieradio'
