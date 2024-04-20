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

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def send_sticker(ctx):
    sticker_path = 'stickers/putin.png'
    
    with open(sticker_path, 'rb') as f:
        img = Image.open(f)
        
        img = img.resize((128, 128))
        
        temp_path = 'temp_sticker.png'
        img.save(temp_path)
        
        with open(temp_path, 'rb') as resized_f:
            resized_sticker = discord.File(resized_f)
            await ctx.send(file=resized_sticker)
    
    os.remove(temp_path)

@bot.command()
async def lolhelp(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="/send_sticker", value="Send a sticker", inline=False)
    embed.add_field(name="/lolhelp", value="Show all commands", inline=False)
    await ctx.send(embed=embed)    

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Bot ID: {bot.user.id}')
    synced = await bot.tree.sync()
    print('synced command(s)', synced)

@bot.tree.command(name='sticker', description='Send a sticker')
@app_commands.describe(sticker='Sticker name')
async def sticker_putin(interaction: discord.Interaction, sticker: str):
    with open(f'putin/{sticker}.png', 'rb') as f:
        img = Image.open(f)
        img = img.resize((128, 128), Image.BICUBIC)

        img.save('test.png', 'PNG')

    
    await interaction.response.send_message(file=discord.File('temp.png'))

    os.remove('temp.png')


bot.run(get_env('DISCORD_TOKEN'))

