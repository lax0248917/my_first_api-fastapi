"""add foreign-key to post table

Revision ID: 2b790650c6b5
Revises: 05f00e77e170
Create Date: 2022-05-06 16:53:07.792079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b790650c6b5'
down_revision = '05f00e77e170'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
