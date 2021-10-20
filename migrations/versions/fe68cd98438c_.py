"""empty message

Revision ID: fe68cd98438c
Revises: cd0f1832fb23
Create Date: 2021-10-20 03:48:55.425096

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe68cd98438c'
down_revision = 'cd0f1832fb23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detallesdeingresos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_articulo', sa.Integer(), nullable=False),
    sa.Column('cantidad_di', sa.Integer(), nullable=False),
    sa.Column('precio_di', sa.Integer(), nullable=False),
    sa.Column('ingreso_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingreso_id'], ['ingresos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('detalleingreso')
    op.add_column('productos', sa.Column('detalleingreso_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'productos', 'detallesdeingresos', ['detalleingreso_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'productos', type_='foreignkey')
    op.drop_column('productos', 'detalleingreso_id')
    op.create_table('detalleingreso',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_ingreso', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_articulo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cantidad_di', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('precio_di', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ingreso_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ingreso_id'], ['ingresos.id'], name='detalleingreso_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('detallesdeingresos')
    # ### end Alembic commands ###
