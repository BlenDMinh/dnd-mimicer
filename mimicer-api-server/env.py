import dotenv
import os

env_vairables = dotenv.dotenv_values()

def get_env(key: str, default=None):
    if not default and key not in env_vairables and key not in os.environ:
        raise ValueError(f"Environment variable {key} is required.")
    
    return env_vairables.get(key, os.environ.get(key, default))

API_PORT = int(get_env("API_PORT", 8000))
API_KEY = get_env("API_KEY")
# DB_URL = get_env("DB_URL", "sqlite:///./app .db")
__POSTGRES_USER = get_env("POSTGRES_USER")
__POSTGRES_PASSWORD = get_env("POSTGRES_PASSWORD")
__POSTGRES_DB = get_env("POSTGRES_DB")
__POSTGRES_HOSTNAME = get_env("POSTGRES_HOSTNAME", "database")
__POSTGRES_PORT = get_env("POSTGRES_PORT","5432")
DB_URL=f'postgresql://{__POSTGRES_USER}:{__POSTGRES_PASSWORD}@{__POSTGRES_HOSTNAME}:{__POSTGRES_PORT}/{__POSTGRES_DB}'
DISCORD_BOT_TOKEN = get_env("DISCORD_BOT_TOKEN")
DISCORD_API_URL = get_env("DISCORD_API_URL", "https://discord.com/api/v10")
ANNOUCEMENT_CHANNEL_ID = get_env("ANNOUCEMENT_CHANNEL_ID")
CAMPAIGN_CHANNEL_ID = get_env("CAMPAIGN_CHANNEL_ID")
REDIS_HOST = get_env("REDIS_HOST")
REDIS_PORT = int(get_env("REDIS_PORT"))
JWT_KEY = get_env("JWT_KEY", "veryverysecretkey")
JWT_ALGO = get_env("JWT_ALGO", "HS256")