import logging

logger = logging.getLogger('discord.cron.test')

async def test_task():
    logger.info('Test task')