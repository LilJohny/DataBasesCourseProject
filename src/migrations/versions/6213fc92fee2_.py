"""empty message

Revision ID: 6213fc92fee2
Revises: 3e19b4a212b6
Create Date: 2020-05-27 02:07:48.459464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6213fc92fee2'
down_revision = '3e19b4a212b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('address', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
