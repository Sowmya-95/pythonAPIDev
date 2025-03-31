"""create users table

Revision ID: 39e4052a0d10
Revises: 49eb276a8380
Create Date: 2025-03-29 19:23:05.972629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39e4052a0d10'
down_revision: Union[str, None] = '49eb276a8380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime,
                  server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id', name='pk_users_id'),
        sa.UniqueConstraint('email', name='uq_users_email')
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
