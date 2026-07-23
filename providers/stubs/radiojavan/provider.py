"""Auto-generated MediaCore catalog stub for `radiojavan`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RadiojavanProvider(StubProvider):
    name = 'radiojavan'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('RadioJavan',)
    source = "catalog"
    description = 'Catalog stub for radiojavan'
