"""create command session

Revision ID: a79d534b5fd5
Revises: d06de7fe4056
Create Date: 2026-06-05 09:55:29.141753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a79d534b5fd5'
down_revision: Union[str, Sequence[str], None] = 'd06de7fe4056'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "command",
        sa.Column("id",sa.Integer,primary_key = True),
        sa.Column("contant",sa.String(100))
    )
def downgrade() -> None:
    op.drop_table("command")
