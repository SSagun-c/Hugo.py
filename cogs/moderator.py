import discord
import datetime
from discord.ext import commands

class moderatorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount + 1)

    @commands.Cog()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.display_name} got kicked at {datetime.datetime.utcnow()} because of: {reason}')




def setup(bot):
    bot.add_cog(moderatorCog(bot))