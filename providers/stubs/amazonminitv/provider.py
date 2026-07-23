"""Auto-generated MediaCore catalog stub for `amazonminitv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AmazonminitvProvider(StubProvider):
    name = 'amazonminitv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('AmazonMiniTV', 'amazonminitv:season', 'amazonminitv:series')
    source = "catalog"
    description = 'Amazon MiniTV Season, "minitv:season:" prefix'
