import discord
import mediascraper
from discord.ext import commands

hh = mediascraper.HentaiHaven()
r34 = mediascraper.Rule34()
gb = mediascraper.Gelbooru()

class nsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['hentaihaven', 'hh'])
    @commands.is_nsfw()
    async def hentai_haven(self, ctx, *args):
        video = await hh.category_search(str(" ").join(args))
        await ctx.send(video)

    
    @commands.command(aliases=['r34'])
    @commands.is_nsfw()
    async def rule34(self, ctx, *args):
        image = await r34.image_search(str(" ").join(args))
        await ctx.send(image)


    @commands.command(aliases=['gbooru', 'gb'])
    @commands.is_nsfw()
    async def gelbooru(self, ctx, *args):
        image = await gb.image_search(str(" ").join(args))
        await ctx.send(image)


def setup(bot):
    bot.add_cog(nsfwCog(bot))