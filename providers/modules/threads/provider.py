"""Auto-generated MediaCore platform module for `threads`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ThreadsProvider(PlatformModule):
    name = 'threads'
    status = 'not_configured'
    host_suffixes = ('threads.net', 'www.threads.net')
    ie_names = ('Threads',)
    source = "catalog"
    description = 'Platform module for threads'
