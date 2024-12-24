"""empty message

Revision ID: 8b05ce373167
Revises: 3945c9547989
Create Date: 2024-12-24 09:13:46.416814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b05ce373167'
down_revision: Union[str, None] = '3945c9547989'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
