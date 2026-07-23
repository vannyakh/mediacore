"""Auto-generated MediaCore catalog stub for `teletask`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TeletaskProvider(StubProvider):
    name = 'teletask'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('TeleTask',)
    source = "catalog"
    description = 'Catalog stub for teletask'
