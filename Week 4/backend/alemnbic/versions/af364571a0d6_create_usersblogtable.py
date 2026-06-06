"""create UsersBlogTable

Revision ID: af364571a0d6
Revises: 
Create Date: 2026-06-05 12:16:21.631656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'af364571a0d6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("UserCreateBlog",
                    sa.Column("Id",postgresql.UUID(as_uuid=True),primary_key=True),
                    sa.Column("name",sa.String(100)),
                    sa.Column("blog",sa.Text(),nullable=True)
                    )


def downgrade() -> None:
    op.drop_table("UserCreateBlog")
