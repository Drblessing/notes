import discord
import asyncio
from Python.env_keys import api_key

DISCORD_BOT_TOKEN = api_key("discord_bot_token")

channel = "[Enter Discord channel here]"


async def send_message(channel_id, message, bot_token):
    client = discord.Client()
    await client.login(bot_token)
    channel = await client.fetch_channel(channel_id)
    await channel.send(message)
    await client.close()


asyncio.get_event_loop().run_until_complete(
    send_message(channel, "Testing", DISCORD_BOT_TOKEN)
)
