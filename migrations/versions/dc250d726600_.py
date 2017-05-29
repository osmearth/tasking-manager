"""empty message

Revision ID: dc250d726600
Revises: ee5315dcf3e1
Create Date: 2017-05-29 10:14:06.958352

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'dc250d726600'
down_revision = 'ee5315dcf3e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('centroid', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), nullable=True))
    op.add_column('projects', sa.Column('geometry', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=4326), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'geometry')
    op.drop_column('projects', 'centroid')
    # ### end Alembic commands ###
