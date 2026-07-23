"""Auto-generated MediaCore catalog stub for `svt`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SvtProvider(StubProvider):
    name = 'svt'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('svt:page', 'svt:play', 'svt:\u200bplay:series')
    source = "catalog"
    description = 'SVT Play and Öppet arkiv'
