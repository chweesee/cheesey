import discord
import re
from discord.enums import ActivityType, Status
from discord.ext import commands
from pip._vendor.progress import counter

class Mods(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod cog is now live!')

    @commands.group(invoke_without_command=True)
#    @commands.has_guild_permissions(manage_roles=True)
 #   async def roleclear(self, ctx):
  #      author=612900700992831490
   #     weeklyrole1 = get(ctx.guild.roles, id=884332552838611005)
    #    await author.remove_roles(weeklyrole1)
     #   weeklyrole2 = get(ctx.guild.roles, id=884332449637740574)
      #  await author.remove_roles(weeklyrole2)

    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount:int=10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(f"Deleted {len(deleted)-1} message(s)")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def links(self, ctx, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False
            chunks = " ".join(m.content.lower().split("\n"))
            chunks = chunks.split(" ")
            for chunk in chunks:
                if (True if re.search(r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))", chunk) else False): # stupid url regular expression ._.
                    counter += 1
                    return True
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which had links")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which started with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which ended with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which contained the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which were sent by the mentioned user")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >100:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 100.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which contained invites")

def setup(bot):
    bot.add_cog(Mods(bot))
