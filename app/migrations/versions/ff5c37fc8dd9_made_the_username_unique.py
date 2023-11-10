"""made the username unique

Revision ID: ff5c37fc8dd9
Revises: bd1d0c97b0d6
Create Date: 2023-11-04 16:05:30.931147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ff5c37fc8dd9'
down_revision: Union[str, None] = 'bd1d0c97b0d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_posts_id', table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('published', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("'2023-11-04 15:39:07.240104+05:30'::timestamp with time zone"), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    op.create_index('ix_posts_id', 'posts', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("'2023-11-04 15:39:07.240104+05:30'::timestamp with time zone"), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###