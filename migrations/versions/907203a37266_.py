"""empty message

Revision ID: 907203a37266
Revises: 2176283df375
Create Date: 2021-10-20 03:27:11.939058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907203a37266'
down_revision = '2176283df375'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingreso', sa.Column('users_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ingreso', 'usuarios', ['users_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ingreso', type_='foreignkey')
    op.drop_column('ingreso', 'users_id')
    # ### end Alembic commands ###
