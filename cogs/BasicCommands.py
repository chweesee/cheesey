import disnake
from disnake.ext import commands

class General(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        '''Use this to check ping! Usage: $ping'''
        await ctx.send(f'🏓 ({self.bot.latency*1000}ms)')
        

def setup(bot):
    bot.add_cog(General(bot))