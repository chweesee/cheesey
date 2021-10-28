import disnake
import os
from disnake.ext import commands
from discord_slash import SlashCommand
from discord_components import DiscordComponents, ComponentsBot, Button
from disnake.utils import get
from disnake import member

bot = commands.Bot(command_prefix=['$','@cheesey#6908','@cheesey#6908 '])
slash=SlashCommand(bot, sync_on_cog_reload=True)
DiscordComponents(bot)
#bot.remove_command('help')


@bot.event
async def on_ready():
    activity = disnake.Game(name="watching paneer", type=3)
    await bot.change_presence(status=disnake.Status.idle, activity=activity)
    print("Bot is ready!")
    print(f'Logged in as {bot.user}! (Bot ID: {bot.user.id})')
    print('------')

#@bot.event
#async def on_message(message):
 #   if message.author.id == 359812392504524811:
  #      await message.reply("sus - https://i.imgur.com/0RazNSS.gif")
   # await bot.process_commands(message)
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    """Use this to load cogs. Usage: $load <cog_name>"""
    await ctx.send(f'Cog {extension} is now loaded!')
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def unload(ctx, extension):
    """Use this to unload cogs. Usage: $unload <cog_name>"""
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now unloaded!')

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    """Use this to reload individual cogs. Usage: $reload <cog_name>"""
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension } is now reloaded!')

@bot.command()
@commands.has_permissions(administrator=True)
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Cog {filename[:-3]} is now reloaded!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
@commands.has_permissions(administrator=True)
async def roles(ctx):
    await ctx.send("Use these buttons for roles (until android devs fix slash commands smh)", components=[Button(label="1969 paris wind", custom_id="884332552838611005"),Button(label="cevala feko", custom_id="884332449637740574")])
    while True:    
        interaction = await bot.wait_for(
            "button_click", check=lambda inter: inter.custom_id == "884332552838611005"
        )
        member=interaction.author.id
        
        #role 1 cases
        #check for only member
        if interaction.author.top_role.id == 872122050418995280:
            await interaction.author.add_roles(get(interaction.guild.roles, id=884332552838611005))
            await interaction.send(f"You now have the role <@&884332552838611005>")
        
        #booster check
        elif interaction.author.top_role.id == 866563743399804930:
            await interaction.author.add_roles(get(interaction.guild.roles, id=884332552838611005))
            await interaction.send(f"You now have the role <@&884332552838611005>")            
            
        #check for has role 2
        elif interaction.author.top_role.id == 884332449637740574:
            await interaction.author.add_roles(get(interaction.guild.roles, id=892744080906416148))
            await interaction.author.remove_roles(get(interaction.guild.roles, id=884332449637740574))
            await interaction.send(f"Enjoy your time as a <@&892744080906416148>")
            
        
                   
        interaction = await bot.wait_for(
            "button_click", check=lambda inter: inter.custom_id == "884332449637740574"
        )
        member=interaction.author.id
        
        #role 2
        #check for member
        if interaction.author.top_role.id == 872122050418995280:
            await interaction.author.add_roles(get(interaction.guild.roles, id=884332449637740574))
            await interaction.send(f"You now have the role <@&884332449637740574>")
        
        #booster check
        elif interaction.author.top_role.id == 866563743399804930:
            await interaction.author.add_roles(get(interaction.guild.roles, id=884332449637740574))
            await interaction.send(f"You now have the role <@&884332449637740574>")            
            
        #check for has role 2
        elif interaction.author.top_role.id == 884332552838611005:
            await interaction.author.add_roles(get(interaction.guild.roles, id=892744080906416148))
            await interaction.author.remove_roles(get(interaction.guild.roles, id=884332552838611005))
            await interaction.send(f"Enjoy your time as a <@&892744080906416148>")
    
token = os.environ.get('BOT_TOKEN')
bot.run(token)
