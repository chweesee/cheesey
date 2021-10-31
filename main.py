import disnake
from disnake.ext import commands
from disnake.utils import get
from disnake import member

import os

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('$'), 
    test_guilds = [848576409312165908, 848098024164294657]
)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename[:-3]}.')

@bot.event
async def on_ready():
    await bot.change_presence(
        status = disnake.Status.idle, 
        activity = disnake.Activity(type = disnake.ActivityType.watching, name = "paneer.")
    )
    print("Bot is ready!")
    print('------')
    print(f'Logged in as {bot.user}! (Bot ID: {bot.user.id})')

# @bot.event
# async def on_message(message):
#     if message.author.id == 359812392504524811:
#         await message.reply("sus - https://i.imgur.com/0RazNSS.gif")
#     await bot.process_commands(message)
    
@bot.command()
@commands.has_permissions(ban_members = True)
async def load(ctx, extension):
    """Use this to load cogs. Usage: $load <cog_name>"""
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now loaded!')


@bot.command()
@commands.has_permissions(kick_members = True)
async def unload(ctx, extension):
    """Use this to unload cogs. Usage: $unload <cog_name>"""
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now unloaded!')

@bot.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    """Use this to reload individual cogs. Usage: $reload <cog_name>"""
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now reloaded!')

@bot.command()
@commands.has_permissions(administrator = True)
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Cog {filename[:-3]} is now reloaded!')

token = os.environ.get('BOT_TOKEN')
bot.run(token)
