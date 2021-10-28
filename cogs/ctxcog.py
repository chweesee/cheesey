from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType
from discord_slash import SlashCommand
from discord_slash import cog_ext

import discord

from discord.ext import commands

class CtxCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ctx menu cog is now live!')
   
    guild_ids = [848576409312165908]

    @cog_ext.cog_context_menu(target=ContextMenuType.MESSAGE, name="Give me Mod", guild_ids=guild_ids)
    async def ctxtest(self, ctx: MenuContext):
        await ctx.send("banned",hidden=True)

    @cog_ext.cog_context_menu(target=ContextMenuType.USER, name="Suspicious", guild_ids=guild_ids)
    async def info(self, ctx: MenuContext):
        await ctx.send("banned",hidden=True)

def setup(bot):
    bot.add_cog(CtxCog(bot))



