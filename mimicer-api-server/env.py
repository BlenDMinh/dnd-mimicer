import dotenv
import os

env_vairables = dotenv.dotenv_values()

def get_env(key: str, default=None):
    if not default and key not in env_vairables and key not in os.environ:
        raise ValueError(f"Environment variable {key} is required.")
    
    return env_vairables.get(key, os.environ.get(key, default))

API_PORT = int(get_env("API_PORT", 8000))
API_KEY = get_env("API_KEY")
DB_URL = get_env("DB_URL", "sqlite:///./app.db")
DISCORD_BOT_TOKEN = get_env("DISCORD_BOT_TOKEN")
DISCORD_API_URL = get_env("DISCORD_API_URL", "https://discord.com/api/v10")
ANNOUCEMENT_CHANNEL_ID = get_env("ANNOUCEMENT_CHANNEL_ID")
CAMPAIGN_CHANNEL_ID = get_env("CAMPAIGN_CHANNEL_ID")
REDIS_HOST = get_env("REDIS_HOST")
REDIS_PORT = int(get_env("REDIS_PORT"))
