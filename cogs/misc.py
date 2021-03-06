import aiohttp
import discord
import random
import datetime
import asyncio
from typing import Optional
from discord import Member
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from discord.ext.commands import cooldown


class miscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'{random.choice(responses)}')


    @commands.command()
    @cooldown(1, 5, commands.BucketType.user)
    async def roll(self, ctx, amount: int=100):
        number = random.randint(1, amount)
        if number == 69:
            await ctx.send(f"{ctx.message.author.display_name} rolled 69 nice.")
        else:
            await ctx.send(f"{ctx.message.author.display_name} rolled {number}")


    @commands.command(aliases=['aw'])
    async def animeweb(self, ctx):
        websites = ['https://animeheaven.site',
                    'https://www1.gogoanime.ai',
                    'https://9anime.to/?13',
                    'https://www.crunchyroll.com/de',
                    'https://kissanime.com.ru',
                    'https://www.animefreak.tv/search',
                    'Thats a looong link: https://animedao.to/?__cf_chl_jschl_tk__=269246f7f0d00364560b64dbad4fd7c9ebf44ddf-1621269746-0-AejSw5U5CDHPBuyxKxjNli4wtTI2JZSjfvENeIiXd9_Fb-UJ-P6imCfXdVK_-pdDJUs3Ar5kA6IeeAb8gZmc4ajDplgiUHTjkaBKtd19eggYt2iGTXj1xJ7eoGJV-fp7ZZB6lluTRaS9clFnvyTJJkY13_FWLVWDXdvZqQ5a_z0MKYetMLHWuQMT7fqzVV6tJGBf09LMAB6zee7qlUBZfPBXhGZxI02rF4Taz5eKcW0_JNvyka-dG5h5T5o_flee1_Mb30j14iYIoGyCsEZaV0yKArhSxLwoDlM1UsnHNLGzWpm0uyl8ufagFAxJ_mZ8-KE4maNukhkU8yUDTrrBLwJOwLzr7IkkLjWejegd7GghVDhywFTNgAA-TysJX9SN3vQFkogRiqUM2BchyCRUHW4',
                    'https://chia-anime.su',
                    'https://www.funimation.com',
                    'https://www.animelab.com',
                    'https://www.viz.com',
                    'https://www.anime-planet.com',
                    'https://www.vrv.co/',
                    'Not avaiable in EU = https://gdpr.tubi.tv',
                    'https://gdpr.tubi.tv',
                    'https://myanimelist.net',
                    'https://www.asiancrush.com',
                    'https://www.hidive.com',]
        await ctx.send(random.choice(websites))

    
    @commands.command(aliases=["say"], pass_context=True)
    @cooldown(1, 5, commands.BucketType.user)
    async def repeat(self, ctx, *, repeat):
        weknow = ['i am dumb',
                    'im dumb',
                    'im stupid',
                    'i am stupid',
                    'i am retarded',
                    'im retarded',
                    'im a reatard',
                    'i am a retard',
                    'im weird',
                    'i am weird',
                    'im weird',
                    'i am a bitch',
                    'im a bitch',
                    'im a dumbass',
                    'i am a dumbass',]
        if repeat in weknow:
            await ctx.send("We know")
        else:
            await ctx.message.delete()
            await ctx.send(repeat)


    @commands.command(aliases=['av'])
    @cooldown(1, 9, commands.BucketType.user)
    async def avatar(self, ctx, target: Optional[Member]):
        target = target or ctx.message.author
        av = target.avatar_url
        embed = discord.Embed(title=target.display_name, color=0x90EE90)
        embed.set_image(url=av)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")
        await ctx.send(embed=embed)


    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        emoji = '\U0001f44d'
        await ctx.message.add_reaction(emoji)
        directmsg = await ctx.message.author.create_dm()
        await directmsg.send('Thanks for the thoughts of inviting me!\nhttps://top.gg/bot/832922273597227019')




    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 10, commands.BucketType.guild)
    async def sauce(self, ctx):
        sauce = random.randint(1, 350000)
        await ctx.send(f"https://nhentai.to/g/{sauce}")


    @commands.command(aliases=['emb'])
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, *, embedvalue):

      embed = discord.Embed(title=embedvalue, color=0xEE6363)
        
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
    

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title="Thank You!", description=f"Hi there {ctx.message.author.display_name}!\nThank you for the thoughts of voting for me!\nSimply [Click Me!](https://top.gg/bot/832922273597227019/vote)\nHave a Nice Day!", color=0x7289DA)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(miscCog(bot))