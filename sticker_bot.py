import discord
from discord.ext import commands
import os
from PIL import Image

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def send_sticker(ctx):
    sticker_path = 'stickers/putin.png'
    
    # Open the image
    with open(sticker_path, 'rb') as f:
        img = Image.open(f)
        
        # Resize the image to 128x128
        img = img.resize((128, 128))
        
        # Save the resized image to a temporary file
        temp_path = 'temp_sticker.png'
        img.save(temp_path)
        
        # Send the resized image
        with open(temp_path, 'rb') as resized_f:
            resized_sticker = discord.File(resized_f)
            await ctx.send(file=resized_sticker)
    
    # Delete the temporary file
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


bot.run(os.getenv('DISCORD_TOKEN'))

