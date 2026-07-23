"""Auto-generated MediaCore catalog stub for `medialaan`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MedialaanProvider(StubProvider):
    name = 'medialaan'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Medialaan',)
    source = "catalog"
    description = 'Catalog stub for medialaan'
