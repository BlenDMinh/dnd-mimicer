from datetime import datetime, timedelta
import discord
from discord import app_commands
import random

import env

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    channel = bot.get_channel(int(env.ANNOUCEMENT_CHANNEL_ID))

    # Replace this with your desired date format
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    # Arrays of possible messages and thumbnails
    message_options = [
        "The realm awaits your decision! Shall we gather around the table of destiny?",
        "The dragons are ready for battle, but your vote determines if we march to war!",
        "The adventure of a lifetime awaits, but only if you decide to roll the dice!",
        "Gather around, adventurers! The fate of the realm lies in your hands!"
    ]
    thumbnail_options = [
        "https://i.imgur.com/MaoXBkH.jpeg",
        "https://i.imgur.com/11102OS.jpeg",
        "https://i.imgur.com/Xvelugj.jpeg",
        "https://i.imgur.com/66gzC9x.jpeg"
    ]
    yes_poll_options = [
        ("✅✅✅ YES YES YES", "Let's go! The dice will roll!"),
        ("🎲🎲🎲 Absolutely YES!", "The dice gods are calling!"),
    ]

    no_poll_options = [
        ("❌❌❌ Go *** yourself", "No DnD for now, maybe next time."),
        ("🛑🛑🛑 Not this time", "We'll wait for the next quest.")
    ]

    # Randomly pick a message, thumbnail, and poll options
    random_message = random.choice(message_options)
    random_thumbnail = random.choice(thumbnail_options)

    # Create the embed with random selections
    embed = discord.Embed(
        title="📊 DnD Session Poll 🎲",
        description=(
            f"**Adventurers!** 🧙‍♂️⚔️\n\n"
            f"{random_message}\n"
            f"Proposed date: **{current_date}**\n\n"
            f"React below to cast your vote:\n"
            f"✅ - **Yes, let the dice roll!**\n"
            f"❌ - **No, the dragons must wait.**"
        ),
        color=discord.Color.gold()
    )
    embed.set_thumbnail(url=random_thumbnail)

    # Send the embed message
    poll_message = await channel.send(embed=embed)

    # Create and send the poll with random answers
    poll = discord.Poll(
        question="📊 DnD Session Poll 🎲",
        duration=timedelta(hours=16),
    )
    poll.add_answer(text=yes_poll_options[random.randint(0, len(yes_poll_options) - 1)][0])
    poll.add_answer(text=no_poll_options[random.randint(0, len(no_poll_options) - 1)][0])
    await channel.send(poll=poll)

bot.run(env.DISCORD_BOT_TOKEN)