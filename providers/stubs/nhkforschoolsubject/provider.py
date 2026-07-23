"""Auto-generated MediaCore catalog stub for `nhkforschoolsubject`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NhkforschoolsubjectProvider(StubProvider):
    name = 'nhkforschoolsubject'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NhkForSchoolSubject',)
    source = "catalog"
    description = 'Portal page for each school subjects, like Japanese (kokugo, 国語) or math (sansuu/suugaku or 算数・数学)'
