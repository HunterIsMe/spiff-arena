"""empty message

Revision ID: 844cee572018
Revises: 57df21dc569d
Create Date: 2023-09-07 14:18:12.357989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844cee572018'
down_revision = '57df21dc569d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=255), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'key', name='user_id_key_uniq')
    )
    with op.batch_alter_table('user_property', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_property_key'), ['key'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_property_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_property', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_property_user_id'))
        batch_op.drop_index(batch_op.f('ix_user_property_key'))

    op.drop_table('user_property')
    # ### end Alembic commands ###