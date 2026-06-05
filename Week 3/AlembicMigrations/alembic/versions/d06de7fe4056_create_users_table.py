"""create users table

Revision ID: d06de7fe4056
Revises: 
Create Date: 2026-06-05 09:41:36.421144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd06de7fe4056'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bolgsTable",
        sa.Column("id",sa.Integer,primary_key = True),
        sa.Column("name",sa.String(100))
    )


def downgrade() -> None:
    op.drop_table("blogTable")
