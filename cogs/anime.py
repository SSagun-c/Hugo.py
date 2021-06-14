import discord
import aiohttp
import datetime
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


        embed = discord.Embed(title=f"Anime: {aqjson['anime']}", description=f"Character: {aqjson['character']}", color=0xE0A899)

        embed.add_field(name="Quote", value=aqjson['quote'])


        await ctx.send(embed=embed)

        







def setup(bot):
    bot.add_cog(animeCog(bot))