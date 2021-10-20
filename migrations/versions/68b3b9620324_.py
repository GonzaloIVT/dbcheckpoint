"""empty message

Revision ID: 68b3b9620324
Revises: d1be009b4979
Create Date: 2021-10-20 03:16:38.693547

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68b3b9620324'
down_revision = 'd1be009b4979'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_cat', sa.String(length=120), nullable=True),
    sa.Column('descripcion_cat', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('categoria')
    op.add_column('productos', sa.Column('categoria_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'productos', 'categorias', ['categoria_id'], ['id'])
    op.drop_column('productos', 'id_categoria')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productos', sa.Column('id_categoria', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'productos', type_='foreignkey')
    op.drop_column('productos', 'categoria_id')
    op.create_table('categoria',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre_cat', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('descripcion_cat', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('categorias')
    # ### end Alembic commands ###