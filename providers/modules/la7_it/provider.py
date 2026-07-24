"""Auto-generated MediaCore platform module for `la7.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class La7ItProvider(PlatformModule):
    name = 'la7.it'
    status = 'not_configured'
    host_suffixes = ('la7.it',)
    ie_names = ('la7.it', 'la7.it:\u200bpod:episode', 'la7.it:podcast')
    source = "catalog"
    description = 'Platform module for la7.it'
