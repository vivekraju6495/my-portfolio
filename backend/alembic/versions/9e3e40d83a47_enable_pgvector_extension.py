"""enable pgvector extension

Revision ID: 9e3e40d83a47
Revises: 53eef5dc3a46
Create Date: 2026-02-17 18:23:33.061702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e3e40d83a47'
down_revision: Union[str, Sequence[str], None] = '53eef5dc3a46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS vector;")
