import discord

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = discord.Client(intents=intents)