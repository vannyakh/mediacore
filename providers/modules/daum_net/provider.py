"""Auto-generated MediaCore platform module for `daum.net`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DaumNetProvider(PlatformModule):
    name = 'daum.net'
    status = 'not_configured'
    host_suffixes = ('daum.net',)
    ie_names = ('daum.net', 'daum.net:clip', 'daum.net:playlist', 'daum.net:user')
    source = "catalog"
    description = 'Platform module for daum.net'
