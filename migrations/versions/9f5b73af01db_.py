"""empty message

Revision ID: 9f5b73af01db
Revises: b5b8370f9262
Create Date: 2017-05-18 16:25:08.317568

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f5b73af01db'
down_revision = 'b5b8370f9262'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_priority_areas_geometry', table_name='priority_areas')
    op.add_column('project_info', sa.Column('project_id_str', sa.String(), nullable=True))
    op.add_column('project_info', sa.Column('text_searchable', postgresql.TSVECTOR(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_info', 'text_searchable')
    op.drop_column('project_info', 'project_id_str')
    op.create_index('idx_priority_areas_geometry', 'priority_areas', ['geometry'], unique=False)
    # ### end Alembic commands ###
