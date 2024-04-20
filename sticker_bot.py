from utils.env import get_env
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!send_sticker'):
        await message.channel.send(file=discord.File("stickers\sticker_3.png"))

client.run(os.getenv('DISCORD_TOKEN'))
