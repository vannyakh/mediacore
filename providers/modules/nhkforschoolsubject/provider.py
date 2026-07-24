"""Auto-generated MediaCore platform module for `nhkforschoolsubject`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NhkforschoolsubjectProvider(PlatformModule):
    name = 'nhkforschoolsubject'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NhkForSchoolSubject',)
    source = "catalog"
    description = 'Portal page for each school subjects, like Japanese (kokugo, 国語) or math (sansuu/suugaku or 算数・数学)'
