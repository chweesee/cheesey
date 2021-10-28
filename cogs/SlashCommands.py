from disnake import member
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
import disnake
from disnake.utils import get

from disnake.ext import commands

class SlashCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Slash Commands cog is now live!')
   
    guild_ids = [848576409312165908,848098024164294657]

    @cog_ext.cog_slash(name="linkoss", description="Remind Linkoss to drink tea!", guild_ids=guild_ids)
    async def tea(self, ctx: SlashContext):
        i = 1
        if i <= 9:
            i = i+1
            await ctx.send("<@359812392504524811> Reminder to drink tea")
        else:
            await ctx.send("Linkoss has had enough tea already :slight_smile:")

    @cog_ext.cog_slash(name="ping", description="Check bot ping", guild_ids=guild_ids)
    async def ping(self, ctx: SlashContext):
        await ctx.send(f"🏓 ({self.bot.latency*1000}ms)",hidden=True)

    @cog_ext.cog_slash(name="roles",description="Command for weeekly roles!",options=[create_option(name="rolename",description="Use this to select your role.",option_type=3,required=True,
                 choices=
                 [
                  create_choice(
                    name="1969 paris wind",
                    value="wr1"
                  )
                  ,
                  create_choice(
                    name="cevala feko",
                    value="wr2"
                  )
                ])], guild_ids=guild_ids )
    async def giverole(self, ctx, rolename: str):
        member = ctx.author.id if isinstance(ctx.author, discord.Member) else ctx.author
        if rolename == "wr1":
            weeklyrole1 = get(ctx.guild.roles, id=884332552838611005)
            await ctx.author.add_roles(weeklyrole1)
            await ctx.send(f"You now have the role <@&884332552838611005>", hidden=True)
        elif rolename == "wr2":
            weeklyrole2 = get(ctx.guild.roles, id=884332449637740574)
            await ctx.author.add_roles(weeklyrole2)
            await ctx.send(f"You now have the role <@&884332449637740574>", hidden=True)

#@commands.has_permissions(ban_members=true)
#@cog_ext.cog_slash(name="rolereplace",description="Command for replacing weeekly roles!",options=[create_option(name="rolename1",description="Use this to enter new role names your role.",option_type=3,required=False)
  #              create_option(name="rolename2",description="Use this to enter new role names your role.",option_type=3,required=False)], guild_ids=guild_ids )

def setup(bot):
    bot.add_cog(SlashCog(bot))
