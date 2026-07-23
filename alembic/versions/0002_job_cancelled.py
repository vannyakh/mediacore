"""add cancelled job status

Revision ID: 0002_job_cancelled
Revises: 0001_initial
Create Date: 2026-07-23

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0002_job_cancelled"
down_revision: Union[str, None] = "0001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name == "postgresql":
        op.execute("ALTER TYPE jobstatus ADD VALUE IF NOT EXISTS 'cancelled'")
    # SQLite / others: Enum stored as string — no DDL required for new value.


def downgrade() -> None:
    # PostgreSQL enum values cannot be removed safely; no-op.
    pass
