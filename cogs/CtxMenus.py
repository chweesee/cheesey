import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands

class CtxCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name = 'Give Me Mod')
    async def gimmemod(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message('banned', ephemeral = True)

    @commands.user_command(name = 'Suspicious')
    async def sus(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message('banned', ephemeral = True)

def setup(bot):
    bot.add_cog(CtxCog(bot))



