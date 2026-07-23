"""Auto-generated MediaCore catalog stub for `bibeltv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BibeltvProvider(StubProvider):
    name = 'bibeltv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('bibeltv:live', 'bibeltv:series', 'bibeltv:video')
    source = "catalog"
    description = 'BibelTV live program'
