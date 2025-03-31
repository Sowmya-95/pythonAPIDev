"""add foreign key to posts table

Revision ID: 20bd99224ad6
Revises: 39e4052a0d10
Create Date: 2025-03-29 19:35:56.643332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20bd99224ad6'
down_revision: Union[str, None] = '39e4052a0d10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
