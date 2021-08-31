"""Constrained rank

Revision ID: 4dbf012a9e9d
Revises: 6d41b0c81973
Create Date: 2021-08-31 15:57:21.596591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dbf012a9e9d'
down_revision = '6d41b0c81973'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
            "positiverank", "span", "rank>0"
        )
    op.create_check_constraint(
            "positiverank", "split", "rank>0"
        )

def downgrade():
    op.drop_constraint("positiverank","span")
    op.drop_constraint("positiverank","split")
