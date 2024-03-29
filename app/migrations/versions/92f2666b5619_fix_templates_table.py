"""fix templates table

Revision ID: 92f2666b5619
Revises: 5492265ba3ba
Create Date: 2023-11-15 23:46:48.928184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92f2666b5619'
down_revision: Union[str, None] = '5492265ba3ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('templates', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_constraint('templates_document_id_key', 'templates', type_='unique')
    op.drop_constraint('templates_user_id_fkey', 'templates', type_='foreignkey')
    op.drop_column('templates', 'document_id')
    op.drop_column('templates', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('templates', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('templates', sa.Column('document_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('templates_user_id_fkey', 'templates', 'users', ['user_id'], ['id'])
    op.create_unique_constraint('templates_document_id_key', 'templates', ['document_id'])
    op.alter_column('templates', 'id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
