import aiohttp
import discord
import datetime
import random
import hmtai
from discord.ext import commands
from discord.ext.commands import cooldown


class imageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['y'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def yuri(self, ctx):
      y = hmtai.useHM("v2","yuri")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Yuri", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command(aliases=['bj'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def blowjob(self, ctx):
      y = hmtai.useHM("v2","blowjob")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Blowjob", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text="wish that was you huh?")

      await ctx.send(embed=embed)
      
      
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def ass(self, ctx):
      y = hmtai.useHM("v2","ass")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Ass", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def bdsm(self, ctx):
      y = hmtai.useHM("v2","bdsm")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 BDSM", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
   
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def cum(self, ctx):
      y = hmtai.useHM("v2","cum")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Cum", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command(aliases=['mb'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def masturbation(self, ctx):
      y = hmtai.useHM("v2","masturbation")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Masturbation", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command(aliases=['e', 'erotic'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def ero(self, ctx):
      y = hmtai.useHM("v2","ero")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Erotic", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed) 
      
    @commands.command(aliases=['ag'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def ahegao(self, ctx):
      y = hmtai.useHM("v2","ahegao")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Ahegao", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command(aliases=['uni'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def uniform(self, ctx):
      y = hmtai.useHM("v2","uniform")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Uniforms", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def glasses(self, ctx):
      y = hmtai.useHM("v2","glasses")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Girl with Glasses", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def gif(self, ctx):
      y = hmtai.useHM("v2","gif")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Random nsfw Gif", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)
      
    @commands.command(aliases=['t'])
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def tentacles(self, ctx):
      y = hmtai.useHM("v2","tentacles")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Tentacles", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"I won't even question it")

      await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def trap(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://waifu.pics/api/nsfw/trap')
            yurijson = await request.json()

        embed = discord.Embed(color=0XEE6363)
        embed.set_author(name="🔞 Trap", url=yurijson['url'])
        embed.set_image(url=yurijson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @cooldown(1, 5, commands.BucketType.user)
    async def thighs(self, ctx):
      y = hmtai.useHM("v2","thighs")
      
      embed = discord.Embed(color=0XEE6363)
      embed.set_author(name="🔞 Thighdeology", url=y)
      embed.set_image(url=y)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author}")

      await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def boobs(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://anime-api.hisoka17.repl.co/img/nsfw/boobs')
            boobsjson = await request.json()

        embed = discord.Embed(color=0xB6245B)
        embed.set_author(name="🔞 Boobs", url=boobsjson["url"])
        embed.set_image(url=boobsjson["url"])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)

    # sfw image commands

    @commands.command()
    @cooldown(1, 5, commands.BucketType.user)
    async def pussy(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            pussyjson = await request.json()

            title = ['A Dog Is A Dog , But A Cat Is A Purrrrson',
                    'A Tail Of Two Cats',
                    'As Every Cat Owner Knows, Nobody Owns A Cat, Cats just Tolerate Us Living In Their House.',
                    'Assistant To My Cat',
                    'Attack Cat',
                    'Cat And Mouse',
                    'Cat-astrophe', 
                    'Catnapping',
                    'Cats Are Always On The Wrong Side Of Every Door',
                    'Cats Are Children With Fur',
                    "Cats Are Like Potato Chips...You Can't Have Just One",
                    'Cats Leave Paw Prints On Your Heart',
                    'Cats Rule And Dogs Drool',
                    'Cats Understand The Importance Of A Nap',
                    'Cool Kitty',
                    'Crazy Cats',
                    'Dogs Have Masters... Cats Have Staff',
                    "Dogs Think They're Human And Cats Think They're God",
                    'Family Felines',
                    'Feeding Times',
                    'Footprints On Our Hearts',
                    'Friends Fur-Ever',
                    'Fur Ever Friends',
                    'Furry Friends',
                    'Here Kitty, Kitty',
                    'Home Is Where The Cat Is',
                    'If You Want The Best Seat In The House... Move The Cat',
                    "I'm Not Rude, I've Got Cat-i-tude",
                    "In This House The Cat's In Charge",
                    'Jungle Cats',
                    'Let Me Get This Straight, My Grandchild Is A Cat',
                    'Love Me, Love My Cat',
                    'Meow',
                    'My Boyfriend Said It Was The Cat Or Him, Gee, I Miss Him Sometimes',
                    'My Cat Kneads Me',
                    'Pick Of The Litter',
                    'Purranoia: The Fear That The Cats Are Up To Something',
                    'Puurrrfect',
                    'Pussy-Cat, Pussy-Cat, Where Have You Been?',
                    'Raining Cats And Dogs',
                    "Sittin' Pretty With My Kitty",
                    'The Cat In The Hat',
                    "The Cat's Meow",
                    'The Cheshire Cat',
                    'The "Purr"fect Way To Spend The Day',
                    'Visit To The Vet',
                    'What A Handsome Hunk Of Cat',
                    "When The Cat's Away, The Mice Will Play",
                    'When You Have A Cat, Everyday Is Purr-fect']

        embed = discord.Embed()
        embed.set_author(name=random.choice(title), url=pussyjson['link'])
        embed.set_image(url=pussyjson['link'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")
        
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(imageCog(bot))