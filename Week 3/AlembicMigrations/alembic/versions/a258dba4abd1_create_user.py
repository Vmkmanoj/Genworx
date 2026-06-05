"""create User

Revision ID: a258dba4abd1
Revises: f01187836fa1
Create Date: 2026-06-05 10:21:10.107028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a258dba4abd1'
down_revision: Union[str, Sequence[str], None] = 'f01187836fa1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "UserTable",
        sa.Column("id",sa.Integer,primary_key = True),
        sa.Column("Name",sa.String(100)),
        sa.Column("City",sa.String(100)),
        sa.Column("Age",sa.Integer)
    )


def downgrade() -> None:
    op.drop_table("UserTable")
