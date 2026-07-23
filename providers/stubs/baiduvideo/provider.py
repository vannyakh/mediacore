"""Auto-generated MediaCore catalog stub for `baiduvideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BaiduvideoProvider(StubProvider):
    name = 'baiduvideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('BaiduVideo',)
    source = "catalog"
    description = '百度视频'
