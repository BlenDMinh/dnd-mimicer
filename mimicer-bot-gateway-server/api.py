import logging
import requests as re
import env

logger = logging.getLogger('discord.api')

class UserApi:
    @staticmethod
    def get_users():
        response = re.get(f'{env.API_HOST}/users?api_key={env.API_KEY}')
        return response.json()

    @staticmethod
    def update_user_batch(users):
        json_data = {
            'users': users
        }
        response = re.put(f'{env.API_HOST}/users/update_batch?api_key={env.API_KEY}', json=json_data)
        return response.json()

class ChannelApi:
    @staticmethod
    def get_channels():
        response = re.get(f'{env.API_HOST}/channels?api_key={env.API_KEY}')
        if response.status_code != 200:
            logger.error(f'Error {response.status_code}: {response.json()}')
            return None
        return response.json()

    @staticmethod
    def update_channel_batch(channels):
        json_data = {
            'channels': channels
        }
        response = re.put(f'{env.API_HOST}/channels/update_batch?api_key={env.API_KEY}', json=json_data)
        if response.status_code != 200:
            logger.error(f'Error {response.status_code}: {response.json()}')
            return None
        return response.json()

class CronJobApi:
    @staticmethod
    def get_cronjobs():
        response = re.get(f'{env.API_HOST}/cronjobs?api_key={env.API_KEY}')
        return response.json()