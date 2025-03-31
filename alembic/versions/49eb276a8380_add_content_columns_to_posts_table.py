"""add content columns to posts table

Revision ID: 49eb276a8380
Revises: 83ba4ac77072
Create Date: 2025-03-29 19:10:24.775907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49eb276a8380'
down_revision: Union[str, None] = '83ba4ac77072'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',
                  sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
