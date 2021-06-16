import discord
import aiohttp
import datetime
from discord.ext import commands
from discord.ext.commands import cooldown



class animeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['aq'])
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
    async def anime(self, ctx, *, AnimeName):

        async with aiohttp.ClientSession() as session:

            async with session.get(f"https://kitsu.io/api/edge/anime?filter[text]={AnimeName}") as r:

                json_data = await r.json()


        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en'], description=json_data['data'][0]['attributes']['synopsis'], color=0xEE00EE)


        embed.set_thumbnail(url=json_data['data'][0]['attributes']['posterImage']['original'])


        fields = ["Created", json_data['data'][0]['attributes']['startDate'], True,

                "Finished", json_data['data'][0]['attributes']['endDate'], True,

                "Status", json_data['data'][0]['attributes']['status'], True,

                "Episodes", f"{json_data['data'][0]['attributes']['episodeCount']} Episodes", True,

                "Average Episode Length", f"{json_data['data'][0]['attributes']['episodeLength']} Minutes", True,

                "Total Length (Minutes)", f"{json_data['data'][0]['attributes']['totalLength']} Minutes", True,

                "Average Rating", f"{json_data['data'][0]['attributes']['averageRating']}/100", True,
                
                "Popularity Rank", f"#{json_data['data'][0]['attributes']['popularityRank']}", True,

                "Rating Rank", f"#{json_data['data'][0]['attributes']['ratingRank']}", True]

        for name, value, inline in fields:

            embed.add_field(name=name, value=value, inline=inline)

        
        embed.set_footer(text=f"Powered by ©Kistu")


        embed.timestamp = datetime.datetime.utcnow()


        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(animeCog(bot))