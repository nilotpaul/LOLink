import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def send_sticker(ctx):
    sticker_path = 'stickers/putin.png'
    with open(sticker_path, 'rb') as f:
        sticker = discord.File(f)
    await ctx.send(file=sticker)

@bot.command()
async def lolhelp(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="/send_sticker", value="Send a sticker", inline=False)
    await ctx.send(embed=embed)    

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Bot ID: {bot.user.id}')


bot.run(os.getenv('DISCORD_TOKEN'))

