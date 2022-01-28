import disnake
from disnake.ext import commands
from disnake.utils import get
from disnake import ApplicationCommandInteraction, Option, OptionType, OptionChoice
from disnake import utils

class SlashCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name = 'linkoss',
        description = 'Remind Linkoss to drink tea!'
    )
    @commands.cooldown(10, 30, commands.BucketType.channel)
    async def tea(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message('<@359812392504524811> Reminder to drink tea')
    
    @tea.error
    async def nomentionlinkoss(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.response.send_message(f'Linkoss can drink tea again after {error.retry_after}s. :slight_smile:')

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
                name = 'roleid', 
                description = 'Use this to select your role.', 
                required = True,
                choices = [
                    OptionChoice(name = 'princess mononoke', value = '884332449637740574'),
                    OptionChoice(name = 'snafu', value = '884332552838611005')
                ]
            )
        ]
    )
    async def giverole(self, ctx: ApplicationCommandInteraction, roleid: str):
        member = ctx.author.id if isinstance(ctx.author, disnake.Member) else ctx.author
        weeklyrole1 = get(ctx.guild.roles, id = 884332449637740574)
        weeklyrole2 = get(ctx.guild.roles, id = 884332552838611005)
        role = get(ctx.guild.roles, id = int(roleid))
        prisoner = get(ctx.guild.roles, id = 892744080906416148)
        if (weeklyrole1 not in ctx.author.roles) and (weeklyrole2 not in ctx.author.roles):
            await ctx.author.add_roles(role)
            await ctx.response.send_message(f'You now have the role <@&{roleid}>', ephemeral = True)
        elif ((weeklyrole1 in ctx.author.roles) and (role == weeklyrole1)) or ((weeklyrole2 in ctx.author.roles) and (role == weeklyrole2)):
            await ctx.author.remove_roles(role)
            await ctx.response.send_message(f'Removed the role <@&{roleid}> u buffoo', ephemeral = True)
        elif ((weeklyrole1 in ctx.author.roles) and (role == weeklyrole2)) or ((weeklyrole2 in ctx.author.roles) and (role == weeklyrole1)):
            await ctx.author.remove_roles(role)
            await ctx.author.add_roles(prisoner)
            await ctx.response.send_message('Enjoy your time as <@&892744080906416148>', ephemeral = True)
# Didn't remove this code for reference :P
# @commands.has_permissions(ban_members=true)
# @cog_ext.cog_slash(name='rolereplace',description='Command for replacing weeekly roles!',options=[create_option(name='rolename1',description='Use this to enter new role names your role.',option_type=3,required=False)
#                 create_option(name='rolename2',description='Use this to enter new role names your role.',option_type=3,required=False)], guild_ids=guild_ids )

def setup(bot):
    bot.add_cog(SlashCog(bot))
