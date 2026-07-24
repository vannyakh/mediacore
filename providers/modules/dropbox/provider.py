"""Auto-generated MediaCore platform module for `dropbox`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DropboxProvider(PlatformModule):
    name = 'dropbox'
    status = 'not_configured'
    host_suffixes = ('dropbox.com', 'www.dropbox.com', 'dl.dropboxusercontent.com')
    ie_names = ('Dropbox',)
    source = "catalog"
    description = 'Platform module for dropbox'
