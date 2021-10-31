import disnake
from disnake import utils, MessageInteraction
from disnake.ext import commands

class RoleButtons(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout = None)
    
    @disnake.ui.button(
        label = 'cevala feko', 
        style = disnake.ButtonStyle.grey,
        custom_id = 'wrone'
    )
    async def wrone(self, button: disnake.ui.Button, ctx: MessageInteraction):

        wrone = utils.get(ctx.guild.roles, name = 'cevala feko')
        wrtwo = utils.get(ctx.guild.roles, name = '1969 paris wind')
        prison = utils.get(ctx.guild.roles, name = 'prisoner')

        if wrone in ctx.author.roles:
            return await ctx.response.send_message('You already have it lol.', ephemeral = True)
        elif (wrone not in ctx.author.roles) and (wrtwo in ctx.author.roles):
            await ctx.author.add_roles(prison)
            await ctx.author.remove_roles(wrtwo)
            await ctx.response.send_message('Be imprisoned.', ephemeral = True)
            return    
        await ctx.author.add_roles(wrone)
        await ctx.response.send_message('You got it mate, congrats.', ephemeral = True)
    
    @disnake.ui.button(
        label = '1969 paris wind',
        style = disnake.ButtonStyle.grey,
        custom_id = 'wrtwo'
    )
    async def wrtwo(self, button: disnake.ui.Button, ctx: MessageInteraction):

        wrone = utils.get(ctx.guild.roles, name = 'cevala feko')
        wrtwo = utils.get(ctx.guild.roles, name = '1969 paris wind')
        prison = utils.get(ctx.guild.roles, name = 'prisoner')

        if wrtwo in ctx.author.roles:
            return await ctx.response.send_message('You already have it lol.', ephemeral = True)
        elif (wrone in ctx.author.roles) and (wrtwo not in ctx.author.roles):
            await ctx.author.add_roles(prison)
            await ctx.author.remove_roles(wrone)
            await ctx.response.send_message('Be imprisoned.', ephemeral = True)
            return    
        await ctx.author.add_roles(wrtwo)
        await ctx.response.send_message('You got it mate, congrats.', ephemeral = True)

class WeeklyRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        await self.bot.wait_until_ready() # or until connect
        self.bot.add_view(RoleButtons())

    @commands.command()
    async def roles(self, ctx):
        await ctx.send('Use these buttons for roles (until android devs fix slash commands smh)', view = RoleButtons())     

def setup(bot):
    bot.add_cog(WeeklyRoles(bot))