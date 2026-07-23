"""Auto-generated MediaCore catalog stub for `google_drive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GoogleDriveProvider(StubProvider):
    name = 'google_drive'
    status = 'not_configured'
    host_suffixes = ('drive.google.com', 'docs.google.com')
    ie_names = ('GoogleDrive', 'GoogleDrive:Folder')
    source = "catalog"
    description = 'Catalog stub for google_drive'
