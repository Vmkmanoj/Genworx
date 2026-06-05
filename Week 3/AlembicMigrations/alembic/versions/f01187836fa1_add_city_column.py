"""add city column

Revision ID: f01187836fa1
Revises: a79d534b5fd5
Create Date: 2026-06-05 10:09:48.893871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f01187836fa1'
down_revision: Union[str, Sequence[str], None] = 'a79d534b5fd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
