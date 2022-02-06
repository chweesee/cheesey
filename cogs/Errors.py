import disnake
from disnake.ext import commands

import aiohttp, pickle, traceback, os

LOGGING_WEBHOOK = os.getenv('WARNLOG')

async def webhook_send(url, message, username = 'Errors', avatar = 'https://i.imgur.com/2qbA4Vd.png'):

    async with aiohttp.ClientSession() as session:
        webhook = disnake.Webhook.from_url(url, adapter = disnake.AsyncWebhookAdapter(session))
        if isinstance(message, disnake.Embed):
            await webhook.send(embed = message, username = username, avatar_url = avatar)
        else:
            await webhook.send(message, username = username, avatar_url = avatar)

async def export_exception(ctx, error):

        embed = disnake.Embed()
        embed.title = 'Server Level exception'
        embed.colour = disnake.Color.red()
        tb_str = ''.join(traceback.format_tb(error.__traceback__))
        err_string = ''.join(tb_str)
        embed.description = f'''
            Detailed Traceback
            ```
            {err_string}
            {error. __class__. __name__}: {str(error)}
            ```

            on command `{ctx.message.content}`
            by user `{ctx.author.name}#{ctx.author.discriminator}`
            on guild `{ctx.guild.id}` with name `{ctx.guild.name}`
            on channel `{ctx.channel.id}` with name `{ctx.channel.name}`
        '''
        await webhook_send(LOGGING_WEBHOOK, embed)
        embed = disnake.Embed()
        embed.title = 'An error occured'
        embed.description = 'The error has been reported to the devs'
        await ctx.send(embed = embed, delete_after = 20)

class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Logger was loaded')

    @commands.Cog.listener()
    async def on_ready(self):

        print('Ready')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return
        embed = disnake.Embed(color = ctx.message.author.color,timestamp = ctx.message.created_at)
        embed.set_footer(text = self.bot.user.name, icon_url = self.bot.user.avatar)
        embed.set_author(name = ctx.message.author.name,icon_url = ctx.message.author.avatar)
        error = getattr(error, 'original', error)


        if isinstance(error, disnake.errors.Forbidden):
            embed.title = 'Bot has Insufficient Perms to perform this action \N{CROSS MARK}'
            if error.text != None:
                embed.add_field(name = f'Error reason:', value = error.text)
            if error.code != None:
                embed.add_field(name = f'Error code:', value = f'**{error.code} Forbidden**')
            if error.status != None:
                embed.add_field(name = f'Error status:', value = f'**{error.status}**')
            return await ctx.send(embed = embed, delete_after = 20)


        if isinstance(error, commands.errors.MissingPermissions):
            embed.title = 'Missing Permissions \N{CROSS MARK}'
            permlist = ''
            for perms in error.missing_perms:
                missperm = str(perms).replace('_',' ').capitalize()
                permlist = permlist + missperm + '\n'
            embed.description = f'**{permlist}**'
            return await ctx.send(embed = embed, delete_after = 20)


        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed.title = 'You didn\'t pass in the required arguements'
            params = ctx.prefix + ctx.command.name + ' ' + ctx.command.signature 
            #await remote(ctx.command.callback)
            embed.description = str(params)
            embed.set_footer(text = '<> Denotes required argument. [] Denotes optional argument')
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.CommandNotFound):
            embed.title = f'Specified command doesn\'t exist'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.MemberNotFound):
            embed.title = f'Could not find the specified member'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.BadArgument):
            embed.title = f'Invalid argument(s) \N{CROSS MARK}'
            invalidargs = ''
            for invalid in error.args:
                invalidargs = invalidargs + invalid + '\n'
            embed.description = f'**{invalidargs}**'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.NoPrivateMessage):
            embed.title = f'Error \N{CROSS MARK}'
            embed.description = f'`{ctx.prefix}{ctx.command.name}` Does not work in private messages'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.CheckFailure):
            embed.title = f'One of the checks failed to validate'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.DisabledCommand):
            embed.title = f'This command has been disabled'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.TooManyArguments):
            embed.title = f'More than required arguments were passed to this command'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.CommandOnCooldown):
            embed.title = f'You are currently on a cooldown'
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                 embed.description = f'**You must wait `{int(s)}` seconds to use this command!**'
            elif int(h) == 0 and int(m) != 0:
                 embed.description = f'**You must wait `{int(m)}` minutes and `{int(s)}` seconds to use this command!**'
            else:
                 embed.description = f'**You must wait `{int(h)}` hours, `{int(m)}` minutes and `{int(s)}` seconds to use this command!**'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.NotOwner):
            embed.title = f'Only the owner can use this command'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.MessageNotFound):
            embed.title = f'Couldn\'t find the requested message'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.UserNotFound):
            embed.title = f'Couldn\'t find the requested user'
            embed.description = error.argument
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.MissingAnyRole):
            embed.title = f'You do not have the requested roles for this command'
            embed.description = error.argument
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.MissingRole):
            embed.title = f'You do not have the requested role for this command'
            embed.description = error.argument
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.BotMissingPermissions):
            embed.title = f'I do not have the permissions to execute the action'
            embed.description = error.argument
            permlist = ''
            for perms in error.missing_perms:
                missperm = str(perms).replace('_',' ').capitalize()
                permlist = permlist+missperm+'\n'
            embed.add_field(name = 'Missing perms:', value = f'**{permlist}**')
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.NSFWChannelRequired):
            embed.title = f'Command can only be executed in NSFW channels'
            embed.description = error.argument
            return await ctx.send(embed = embed, delete_after = 20)   

        if isinstance(error, commands.errors.ExtensionAlreadyLoaded):
            embed.title = f'Cog is already loaded'
            return await ctx.send(embed = embed, delete_after = 20)
        
        if isinstance(error, commands.errors.ExtensionNotLoaded):
            embed.title = f'Cog could not be loaded'
            return await ctx.send(embed = embed, delete_after = 20)

        if isinstance(error, commands.errors.ExtensionNotFound):
            embed.title = f'Cog does not exist'
            return await ctx.send(embed = embed, delete_after = 20)                            

        await export_exception(ctx, error)
        #raise error
def setup(client):
    client.add_cog(ErrorHandler(client))

