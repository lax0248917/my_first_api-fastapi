"""add content column to posts table

Revision ID: 9dce005b4531
Revises: c89667ed063f
Create Date: 2022-05-06 16:39:14.537973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dce005b4531'
down_revision = 'c89667ed063f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
