"""add category to resume_chunks

Revision ID: a350450a1191
Revises: ace3e3cdb4e6
Create Date: 2026-02-17 20:36:40.068470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a350450a1191'
down_revision: Union[str, Sequence[str], None] = 'ace3e3cdb4e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "resume_chunks",
        sa.Column("category", sa.String(), nullable=True)
    )

def downgrade():
    op.drop_column("resume_chunks", "category")

