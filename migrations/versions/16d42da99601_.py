"""empty message

Revision ID: 16d42da99601
Revises: deec8123583d
Create Date: 2018-08-23 00:18:10.765086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16d42da99601'
down_revision = 'deec8123583d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('projects', sa.Column('id_custom_imagery', sa.String(), nullable=True))
    op.add_column('projects', sa.Column('id_custom_presets', sa.String(), nullable=True))
    op.add_column('projects', sa.Column('id_min_editable_zoom', sa.Integer(), nullable=True))
    
  
def downgrade():
    op.drop_column('projects', 'id_custom_imagery')
    op.drop_column('projects', 'id_custom_presets')
    op.drop_column('projects', 'id_min_editable_zoom')
    
