"""Auto-generated MediaCore platform module for `croatian.film`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CroatianFilmProvider(PlatformModule):
    name = 'croatian.film'
    status = 'not_configured'
    host_suffixes = ('croatian.film', 'www.croatian.film')
    ie_names = ('croatian.film',)
    source = "catalog"
    description = 'Platform module for croatian.film'
