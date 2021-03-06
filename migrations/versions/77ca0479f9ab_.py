"""empty message

Revision ID: 77ca0479f9ab
Revises: d2fea5e259dc
Create Date: 2021-10-20 03:07:09.497756

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77ca0479f9ab'
down_revision = 'd2fea5e259dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('detalledeventas_ibfk_2', 'detalledeventas', type_='foreignkey')
    op.drop_column('detalledeventas', 'venta_id')
    op.add_column('ventas', sa.Column('detalleventa_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ventas', 'detalledeventas', ['detalleventa_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ventas', type_='foreignkey')
    op.drop_column('ventas', 'detalleventa_id')
    op.add_column('detalledeventas', sa.Column('venta_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('detalledeventas_ibfk_2', 'detalledeventas', 'ventas', ['venta_id'], ['id'])
    # ### end Alembic commands ###
