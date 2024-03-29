"""add season to latest_updates

Revision ID: 89f9d5d96dff
Revises: 9d2bc5f28130
Create Date: 2021-07-18 20:57:02.286680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89f9d5d96dff'
down_revision = '9d2bc5f28130'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('latest_updates', sa.Column('season', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('latest_updates', 'season')
    # ### end Alembic commands ###
