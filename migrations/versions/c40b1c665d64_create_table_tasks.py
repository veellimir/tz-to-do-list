"""create table tasks

Revision ID: c40b1c665d64
Revises: 3d71ee2223ab
Create Date: 2024-11-05 11:44:10.191598

"""
from alembic import op
import sqlalchemy as sa

revision = 'c40b1c665d64'
down_revision = '3d71ee2223ab'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tasks',
    sa.Column('title', sa.String(), nullable=True),
            sa.Column('description', sa.String(), nullable=True),
            sa.Column('status', sa.String(), nullable=True),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
            sa.PrimaryKeyConstraint('id')
            )
    op.create_index(op.f('ix_tasks_description'), 'tasks', ['description'], unique=False)
    op.create_index(op.f('ix_tasks_title'), 'tasks', ['title'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_tasks_title'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_description'), table_name='tasks')
    op.drop_table('tasks')
