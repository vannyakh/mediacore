"""Auto-generated MediaCore catalog stub for `radio.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RadioDeProvider(StubProvider):
    name = 'radio.de'
    status = 'broken'
    host_suffixes = ('radio.de',)
    ie_names = ('radio.de',)
    source = "catalog"
    description = 'Catalog stub for radio.de'
