"""empty message

Revision ID: 66877218d201
Revises: 
Create Date: 2024-04-27 15:37:39.013650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '66877218d201'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('post', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follows',
    sa.Column('followed_username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('follower_username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('followed_username', 'follower_username')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('read', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_content'), 'posts', ['content'], unique=False)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_content'), table_name='posts')
    op.drop_table('posts')
    op.drop_table('notifications')
    op.drop_table('likes')
    op.drop_table('follows')
    op.drop_table('comments')
    # ### end Alembic commands ###