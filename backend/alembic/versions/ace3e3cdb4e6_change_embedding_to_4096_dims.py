"""change embedding to 4096 dims

Revision ID: ace3e3cdb4e6
Revises: 4edb035d8740
Create Date: 2026-02-17 20:04:31.944449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ace3e3cdb4e6'
down_revision: Union[str, Sequence[str], None] = '4edb035d8740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
