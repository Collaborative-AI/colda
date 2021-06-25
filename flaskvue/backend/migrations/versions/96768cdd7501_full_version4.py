"""full_version4

Revision ID: 96768cdd7501
Revises: 8bc1ec6c4bcd
Create Date: 2021-06-24 22:17:03.611883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96768cdd7501'
down_revision = '8bc1ec6c4bcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sender_random_id', sa.String(length=120), nullable=True))

    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sender_random_id_list', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('task_id_list', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.drop_column('task_id_list')
        batch_op.drop_column('sender_random_id_list')

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('sender_random_id')

    # ### end Alembic commands ###
