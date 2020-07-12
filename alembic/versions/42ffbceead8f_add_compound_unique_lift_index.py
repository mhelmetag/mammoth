"""remove other indexes and add compound unique lift index

Revision ID: 42ffbceead8f
Revises: 51909df056b7
Create Date: 2020-07-11 17:13:11.813517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42ffbceead8f'
down_revision = '51909df056b7'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('lifts_name_key', 'lifts')
    op.drop_index(op.f('ix_lifts_season'), 'lifts')
    op.create_index(op.f('ix_lifts_season_name'), 'lifts',
                    ['season', 'name'], unique=True)


def downgrade():
    op.create_unique_constraint('lifts_name_key', 'lifts', ['name'])
    op.create_index('ix_lifts_season', 'lifts', ['season'], unique=False)
    op.drop_index(op.f('ix_lifts_season_name'), 'lifts',
                  ['season', 'name'], unique=True)
