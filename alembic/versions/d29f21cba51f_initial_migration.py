"""Initial migration

Revision ID: d29f21cba51f
Revises: 
Create Date: 2023-12-27 23:52:35.656785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd29f21cba51f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('related_task', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('employee', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_limit_hours', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['employee'], ['employees.id'], name='tasks_employee_fkey'),
    sa.ForeignKeyConstraint(['related_task'], ['tasks.id'], name='tasks_related_task_fkey'),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)
    # ### end Alembic commands ###
