from api import ChannelApi, UserApi
from app import bot
import json
import logging

logger = logging.getLogger('discord.cron.metadata')

async def fetch_user():
    users = bot.get_all_members()
    users = [{
        'id': str(user.id),
        'name': user.name,
        'discriminator': user.discriminator,
        'avatar': user.display_avatar.url,
        'bot': user.bot,
        'created_at': user.created_at.timestamp(),
        'display_name': user.display_name,
        'joined_at': user.joined_at.timestamp(),
        'status': user.status.value,
    } for user in users]
    result = UserApi.update_user_batch(users)
    if result:
        logger.info('User data updated')

async def fetch_channel():
    channels = bot.get_all_channels()
    channels = [{
        'id': str(channel.id),
        'name': channel.name,
        'type': channel.type.value,
        'created_at': channel.created_at.timestamp(),
    } for channel in channels]
    result = ChannelApi.update_channel_batch(channels)
    if result:
        logger.info('Channel data updated')
