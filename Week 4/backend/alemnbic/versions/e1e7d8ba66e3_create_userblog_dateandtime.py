"""create Userblog dateAndtime

Revision ID: e1e7d8ba66e3
Revises: af364571a0d6
Create Date: 2026-06-06 14:55:53.890422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1e7d8ba66e3'
down_revision: Union[str, Sequence[str], None] = 'af364571a0d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("UserCreateBlog",sa.Column("CreateDateAndTime",sa.TIMESTAMP))



def downgrade() -> None:
    op.drop_column( "UserCreateBlog","CreateDateAndTime")
