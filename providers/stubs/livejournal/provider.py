"""Auto-generated MediaCore catalog stub for `livejournal`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LivejournalProvider(StubProvider):
    name = 'livejournal'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('LiveJournal',)
    source = "catalog"
    description = 'Catalog stub for livejournal'
