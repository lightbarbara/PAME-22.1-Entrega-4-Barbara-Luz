"""empty message

Revision ID: 1765e50581ac
Revises: bace00c37db0
Create Date: 2022-07-07 14:57:00.774225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1765e50581ac'
down_revision = 'bace00c37db0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cliente', 'nome',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('cliente', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('cliente', 'senha',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('cliente', 'endereco',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cliente', 'endereco',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('cliente', 'senha',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('cliente', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('cliente', 'nome',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###