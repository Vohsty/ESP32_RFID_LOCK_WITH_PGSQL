"""Initial Migration

Revision ID: 171b80985dad
Revises: 
Create Date: 2019-06-07 08:35:34.935590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171b80985dad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('failed_access_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attempted_uid', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_failed_access_logs_created_at'), 'failed_access_logs', ['created_at'], unique=False)
    op.drop_column('users', 'pin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pin', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_failed_access_logs_created_at'), table_name='failed_access_logs')
    op.drop_table('failed_access_logs')
    # ### end Alembic commands ###
