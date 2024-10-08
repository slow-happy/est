"""empty message

Revision ID: f33922b46186
Revises: 64951165525e
Create Date: 2024-07-03 20:50:50.988137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f33922b46186'
down_revision = '64951165525e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales_group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curr_lv1', sa.String(length=3), nullable=True))
        batch_op.add_column(sa.Column('curr_lv2', sa.String(length=3), nullable=True))
        batch_op.add_column(sa.Column('curr_lv3', sa.String(length=3), nullable=True))
        batch_op.add_column(sa.Column('curr_lv4', sa.String(length=3), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales_group', schema=None) as batch_op:
        batch_op.drop_column('curr_lv4')
        batch_op.drop_column('curr_lv3')
        batch_op.drop_column('curr_lv2')
        batch_op.drop_column('curr_lv1')

    # ### end Alembic commands ###
