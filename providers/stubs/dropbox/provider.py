"""Auto-generated MediaCore catalog stub for `dropbox`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DropboxProvider(StubProvider):
    name = 'dropbox'
    status = 'not_configured'
    host_suffixes = ('dropbox.com', 'www.dropbox.com', 'dl.dropboxusercontent.com')
    ie_names = ('Dropbox',)
    source = "catalog"
    description = 'Catalog stub for dropbox'
