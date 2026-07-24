"""Auto-generated MediaCore platform module for `google_drive`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class GoogleDriveProvider(PlatformModule):
    name = 'google_drive'
    status = 'not_configured'
    host_suffixes = ('drive.google.com', 'docs.google.com')
    ie_names = ('GoogleDrive', 'GoogleDrive:Folder')
    source = "catalog"
    description = 'Platform module for google_drive'
