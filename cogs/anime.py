import asyncio
from aiohttp.tracing import TraceRequestRedirectParams
import discord
import aiohttp
import datetime
from discord.ext import commands
from discord.ext.commands import cooldown



class animeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['aq', 'quote'])
    @cooldown(1, 5, commands.BucketType.user)

    async def animequote(self, ctx):

        async with aiohttp.ClientSession() as Session:


            request = await Session.get('https://animechan.vercel.app/api/random')

            aqjson = await request.json()


        embed = discord.Embed(title=f"Anime: {aqjson['anime']}", description=f"Character: {aqjson['character']}", color=0xE0A899)

        embed.add_field(name="Quote", value=aqjson['quote'])


        await ctx.send(embed=embed)

        

    @commands.command(aliases=['aav', 'avatars'])
    @cooldown(1, 10, commands.BucketType.user)
    async def animeavatar(self, ctx):

        async with aiohttp.ClientSession() as Session:

            request = await Session.get('https://shiro.gg/api/images/avatars')

            ajson = await request.json()


        embed = discord.Embed(title=f"Here's your Avatar {ctx.message.author.display_name}", color=0xAE0786)

        embed.set_image(url=ajson['url'])
        await ctx.send(embed=embed)


    @commands.command()
    @cooldown(1, 10, commands.BucketType.user)
    async def anime(self, ctx, *, Anime_Name):

        async with aiohttp.ClientSession() as session:

            async with session.get(f"https://kitsu.io/api/edge/anime?filter[text]={Anime_Name}") as r:

                json_data = await r.json()


        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en_jp'], url=json_data['data'][0]['links']['self'], description=f"{json_data['data'][0]['attributes']['synopsis']}\n\n", color=0xEE00EE)


        embed.set_thumbnail(url=json_data['data'][0]['attributes']['posterImage']['original'])

        embed.add_field(name="📆 Aired", value=f"From **{json_data['data'][0]['attributes']['startDate']}** to **{json_data['data'][0]['attributes']['endDate']}**", inline=False)
    
        embed.add_field(name="⌛ Status", value=f"{json_data['data'][0]['attributes']['status']}\n\n", inline=True)

        embed.add_field(name="💿 Total Episodes", value=f"{json_data['data'][0]['attributes']['episodeCount']} Episodes", inline=False)

        embed.add_field(name="⌚ Average Episode Length", value=f"{json_data['data'][0]['attributes']['episodeLength']} Minutes", inline=True)

        embed.add_field(name="🕒 Total Length (Minutes)", value=f"{json_data['data'][0]['attributes']['totalLength']} Minutes\n\n", inline=True)

        embed.add_field(name="🏆 Average Rating", value=f"{json_data['data'][0]['attributes']['averageRating']}/100", inline=False)

        embed.add_field(name="✨ Popularity Rank", value=f"#{json_data['data'][0]['attributes']['popularityRank']}", inline=False)

        embed.add_field(name="💯 Rating Rank", value=f"#{json_data['data'][0]['attributes']['ratingRank']}", inline=True)


        embed.set_footer(text=f"Powered by Kitsu ©")


        embed.timestamp = datetime.datetime.utcnow()


        await ctx.send(embed=embed)




    @commands.command()
    @cooldown(1, 10, commands.BucketType.user)
    async def manga(self, ctx, *, Manga_Name):

        async with aiohttp.ClientSession() as session:

            async with session.get(f"https://kitsu.io/api/edge/manga?filter[text]={Manga_Name}") as r:

                json_data = await r.json()

        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en_jp'], url=json_data['data'][0]['links']['self'], description=f"{json_data['data'][0]['attributes']['synopsis']}\n\n", color=0xFF00EE)

        embed.set_thumbnail(url=json_data['data'][0]['attributes']['posterImage']['original'])

        embed.add_field(name="📆 Published", value=f"From **{json_data['data'][0]['attributes']['startDate']}** to **{json_data['data'][0]['attributes']['endDate']}**", inline=False)

        embed.add_field(name="📜 SubType", value=json_data['data'][0]['attributes']['subtype'], inline=False)

        embed.add_field(name="⌛ Status", value=f"{json_data['data'][0]['attributes']['status']}", inline=False)

        embed.add_field(name="📖 Chapters", value=f"{json_data['data'][0]['attributes']['chapterCount']} Chapter(s)", inline=True)

        embed.add_field(name="📰 Total Volumes", value=f"{json_data['data'][0]['attributes']['volumeCount']} Volume(s)", inline=True)

        embed.add_field(name="🏆 Average Rating", value=f"{json_data['data'][0]['attributes']['averageRating']}/100", inline=False)

        embed.add_field(name="✨ Popularity Rank", value=f"#{json_data['data'][0]['attributes']['popularityRank']}", inline=False)

        embed.add_field(name="💯 Rating Rank", value=f"#{json_data['data'][0]['attributes']['ratingRank']}", inline=True)


        embed.set_footer(text=f"Powered by Kitsu ©")


        embed.timestamp = datetime.datetime.utcnow()


        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(animeCog(bot))