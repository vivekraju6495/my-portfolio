"""add category to resume_chunks

Revision ID: 371171a9b13c
Revises: a350450a1191
Create Date: 2026-02-17 20:37:13.041577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '371171a9b13c'
down_revision: Union[str, Sequence[str], None] = 'a350450a1191'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "resume_chunks",
        sa.Column("categorys", sa.String(), nullable=True)
    )

def downgrade():
    op.drop_column("resume_chunks", "categorys")
