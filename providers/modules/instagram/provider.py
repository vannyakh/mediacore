"""Auto-generated MediaCore platform module for `instagram`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class InstagramProvider(PlatformModule):
    name = 'instagram'
    status = 'broken'
    host_suffixes = ('instagram.com', 'www.instagram.com')
    ie_names = ('Instagram', 'instagram:story', 'instagram:tag', 'instagram:user')
    source = "catalog"
    description = 'Instagram hashtag search URLs'
