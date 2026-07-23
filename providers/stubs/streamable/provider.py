"""Auto-generated MediaCore catalog stub for `streamable`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class StreamableProvider(StubProvider):
    name = 'streamable'
    status = 'not_configured'
    host_suffixes = ('streamable.com', 'www.streamable.com')
    ie_names = ('Streamable',)
    source = "catalog"
    description = 'Catalog stub for streamable'
