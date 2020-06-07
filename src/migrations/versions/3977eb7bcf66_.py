"""empty message

Revision ID: 3977eb7bcf66
Revises: 7be83d6f1ea2
Create Date: 2020-05-27 02:08:15.373908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3977eb7bcf66'
down_revision = '7be83d6f1ea2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('client_mail_key', 'client', type_='unique')
    op.drop_column('client', 'mail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('mail', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.create_unique_constraint('client_mail_key', 'client', ['mail'])
    # ### end Alembic commands ###
