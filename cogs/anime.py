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
    async def anime(self, ctx, *, name="Naruto"):

        async with aiohttp.ClientSession() as session:

            request = await session.get(f" https://api.jikan.moe/v3/search/anime?q={name}")
            
            anijson = await request.json()

        embed = discord.Embed(title=anijson['results'][0]['title'])

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(animeCog(bot))