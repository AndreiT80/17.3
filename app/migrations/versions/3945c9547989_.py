"""empty message

Revision ID: 3945c9547989
Revises: 229ba75a3af6
Create Date: 2024-12-24 09:13:07.075030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3945c9547989'
down_revision: Union[str, None] = '229ba75a3af6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
