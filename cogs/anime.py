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


    @commands.command(aliases=['anisearch', 'kitsu', 'as'])
    @cooldown(1, 10, commands.BucketType.guild)

    async def anime(self, ctx, *, anime):

        async with aiohttp.ClientSession() as session:

            request = await session.get(f'https://kitsu.io/api/edge/anime?filter[text]={anime}')

            animejson = await request.json()


        embed = discord.Embed(title={animejson['titles': 'en']}, description=animejson['description'])

        embed.set_thumbnail(url=animejson['posterImage': 'original'])

        embed.add_field(name="Status", value=animejson['status'])
        embed.add_field(name="Genres", value=animejson['ageRatingGuide'])

        embed.add_field(name="💯Average Rating", value=f"{animejson['averageRating']}/100")
        embed.add_field(name="✨Popularity Rank", value=f"Rank #{animejson['popularityRank']}")
        embed.add_field(name="1️⃣ Rating Rank", value=f"Rank #{animejson['ratingRank']}")

        embed.add_field(name="Started at", value=animejson['startDate'])
        embed.add_field(name="Ended at", value=animejson['endDate'])

        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

        







def setup(bot):
    bot.add_cog(animeCog(bot))