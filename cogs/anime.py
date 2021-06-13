from aiohttp.typedefs import DEFAULT_JSON_DECODER
import discord
import aiohttp
from discord.ext import commands
from discord.ext.commands import cooldown



class animeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['aq'])
    @cooldown(1, 5, commands.BucketType.guild)

    async def animequote(self, ctx):

        async with aiohttp.ClientSession() as Session:


            request = await Session.get('https://animechan.vercel.app/api/random')

            aqjson = await request.json()


        embed = discord.Embed(title=aqjson['anime'], description=f"Character: {aqjson['character']}")

        embed.add_field(name=None, value=aqjson['quote'])


        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(animeCog(bot))