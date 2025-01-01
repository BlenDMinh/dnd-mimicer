from app import bot
import logging
import cron
import env

logger = logging.getLogger('discord')

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name} ({bot.user.id})")
    bot.loop.create_task(cron.start_cron())

if __name__ == '__main__':
    bot.run(env.DISCORD_BOT_TOKEN)