"""Auto-generated MediaCore catalog stub for `lecture2go`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Lecture2goProvider(StubProvider):
    name = 'lecture2go'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Lecture2Go',)
    source = "catalog"
    description = 'Catalog stub for lecture2go'
