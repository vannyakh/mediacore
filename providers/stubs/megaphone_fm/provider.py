"""Auto-generated MediaCore catalog stub for `megaphone.fm`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MegaphoneFmProvider(StubProvider):
    name = 'megaphone.fm'
    status = 'not_configured'
    host_suffixes = ('megaphone.fm',)
    ie_names = ('megaphone.fm',)
    source = "catalog"
    description = 'megaphone.fm embedded players'
