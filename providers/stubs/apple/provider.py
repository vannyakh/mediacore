"""Auto-generated MediaCore catalog stub for `apple`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AppleProvider(StubProvider):
    name = 'apple'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('apple:\u200bmusic:connect',)
    source = "catalog"
    description = 'Apple Music Connect'
