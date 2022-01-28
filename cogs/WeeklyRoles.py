import disnake
from disnake import utils, MessageInteraction
from disnake.ext import commands

class RoleButtons(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout = None)
    
    @disnake.ui.button(
        label = 'princess mononoke', 
        style = disnake.ButtonStyle.red,
        custom_id = 'wrone'
    )
    async def wrone(self, button: disnake.ui.Button, ctx: MessageInteraction):

        wrone = utils.get(ctx.guild.roles, id = 884332449637740574)
        wrtwo = utils.get(ctx.guild.roles, id = 884332552838611005)
        prison = utils.get(ctx.guild.roles, id = 892744080906416148)

        if wrone in ctx.author.roles:
            await ctx.author.remove_roles(wrone)
            await ctx.response.send_message('Removed the role <@&884332449637740574> u buffoo', ephemeral = True)
            return 
        elif (wrone not in ctx.author.roles) and (wrtwo in ctx.author.roles):
            await ctx.author.add_roles(prison)
            await ctx.author.remove_roles(wrtwo)
            await ctx.response.send_message('Enjoy your time as <@&892744080906416148>', ephemeral = True)
            return    
        await ctx.author.add_roles(wrone)
        await ctx.response.send_message('You now have the role <@&884332449637740574>', ephemeral = True)
    
    @disnake.ui.button(
        label = 'snafu',
        style = disnake.ButtonStyle.blurple,
        custom_id = 'wrtwo'
    )
    async def wrtwo(self, button: disnake.ui.Button, ctx: MessageInteraction):

        wrone = utils.get(ctx.guild.roles, id = 884332449637740574)
        wrtwo = utils.get(ctx.guild.roles, id = 884332552838611005)
        prison = utils.get(ctx.guild.roles, id = 892744080906416148)

        if wrtwo in ctx.author.roles:
            await ctx.author.remove_roles(wrtwo)
            await ctx.response.send_message('Removed the role <@&884332552838611005> u buffoo', ephemeral = True)
            return 
        elif (wrone in ctx.author.roles) and (wrtwo not in ctx.author.roles):
            await ctx.author.add_roles(prison)
            await ctx.author.remove_roles(wrone)
            await ctx.response.send_message('Enjoy your time as <@&892744080906416148>', ephemeral = True)
            return    
        await ctx.author.add_roles(wrtwo)
        await ctx.response.send_message('You now have the role <@&884332552838611005>', ephemeral = True)

class WeeklyRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        await self.bot.wait_until_ready() # or until connect
        self.bot.add_view(RoleButtons())
    
    @commands.has_guild_permissions(manage_roles = True)
    @commands.command()
    async def roles(self, ctx):
        await ctx.send('Use these buttons for roles (until android devs fix slash commands smh)', view = RoleButtons())     

def setup(bot):
    bot.add_cog(WeeklyRoles(bot))
