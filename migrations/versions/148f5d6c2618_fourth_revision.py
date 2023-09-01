"""fourth revision

Revision ID: 148f5d6c2618
Revises: c0eda1b072d3
Create Date: 2023-09-01 04:38:43.329836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '148f5d6c2618'
down_revision: Union[str, None] = 'c0eda1b072d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_bug_created_at'), 'bug', ['created_at'], unique=False)
    op.create_index(op.f('ix_bug_updated_at'), 'bug', ['updated_at'], unique=False)
    op.create_index(op.f('ix_story_created_at'), 'story', ['created_at'], unique=False)
    op.create_index(op.f('ix_story_updated_at'), 'story', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_story_updated_at'), table_name='story')
    op.drop_index(op.f('ix_story_created_at'), table_name='story')
    op.drop_index(op.f('ix_bug_updated_at'), table_name='bug')
    op.drop_index(op.f('ix_bug_created_at'), table_name='bug')
    # ### end Alembic commands ###