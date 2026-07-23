"""initial schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-07-23

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "0001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_admin", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "api_keys",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("user_id", sa.String(length=36), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("key_hash", sa.String(length=128), nullable=False),
        sa.Column("key_prefix", sa.String(length=16), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("last_used_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_api_keys_key_hash", "api_keys", ["key_hash"], unique=True)
    op.create_index("ix_api_keys_key_prefix", "api_keys", ["key_prefix"])

    op.create_table(
        "jobs",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("user_id", sa.String(length=36), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("api_key_id", sa.String(length=36), sa.ForeignKey("api_keys.id"), nullable=True),
        sa.Column("type", sa.String(length=32), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "pending", "queued", "running", "completed", "failed", "expired", name="jobstatus"
            ),
            nullable=False,
        ),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("platform", sa.String(length=64), nullable=True),
        sa.Column("format_id", sa.String(length=64), nullable=True),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("result_path", sa.Text(), nullable=True),
        sa.Column("result_url", sa.Text(), nullable=True),
        sa.Column("meta_json", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_jobs_status", "jobs", ["status"])

    op.create_table(
        "downloads",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("job_id", sa.String(length=36), sa.ForeignKey("jobs.id"), nullable=False),
        sa.Column("path", sa.Text(), nullable=False),
        sa.Column("format_id", sa.String(length=64), nullable=False),
        sa.Column("container", sa.String(length=32), nullable=False),
        sa.Column("filesize", sa.Integer(), nullable=True),
        sa.Column("content_type", sa.String(length=128), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_downloads_job_id", "downloads", ["job_id"])

    op.create_table(
        "usage_events",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("api_key_id", sa.String(length=36), sa.ForeignKey("api_keys.id"), nullable=True),
        sa.Column("endpoint", sa.String(length=128), nullable=False),
        sa.Column("method", sa.String(length=16), nullable=False),
        sa.Column("status_code", sa.Integer(), nullable=False),
        sa.Column("platform", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_table(
        "rate_limits",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("api_key_id", sa.String(length=36), sa.ForeignKey("api_keys.id"), nullable=True),
        sa.Column("window_seconds", sa.Integer(), nullable=False),
        sa.Column("max_requests", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_table(
        "audit_logs",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("actor", sa.String(length=255), nullable=True),
        sa.Column("action", sa.String(length=128), nullable=False),
        sa.Column("detail", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("audit_logs")
    op.drop_table("rate_limits")
    op.drop_table("usage_events")
    op.drop_index("ix_downloads_job_id", table_name="downloads")
    op.drop_table("downloads")
    op.drop_index("ix_jobs_status", table_name="jobs")
    op.drop_table("jobs")
    op.drop_index("ix_api_keys_key_prefix", table_name="api_keys")
    op.drop_index("ix_api_keys_key_hash", table_name="api_keys")
    op.drop_table("api_keys")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
