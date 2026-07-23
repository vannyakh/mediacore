"""Auto-generated MediaCore catalog stub for `youtubeytbe`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoutubeytbeProvider(StubProvider):
    name = 'youtubeytbe'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YoutubeYtBe',)
    source = "catalog"
    description = 'youtu.be'
