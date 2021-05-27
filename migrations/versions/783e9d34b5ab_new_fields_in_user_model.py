"""new fields in user model

Revision ID: 783e9d34b5ab
Revises: 78b3bb8371f4
Create Date: 2021-05-09 19:52:30.474210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '783e9d34b5ab'
down_revision = '78b3bb8371f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###