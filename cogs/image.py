import aiohttp
import discord
import datetime
import random
from discord.ext import commands
from discord.ext.commands import cooldown


class imageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['y'])
    @commands.is_nsfw()
    @cooldown(1, 8, commands.BucketType.user)
    async def yuri(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.computerfreaker.cf/v1/yuri')
            yurijson = await request.json()

        embed = discord.Embed()
        embed.set_author(name="🔞 Yuri", url=yurijson['url'])
        embed.set_image(url=yurijson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command(aliases=['nn'])
    @commands.is_nsfw()
    @cooldown(1, 8, commands.BucketType.user)
    async def thighs(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://shiro.gg/api/images/nsfw/thighs')
            thighsjson = await request.json()

        embed = discord.Embed()
        embed.set_author(name="🔞 Thighs", url=thighsjson['url'])
        embed.set_image(url=thighsjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command()
    @cooldown(1, 8, commands.BucketType.user)
    @commands.is_nsfw()
    async def trap(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.computerfreaker.cf/v1/trap')
            trapjson = await request.json()

        embed = discord.Embed(color=0xC21456)
        embed.set_author(name="🔞 Trap", url=trapjson['url'])
        embed.set_image(url=trapjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)

    
    @commands.command(aliases=['h'])
    @cooldown(1, 8, commands.BucketType.user)
    @commands.is_nsfw()
    async def hentai(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://shiro.gg/api/images/nsfw/hentai')
            hentaijson = await request.json()

        embed = discord.Embed()
        embed.set_author(name="🔞 Hentai", url=hentaijson['url'])
        embed.set_image(url=hentaijson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command(aliases=['b'])
    @cooldown(1, 8, commands.BucketType.user)
    @commands.is_nsfw()
    async def bondage(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://shiro.gg/api/images/nsfw/bondage')
            bondjson = await request.json()

        embed = discord.Embed()
        embed.set_author(name="🔞 Bondage", url=bondjson['url'])
        embed.set_image(url=bondjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)
        
    # sfw image commands

    @commands.command()
    @cooldown(1, 8, commands.BucketType.user)
    async def neko(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://shiro.gg/api/images/neko')
            nekojson = await request.json()

        embed = discord.Embed()
        embed.set_author(name="Neko", url=nekojson['url'])
        embed.set_image(url=nekojson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command()
    @cooldown(1, 8, commands.BucketType.user)
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


    @commands.command(aliases=['a'])
    @cooldown(1, 8, commands.BucketType.user)
    async def anigirl(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.computerfreaker.cf/v1/anime')
            animejson = await request.json()

        embed = discord.Embed()
        embed.set_author(name='Anime Girl', url=animejson['url'])
        embed.set_image(url=animejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command()
    @cooldown(1, 8, commands.BucketType.user)
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




def setup(bot):
    bot.add_cog(imageCog(bot))