"""empty message

Revision ID: 81c435bdc78e
Revises: 50163df575b9
Create Date: 2021-02-12 08:53:11.962549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81c435bdc78e'
down_revision = '50163df575b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('plant_origin_key', 'plant', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('plant_origin_key', 'plant', ['origin'])
    # ### end Alembic commands ###
