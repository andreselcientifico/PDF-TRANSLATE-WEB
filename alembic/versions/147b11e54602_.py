"""empty message

Revision ID: 147b11e54602
Revises: 3118d24d35af
Create Date: 2024-04-28 17:26:30.202174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import pgvector

# revision identifiers, used by Alembic.
revision: str = '147b11e54602'
down_revision: Union[str, None] = '3118d24d35af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('embeddings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('embbedings', pgvector.sqlalchemy.Vector(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_content'), 'comments', ['content'], unique=False)
    op.create_index(op.f('ix_notifications_content'), 'notifications', ['content'], unique=False)
    op.drop_column('posts', 'embbedings')
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.add_column('posts', sa.Column('embbedings', pgvector.sqlalchemy.Vector(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_notifications_content'), table_name='notifications')
    op.drop_index(op.f('ix_comments_content'), table_name='comments')
    op.drop_table('embeddings')
    # ### end Alembic commands ###
