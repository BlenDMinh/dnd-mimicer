import os
import dotenv

env_vairables = dotenv.dotenv_values()

# Load environment variables from .env file into a dictionary (without affecting the global environment)
def get_env(key: str, default=None):
    if not default and key not in env_vairables and key not in os.environ:
        raise ValueError(f"Environment variable {key} is required.")
    
    return env_vairables.get(key, os.environ.get(key, default))

API_HOST = get_env('API_URL', 'http://localhost:8000')
API_KEY = get_env('API_KEY')
DISCORD_BOT_TOKEN = get_env('DISCORD_BOT_TOKEN')
ANNOUCEMENT_CHANNEL_ID = get_env('ANNOUCEMENT_CHANNEL_ID')
CAMPAIGN_CHANNEL_ID = get_env("CAMPAIGN_CHANNEL_ID")
