"""installation

Revision ID: 5881e16a9d
Revises: 
Create Date: 2015-09-05 00:13:30.639058

"""

# revision identifiers, used by Alembic.
revision = '5881e16a9d'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_protocol_irc_channels_network_id'), 'protocol_irc_channels', ['network_id'], unique=False)
    op.create_index(op.f('ix_protocol_irc_channels_user_id'), 'protocol_irc_channels', ['user_id'], unique=False)
    op.drop_index('network', table_name='protocol_irc_channels')
    op.drop_index('user', table_name='protocol_irc_channels')
    op.create_index(op.f('ix_protocol_irc_networks_autojoin'), 'protocol_irc_networks', ['autojoin'], unique=False)
    op.create_index(op.f('ix_protocol_irc_networks_nick_id'), 'protocol_irc_networks', ['nick_id'], unique=False)
    op.create_index(op.f('ix_protocol_irc_networks_user_id'), 'protocol_irc_networks', ['user_id'], unique=False)
    op.drop_index('nick', table_name='protocol_irc_networks')
    op.drop_index('user', table_name='protocol_irc_networks')
    op.create_index(op.f('ix_system_protocols_enabled'), 'system_protocols', ['enabled'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_system_protocols_enabled'), table_name='system_protocols')
    op.create_index('user', 'protocol_irc_networks', ['user_id'], unique=False)
    op.create_index('nick', 'protocol_irc_networks', ['nick_id'], unique=False)
    op.drop_index(op.f('ix_protocol_irc_networks_user_id'), table_name='protocol_irc_networks')
    op.drop_index(op.f('ix_protocol_irc_networks_nick_id'), table_name='protocol_irc_networks')
    op.drop_index(op.f('ix_protocol_irc_networks_autojoin'), table_name='protocol_irc_networks')
    op.create_index('user', 'protocol_irc_channels', ['user_id'], unique=False)
    op.create_index('network', 'protocol_irc_channels', ['network_id'], unique=False)
    op.drop_index(op.f('ix_protocol_irc_channels_user_id'), table_name='protocol_irc_channels')
    op.drop_index(op.f('ix_protocol_irc_channels_network_id'), table_name='protocol_irc_channels')
    ### end Alembic commands ###
