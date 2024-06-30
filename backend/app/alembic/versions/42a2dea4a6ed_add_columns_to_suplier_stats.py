"""Add columns to suplier stats

Revision ID: 42a2dea4a6ed
Revises: f327615111b1
Create Date: 2024-06-24 20:50:06.908063

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '42a2dea4a6ed'
down_revision = 'f327615111b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier_stat', sa.Column('rate_rank', sa.Integer(), nullable=True))
    op.add_column('supplier_stat', sa.Column('daystohire', sa.Integer(), nullable=True))
    op.add_column('supplier_stat', sa.Column('daystohire_rank', sa.Integer(), nullable=True))
    op.add_column('supplier_stat', sa.Column('conversion', sa.Integer(), nullable=True))
    op.add_column('supplier_stat', sa.Column('conversion_rank', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier_stat', 'conversion_rank')
    op.drop_column('supplier_stat', 'conversion')
    op.drop_column('supplier_stat', 'daystohire_rank')
    op.drop_column('supplier_stat', 'daystohire')
    op.drop_column('supplier_stat', 'rate_rank')
    # ### end Alembic commands ###