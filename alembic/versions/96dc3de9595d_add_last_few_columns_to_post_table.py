"""add last few columns to post table

Revision ID: 96dc3de9595d
Revises: 2b790650c6b5
Create Date: 2022-05-06 16:57:43.285744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96dc3de9595d'
down_revision = '2b790650c6b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
