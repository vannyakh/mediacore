"""Auto-generated MediaCore platform module for `afreecatv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class AfreecatvProvider(PlatformModule):
    name = 'afreecatv'
    status = 'not_configured'
    host_suffixes = ('afreecatv.com', 'www.afreecatv.com', 'vod.afreecatv.com', 'sooplive.com', 'www.sooplive.com', 'vod.sooplive.com', 'play.sooplive.com')
    ie_names = ('soop', 'afreecatv', 'soop:live', 'soop:user', 'soop:catchstory')
    source = "catalog"
    description = 'sooplive.com'
