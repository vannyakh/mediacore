"""Auto-generated MediaCore catalog stub for `voicy`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VoicyProvider(StubProvider):
    name = 'voicy'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('voicy', 'voicy:channel')
    source = "catalog"
    description = 'Catalog stub for voicy'
