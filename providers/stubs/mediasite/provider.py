"""Auto-generated MediaCore catalog stub for `mediasite`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MediasiteProvider(StubProvider):
    name = 'mediasite'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Mediasite',)
    source = "catalog"
    description = 'Catalog stub for mediasite'
