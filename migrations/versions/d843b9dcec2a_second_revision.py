"""second revision

Revision ID: d843b9dcec2a
Revises: d286f7d2176d
Create Date: 2023-09-01 04:36:57.221164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd843b9dcec2a'
down_revision: Union[str, None] = 'd286f7d2176d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('story',
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_story_created_at'), 'story', ['created_at'], unique=False)
    op.create_index(op.f('ix_story_id'), 'story', ['id'], unique=False)
    op.create_table('bug',
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['story_id'], ['story.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bug_created_at'), 'bug', ['created_at'], unique=False)
    op.create_index(op.f('ix_bug_id'), 'bug', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bug_id'), table_name='bug')
    op.drop_index(op.f('ix_bug_created_at'), table_name='bug')
    op.drop_table('bug')
    op.drop_index(op.f('ix_story_id'), table_name='story')
    op.drop_index(op.f('ix_story_created_at'), table_name='story')
    op.drop_table('story')
    # ### end Alembic commands ###
