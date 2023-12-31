"""empty message

Revision ID: 87f890d92cfa
Revises: 08c51047699f
Create Date: 2023-07-31 10:27:08.480266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f890d92cfa'
down_revision = '08c51047699f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('mass',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('skin_color',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('rotation_period',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('orbital_period',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('diameter',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('gravity',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('surface_water',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('population',
               existing_type=sa.BIGINT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('population',
               existing_type=sa.BIGINT(),
               nullable=False)
        batch_op.alter_column('surface_water',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('gravity',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('diameter',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('orbital_period',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('rotation_period',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('skin_color',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('mass',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
