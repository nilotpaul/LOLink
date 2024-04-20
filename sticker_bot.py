import discord
from discord.ext import commands
from discord import app_commands
from PIL import Image
from utils.env import get_env
import os
import io

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) # client bot initialization

@bot.command() # help commands
async def lolhelp(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="/sticker:{name}", value="Send a sticker", inline=False)
    embed.add_field(name="/lolhelp", value="Show all commands", inline=False)
    await ctx.send(embed=embed)    

@bot.event
async def on_ready(): # on successfull connection
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Bot ID: {bot.user.id}')
    synced = await bot.tree.sync() # sync commands on every connect
    print('synced command(s)', synced)

@bot.tree.command(name='sticker', description='Send a sticker') # sticker command autocomplete
@app_commands.describe(sticker='Sticker name')
async def sticker_putin(interaction: discord.Interaction, sticker: str):
    with open(f'putin/{sticker}.png', 'rb') as f:
        img = Image.open(f)
        img = img.resize((128, 128), Image.BICUBIC) # resizing and saving temp img locally

        img.save('temp.png', 'PNG')

    
    await interaction.response.send_message(file=discord.File('temp.png')) # uploading

    os.remove('temp.png') # removing the temp img


bot.run(get_env('DISCORD_TOKEN'))

