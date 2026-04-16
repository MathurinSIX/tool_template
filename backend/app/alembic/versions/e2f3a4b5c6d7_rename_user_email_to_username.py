"""rename user email column to username

Revision ID: e2f3a4b5c6d7
Revises: d4e8a1b2c3f4
Create Date: 2026-04-16 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "e2f3a4b5c6d7"
down_revision = "d4e8a1b2c3f4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_index("ix_user_email", table_name="user")
    op.alter_column(
        "user",
        "email",
        new_column_name="username",
        existing_type=sa.String(length=255),
        existing_nullable=False,
    )
    op.create_index(
        op.f("ix_user_username"), "user", ["username"], unique=True
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.alter_column(
        "user",
        "username",
        new_column_name="email",
        existing_type=sa.String(length=255),
        existing_nullable=False,
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
