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
    async def anime(self, ctx, *, name):

        async with aiohttp.ClientSession() as session:

            async with session.get(f"https://kitsu.io/api/edge/anime?filter[text]={name}") as r:

                json_data = await r.json()


        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en'], description=json_data['data'][0]['attributes']['synopsis'])


        await ctx.send(embed=embed)


        print(json_data['results'][0]['description'])








    async def cog_command_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            
            embed = discord.Embed(title=f"{ctx.message.author.display_name} Please provide the name of the Anime you want. e.g. h!anime Date A Live", color=0xFF0000)

            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(animeCog(bot))