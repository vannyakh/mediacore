"""Auto-generated MediaCore catalog stub for `play.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PlayTvProvider(StubProvider):
    name = 'play.tv'
    status = 'not_configured'
    host_suffixes = ('play.tv',)
    ie_names = ('play.tv',)
    source = "catalog"
    description = 'PLAY (formerly goplay.be)'
