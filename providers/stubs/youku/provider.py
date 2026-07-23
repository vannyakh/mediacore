"""Auto-generated MediaCore catalog stub for `youku`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoukuProvider(StubProvider):
    name = 'youku'
    status = 'not_configured'
    host_suffixes = ('youku.com', 'v.youku.com', 'www.youku.com')
    ie_names = ('youku', 'youku:show')
    source = "catalog"
    description = '优酷'
