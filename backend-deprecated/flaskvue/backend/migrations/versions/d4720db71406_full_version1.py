"""full_version1

Revision ID: d4720db71406
Revises: 
Create Date: 2021-08-05 23:13:59.774677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4720db71406'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matched',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.String(length=120), nullable=True),
    sa.Column('request_timestamp', sa.DateTime(), nullable=True),
    sa.Column('match_id_timestamp', sa.DateTime(), nullable=True),
    sa.Column('sponsor_id', sa.Integer(), nullable=True),
    sa.Column('assistor_id_pair', sa.Integer(), nullable=True),
    sa.Column('Matched_id_file', sa.Text(), nullable=True),
    sa.Column('matched_done', sa.Integer(), nullable=True),
    sa.Column('sponsor_random_id', sa.String(length=120), nullable=True),
    sa.Column('assistor_random_id_pair', sa.String(length=120), nullable=True),
    sa.Column('test_indicator', sa.String(length=10), nullable=True),
    sa.Column('test_id', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_matched_match_id_timestamp'), 'matched', ['match_id_timestamp'], unique=False)
    op.create_index(op.f('ix_matched_request_timestamp'), 'matched', ['request_timestamp'], unique=False)
    op.create_index(op.f('ix_matched_task_id'), 'matched', ['task_id'], unique=False)
    op.create_index(op.f('ix_matched_test_id'), 'matched', ['test_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('last_requests_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_matched_file_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_situation_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_output_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_test_requests_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_test_matched_file_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_test_output_read_time', sa.DateTime(), nullable=True),
    sa.Column('last_messages_read_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('situation_timestamp', sa.DateTime(), nullable=True),
    sa.Column('output_timestamp', sa.DateTime(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('sender_random_id', sa.String(length=120), nullable=True),
    sa.Column('assistor_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.String(length=120), nullable=True),
    sa.Column('rounds', sa.Integer(), nullable=True),
    sa.Column('situation', sa.Text(), nullable=True),
    sa.Column('output', sa.Text(), nullable=True),
    sa.Column('test_indicator', sa.String(length=10), nullable=True),
    sa.Column('test_id', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['assistor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_output_timestamp'), 'messages', ['output_timestamp'], unique=False)
    op.create_index(op.f('ix_messages_situation_timestamp'), 'messages', ['situation_timestamp'], unique=False)
    op.create_index(op.f('ix_messages_task_id'), 'messages', ['task_id'], unique=False)
    op.create_index(op.f('ix_messages_test_id'), 'messages', ['test_id'], unique=False)
    op.create_index(op.f('ix_messages_timestamp'), 'messages', ['timestamp'], unique=False)
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.Float(), nullable=True),
    sa.Column('payload_json', sa.Text(), nullable=True),
    sa.Column('sender_random_id_list', sa.Text(), nullable=True),
    sa.Column('task_id_list', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notifications_name'), 'notifications', ['name'], unique=False)
    op.create_index(op.f('ix_notifications_timestamp'), 'notifications', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notifications_timestamp'), table_name='notifications')
    op.drop_index(op.f('ix_notifications_name'), table_name='notifications')
    op.drop_table('notifications')
    op.drop_index(op.f('ix_messages_timestamp'), table_name='messages')
    op.drop_index(op.f('ix_messages_test_id'), table_name='messages')
    op.drop_index(op.f('ix_messages_task_id'), table_name='messages')
    op.drop_index(op.f('ix_messages_situation_timestamp'), table_name='messages')
    op.drop_index(op.f('ix_messages_output_timestamp'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_matched_test_id'), table_name='matched')
    op.drop_index(op.f('ix_matched_task_id'), table_name='matched')
    op.drop_index(op.f('ix_matched_request_timestamp'), table_name='matched')
    op.drop_index(op.f('ix_matched_match_id_timestamp'), table_name='matched')
    op.drop_table('matched')
    # ### end Alembic commands ###