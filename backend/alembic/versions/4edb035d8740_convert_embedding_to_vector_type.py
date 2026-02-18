"""convert embedding to vector type

Revision ID: 4edb035d8740
Revises: 9e3e40d83a47
Create Date: 2026-02-17 18:38:53.080729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4edb035d8740'
down_revision: Union[str, Sequence[str], None] = '9e3e40d83a47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        "ALTER TABLE resume_chunks "
        "ALTER COLUMN embedding TYPE vector(4096) "
        "USING embedding::vector;"
    )

def downgrade():
    op.execute(
        "ALTER TABLE resume_chunks "
        "ALTER COLUMN embedding TYPE vector(1536) "
        "USING embedding::vector;"
    )
