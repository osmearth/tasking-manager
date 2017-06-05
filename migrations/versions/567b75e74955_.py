"""empty message

Revision ID: 567b75e74955
Revises: 7991a7e1b88d
Create Date: 2017-06-02 17:18:52.374843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '567b75e74955'
down_revision = '7991a7e1b88d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_registered', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('last_validation_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_validation_date')
    op.drop_column('users', 'date_registered')
    # ### end Alembic commands ###
