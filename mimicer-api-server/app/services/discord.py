from app.api_clients.discord import discord_client

class DiscordService:
    def __init__(self):
        self.client = discord_client

    def create_session_message(self, session_id: str, initiative_rolls: list, dice_roll_log: list):
        """
        Create an embed message for a DnD session displaying initiative rolls and dice roll log.

        Args:
            session_id (str): The ID of the session.
            initiative_rolls (list): List of dictionaries with 'name', 'roll', and optional 'hidden' for initiative rolls.
            dice_roll_log (list): List of dictionaries with 'name', 'action', 'roll', and optional 'hidden' for the dice roll log.
        """
        # Sort initiative rolls by roll value (descending)
        sorted_initiative = sorted(initiative_rolls, key=lambda x: x['roll'], reverse=True)
        initiative_desc = "\n".join(
            [
                f"**{item['name']}**: {item['roll'] if not item.get('hidden', False) else '???'}"
                for item in sorted_initiative
            ]
        )

        # Format dice roll log
        roll_log_desc = "\n".join(
            [
                f"**{log['name']}** rolled **{log['action']}**: {log['roll'] if not log.get('hidden', False) else '???'}"
                for log in dice_roll_log
            ]
        )

        embeds = [
            {
                "title": f"DnD Session Info: {session_id}",
                "description": "Gather your party and prepare for adventure! The session has begun!",
                "color": 0x00ff00,
                "fields": [
                    {
                        "name": "🎲 Initiative Rolls (Sorted)",
                        "value": initiative_desc or "No initiative rolls yet.",
                        "inline": False,
                    },
                    {
                        "name": "📜 Dice Roll Log",
                        "value": roll_log_desc or "No dice rolls logged yet.",
                        "inline": False,
                    },
                ],
            }
        ]

        return embeds
    
    def create_session(self, session_id: str):
        """
        Create a new DnD session.
        
        Args:
            session_id (str): The ID of the session.
        """
        embeds = self.create_session_message(session_id, [], [])
        response = self.client.send_campaign_message(embeds=embeds)
        return response.json()

    def update_session(self, message_id: str, session_id: str, initiative_rolls: list, dice_roll_log: list):
        """
        Update a DnD session.
        
        Args:
            message_id (str): The ID of the message to update.
            session_id (str): The ID of the session.
            initiative_rolls (list): List of dictionaries with 'name' and 'roll' for initiative rolls.
            dice_roll_log (list): List of dictionaries with 'name', 'action', and 'roll' for the dice roll log.
        """
        embeds = self.create_session_message(session_id, initiative_rolls, dice_roll_log)
        response = self.client.send_campaign_message(embeds=embeds, message_id=message_id)
        return response.json()

discord_service = DiscordService()
