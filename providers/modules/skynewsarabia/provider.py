"""Auto-generated MediaCore platform module for `skynewsarabia`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SkynewsarabiaProvider(PlatformModule):
    name = 'skynewsarabia'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('skynewsarabia:article', 'skynewsarabia:video')
    source = "catalog"
    description = 'Platform module for skynewsarabia'
