"""Auto-generated MediaCore platform module for `linkedin`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class LinkedinProvider(PlatformModule):
    name = 'linkedin'
    status = 'not_configured'
    host_suffixes = ('linkedin.com', 'www.linkedin.com')
    ie_names = ('LinkedIn', 'linkedin', 'linkedin:events', 'linkedin:learning', 'linkedin:\u200blearning:course')
    source = "catalog"
    description = 'Platform module for linkedin'
