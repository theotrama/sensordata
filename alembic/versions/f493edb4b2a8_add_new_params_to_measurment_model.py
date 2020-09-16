"""Add new params to Measurment model

Revision ID: f493edb4b2a8
Revises: 5b7447ea1cc4
Create Date: 2020-09-16 11:52:59.082324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f493edb4b2a8'
down_revision = '5b7447ea1cc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurements', sa.Column('data', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('measurements', 'data')
    # ### end Alembic commands ###
