"""Add constraint to supplier_stat

Revision ID: 1a064a7a9ffd
Revises: a1563c57883e
Create Date: 2024-06-26 10:09:33.596156

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '1a064a7a9ffd'
down_revision = 'a1563c57883e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('supplier_stat_uniquecol_key', 'supplier_stat', type_='unique')
    op.create_unique_constraint('supplier_stat_constraint', 'supplier_stat', ['authority_id', 'veh_group_id', 'circs_group_id', 'supplier_id'])
    op.drop_column('supplier_stat', 'uniquecol')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier_stat', sa.Column('uniquecol', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint('supplier_stat_constraint', 'supplier_stat', type_='unique')
    op.create_unique_constraint('supplier_stat_uniquecol_key', 'supplier_stat', ['uniquecol'])
    # ### end Alembic commands ###
