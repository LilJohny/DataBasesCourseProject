"""empty message

Revision ID: 45deb0364a12
Revises: a627baad15a3
Create Date: 2020-05-26 23:53:31.744910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45deb0364a12'
down_revision = 'a627baad15a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('address', sa.String(length=50), nullable=True))
    op.add_column('client', sa.Column('birth_date', sa.Date(), nullable=True))
    op.add_column('client', sa.Column('sex', sa.String(length=1), nullable=True))
    op.add_column('client', sa.Column('username', sa.String(length=30), nullable=False))
    op.create_unique_constraint(None, 'client', ['username'])
    op.add_column('friend', sa.Column('address', sa.String(length=50), nullable=True))
    op.add_column('friend', sa.Column('birth_date', sa.Date(), nullable=True))
    op.add_column('friend', sa.Column('sex', sa.String(length=1), nullable=True))
    op.add_column('friend', sa.Column('username', sa.String(length=30), nullable=False))
    op.create_unique_constraint(None, 'friend', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'friend', type_='unique')
    op.drop_column('friend', 'username')
    op.drop_column('friend', 'sex')
    op.drop_column('friend', 'birth_date')
    op.drop_column('friend', 'address')
    op.drop_constraint(None, 'client', type_='unique')
    op.drop_column('client', 'username')
    op.drop_column('client', 'sex')
    op.drop_column('client', 'birth_date')
    op.drop_column('client', 'address')
    # ### end Alembic commands ###
