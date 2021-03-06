"""empty message

Revision ID: d1be009b4979
Revises: 845e615d2211
Create Date: 2021-10-20 03:11:58.347002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1be009b4979'
down_revision = '845e615d2211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('detalledeventas', sa.Column('venta_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'detalledeventas', 'ventas', ['venta_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'detalledeventas', type_='foreignkey')
    op.drop_column('detalledeventas', 'venta_id')
    # ### end Alembic commands ###
