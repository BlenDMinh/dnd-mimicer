import requests as re
import env

class DiscordApiClient:
    def __init__(self, token: str):
        self.token = token

    def get_oauth_url():
        url = (
            f"https://discord.com/oauth2/authorize"
            f"?client_id={env.DISCORD_CLIENT_ID}"
            f"&response_type=code"
            f"&scope=identify"
        )
        return url 
        

    def make_request(self, url: str, method: str = "GET", data: dict = None):
        print(f"Making {method} request to {url}")
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        response = re.request(method, url, headers=headers, json=data)
        return response
    
    def send_message(
        self, 
        channel_id: str, 
        message: str | None = None, 
        embeds: dict | None = None,
        message_id: str | None = None
    ):
        if(message_id):
            url = f"{env.DISCORD_API_URL}/channels/{channel_id}/messages/{message_id}"
            method = "PATCH"
        else:
            url = f"{env.DISCORD_API_URL}/channels/{channel_id}/messages"
            method = "POST"
        
        data = {
            "content": message,
            "embeds": embeds
        }

        response = self.make_request(url, method, data)
        return response
  
    def send_announcement_message(
        self, 
        message: str | None = None, 
        embeds: dict | None = None, 
        message_id: str | None = None
    ):
        return self.send_message(env.ANNOUCEMENT_CHANNEL_ID, message, embeds, message_id)

    def send_campaign_message(
        self, 
        message: str | None = None, 
        embeds: dict | None = None, 
        message_id: str | None = None
    ):
        return self.send_message(env.CAMPAIGN_CHANNEL_ID, message, embeds, message_id)

discord_client = DiscordApiClient(env.DISCORD_BOT_TOKEN)