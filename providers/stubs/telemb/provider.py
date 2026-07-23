"""Auto-generated MediaCore catalog stub for `telemb`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TelembProvider(StubProvider):
    name = 'telemb'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('TeleMB',)
    source = "catalog"
    description = 'Catalog stub for telemb'
