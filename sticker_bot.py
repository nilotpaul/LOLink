from libs import *

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) # client bot initialization

@bot.command() # help commands
async def lolhelp(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="/sticker:{putin}", value="Send a funny putin sticker", inline=False)
    embed.add_field(name="/sticker:{ff}", value="Send a fucked up emoji sticker", inline=False)
    embed.add_field(name="/sticker:{meme}", value="Send a funny meme sticker", inline=False)
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
    try:
        if sticker == 'putin':
            random_value = random.randint(1, 30)
            sticker_path = f'putin/{random_value}.png'

        elif sticker == 'ff':
            random_value = random.randint(1,30)
            sticker_path = f'ff/{random_value}.png'

        elif sticker == 'meme':
            random_value = random.randint(1,30)
            sticker_path = f'meme/sticker_{random_value}.png'    

        else:
            sticker_path = f'Logo.png'

        if not os.path.exists(sticker_path):
            raise FileNotFoundError("Sticker not found")

        with open(sticker_path, 'rb') as f:
            img = Image.open(f)
            img = img.resize((128, 128), Image.BICUBIC) # resizing and saving temp img locally
            img.save('temp.png', 'PNG')

        await interaction.response.send_message(file=discord.File('temp.png')) # uploading

        os.remove('temp.png') # removing the temp img
    
    except DiscordException as e:
        logger.error(e)
        await interaction.response.send_message('Something went wrong')

    except FileNotFoundError as e:
        logger.error(e)
        await interaction.response.send_message('No sticker')        

    except Exception as e:
        logger.error(e)
        await interaction.response.send_message('Something went wrong')




bot.run(get_env('DISCORD_TOKEN'))

