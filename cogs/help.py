import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(title="Currently being edited", description="For help join the help Server [here](https://discord.gg/6JkmzhDsps)", color=0x8962AA)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpCog(bot))