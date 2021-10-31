import disnake
from disnake.ext import commands
from disnake.utils import get
from disnake import ApplicationCommandInteraction, Option, OptionType, OptionChoice

import asyncio

class SlashCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    times_slash_linkoss_used = 0

    @commands.slash_command(
        name = 'linkoss',
        description = 'Remind Linkoss to drink tea!'
    )
    async def tea(self, ctx: ApplicationCommandInteraction):
        global times_slash_linkoss_used
        if times_slash_linkoss_used <= 9:
            global times_slash_linkoss_used
            times_slash_linkoss_used += 1
            await ctx.response.send_message('<@359812392504524811> Reminder to drink tea')
        else:
            await ctx.response.send_message('Linkoss has had enough tea already :slight_smile:')
            await asyncio.sleep(20)
            global times_slash_linkoss_used
            times_slash_linkoss_used = 0

    @commands.slash_command(
        name = 'ping',
        description = 'Check bot ping.'
    )
    async def ping(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message(f'🏓 ({self.bot.latency*1000}ms)', ephemeral = True)

    @commands.slash_command(
        name = 'roles',
        description = 'Command for weeekly roles!',
        options = [
            Option(
                name = 'rolename', 
                description = 'Use this to select your role.', 
                required = True,
                choices = [
                    OptionChoice(name = '1969 paris wind', value = 'wr1'),
                    OptionChoice(name = 'cevalafeko', value = 'wr2')
                ]
            )
        ]
    )
    async def giverole(self, ctx: ApplicationCommandInteraction, rolename: str):
        member = ctx.author.id if isinstance(ctx.author, disnake.Member) else ctx.author
        if rolename == 'wr1':
            weeklyrole1 = get(ctx.guild.roles, id = 884332552838611005)
            await ctx.author.add_roles(weeklyrole1)
            await ctx.response.send_message(f'You now have the role <@&884332552838611005>', ephemeral = True)
        elif rolename == 'wr2':
            weeklyrole2 = get(ctx.guild.roles, id = 884332449637740574)
            await ctx.author.add_roles(weeklyrole2)
            await ctx.response.send_message(f'You now have the role <@&884332449637740574>', ephemeral = True)

# Didn't remove this code for reference :P
# @commands.has_permissions(ban_members=true)
# @cog_ext.cog_slash(name='rolereplace',description='Command for replacing weeekly roles!',options=[create_option(name='rolename1',description='Use this to enter new role names your role.',option_type=3,required=False)
#                 create_option(name='rolename2',description='Use this to enter new role names your role.',option_type=3,required=False)], guild_ids=guild_ids )

def setup(bot):
    bot.add_cog(SlashCog(bot))
