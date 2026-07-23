"""Auto-generated MediaCore catalog stub for `pornhub`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PornhubProvider(StubProvider):
    name = 'pornhub'
    status = 'not_configured'
    host_suffixes = ('pornhub.com', 'www.pornhub.com')
    ie_names = ('PornHub',)
    source = "catalog"
    description = 'PornHub and Thumbzilla'
