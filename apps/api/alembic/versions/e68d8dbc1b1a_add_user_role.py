"""add user role

Revision ID: e68d8dbc1b1a
Revises: d35e34f264ed
Create Date: 2026-08-08 12:37:23.811428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'e68d8dbc1b1a'
down_revision: Union[str, Sequence[str], None] = 'd35e34f264ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    userrole = sa.Enum(
        "customer",
        "admin",
        name="userrole",
    )

    userrole.create(
        op.get_bind(),
        checkfirst=True,
    )

    op.add_column(
        "users",
        sa.Column(
            "role",
            userrole,
            nullable=False,
            server_default="customer",
        ),
    )


def downgrade():
    op.drop_column("users", "role")

    userrole = sa.Enum(
        "customer",
        "admin",
        name="userrole",
    )

    userrole.drop(
        op.get_bind(),
        checkfirst=True,
    )