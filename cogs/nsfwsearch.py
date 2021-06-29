import discord
import mediascraper
from discord.ext import commands

hh = mediascraper.HentaiHaven()
r34 = mediascraper.Rule34()

class nsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['hentaihaven', 'hh'])
    @commands.is_nsfw()
    async def hentai_haven(self, ctx, *args):
        video = await hh.category_search(str(" ").join(args))
        await ctx.send(video)


def setup(bot):
    bot.add_cog(nsfwCog(bot))