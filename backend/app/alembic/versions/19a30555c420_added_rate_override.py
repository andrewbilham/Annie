"""added rate override

Revision ID: 19a30555c420
Revises: 55e3e7adc035
Create Date: 2024-06-27 13:34:52.105505

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '19a30555c420'
down_revision = '55e3e7adc035'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier_rate', sa.Column('rate_override', sqlmodel.sql.sqltypes.AutoString(), server_default='No', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier_rate', 'rate_override')
    # ### end Alembic commands ###
