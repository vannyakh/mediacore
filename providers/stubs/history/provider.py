"""Auto-generated MediaCore catalog stub for `history`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class HistoryProvider(StubProvider):
    name = 'history'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('history:player', 'history:topic')
    source = "catalog"
    description = 'History.com Topic'
