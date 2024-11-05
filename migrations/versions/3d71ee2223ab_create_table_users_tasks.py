"""create table users, tasks

Revision ID: 3d71ee2223ab
Revises: 
Create Date: 2024-11-05 11:40:49.241980

"""
from alembic import op
import sqlalchemy as sa

revision = '3d71ee2223ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=True),
            sa.Column('password_hash', sa.String(), nullable=True),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
