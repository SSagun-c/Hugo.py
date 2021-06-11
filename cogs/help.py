import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(title="Hugo.py Command List", description="For help join the help Server [here](https://discord.gg/6JkmzhDsps)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpCog(bot))