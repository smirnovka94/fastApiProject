"""Add

Revision ID: de97256013ba
Revises: c92ce14f1337
Create Date: 2023-12-28 00:04:26.746789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de97256013ba'
down_revision: Union[str, None] = 'c92ce14f1337'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_table('tasks')
    op.drop_index('ix_employees_id', table_name='employees')
    op.drop_table('employees')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('employees_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('second_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('patronymic_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='employees_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_employees_id', 'employees', ['id'], unique=False)
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
