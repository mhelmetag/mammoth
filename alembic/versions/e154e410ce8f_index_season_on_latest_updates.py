"""index season on latest_updates

Revision ID: e154e410ce8f
Revises: 89f9d5d96dff
Create Date: 2021-07-18 22:49:03.916487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e154e410ce8f'
down_revision = '89f9d5d96dff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_latest_updates_season'), 'latest_updates', ['season'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_latest_updates_season'), table_name='latest_updates')
    # ### end Alembic commands ###
