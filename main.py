import discord
import json
import random
import os
import aiohttp
import asyncio
import datetime as dt
import typing as t
import re
from PIL import Image
from io import BytesIO
from discord import Embed, Member
from discord.abc import GuildChannel
from discord.colour import Color
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from discord import Member
from discord.ext.commands import Bot, BucketType, cooldown
from discord.ext.commands import has_permissions, MissingPermissions, CommandOnCooldown
from discord.ext.commands.errors import CommandError
from discord.utils import get

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='.')


client.remove_command('help')
status = cycle(['hentaihaven.org',
         'hanime.tv', 
         'nhentai.xxx', 
         'hentai.xxx', 
         'simply-hentai.com', 
         'hd.freehentaistream.com', 
         'luscious.net', 
         'hentaidude.com', 
         'hentai-foundry.com', 
         'rule34.xxx',
         'e-hentai.org',
         'naughtymachinima.com',
         'lolhentai.net',
         'hentaipulse.com',
         'cartoonporn.xxx',
         'hentaiplay.net',
         'fakku.net',
         'hypnohub.net',
         'hentaifreak.org',
         'pururin.io',
         'hentai.cafe',
         'cartoonpornvideos.com',
         'mult34.com',
         'hentaigasm.com',
         'porcore.com',
         'tube.hentaistream.com',
         'ohentai.org',
         'hentaifox.com',
         'xanimeporn.com',
         'hentaihere.com',
         'zzcartoon.com',
         'hentaifromhell.org',
         'fapservice.com',
         'sankakucomplex.com',
         'studiofow.com',
         'muchohentai.com',
         'tsumino.com',
         'miohentai.com',
         'underhentai.net',
         'kisshentai.net',
         'whentai.com',
         'animeidhentai.com',
         'hentailove.tv',
         'giantessbooru.com',
         'xbooru.com',
         'hentaicloud.com',
         'rule34.paheal.net',
         'hentaimama.com',
         'danbooru.donmai.us',
         'asmhentai.com',
         'hentai.animestigma.com',
         'myhentai.tv',
         'exhentai.org',
         'e621.net'])
# Event

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
@commands.has_permissions(administrator=False)
async def on_message(message):
    if ['youtube.com',
        'twitch.tv',
        'instagram',
        'facebook',] is message.content.lower():
        await message.delete()
        await message.channel.send("Please do not advertise here, go to #self-promotion instead!")
    await client.process_commands(message)

@client.command()
async def prefix(ctx):
    
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    pre = prefixes[str(ctx.guild.id)]

    await ctx.send(f"My current prefix for this server is '{pre}'")


# Fun commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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

@client.command()
@cooldown(1, 8)
async def pussy(ctx):
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
    embed = discord.Embed(title=random.choice(title))
    embed.set_image(url=pussyjson['link'])
    await ctx.send(embed=embed)

@pussy.error
async def pussy_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def neko(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/neko')
        nekojson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=nekojson['url'])
    await ctx.send(embed=embed)

@neko.error
async def neko_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def hentai(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/hentai')
        hentaijson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=hentaijson['url'])
    await ctx.send(embed=embed)

@hentai.error
async def hentai_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def foxgirl(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://nekos.life/api/v2/img/fox_girl')
        foxgirljson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=foxgirljson['url'])
    await ctx.send(embed=embed)

@foxgirl.error
async def foxgirl_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('http://meme-api.herokuapp.com/gimme')
        memejson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=memejson['url'])
    await ctx.send(embed=embed)

@meme.error
async def meme_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def anime(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/anime')
        animejson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=animejson['url'])
    await ctx.send(embed=embed)

@anime.error
async def anime_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def trap(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/trap')
        trapjson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=trapjson['url'])
    await ctx.send(embed=embed)

@trap.error
async def trap_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

@client.command()
@cooldown(1, 8)
async def nsfwneko(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/nsfwneko')
        nsfwnekojson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=nsfwnekojson['url'])
    await ctx.send(embed=embed)

@nsfwneko.error
async def nsfwneko_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.")

# help

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", color=0xFFFF00)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/sagun.mp3/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.add_field(name="**General Commands**", value="ping   8ball   pussy   serverinfo", inline=True)
    embed.add_field(name="**Meme Command**", value="meme", inline=False)
    embed.add_field(name="**Anime Related Commands**", value="anime   foxgirl   neko", inline=True)
    embed.add_field(name="**NSFW Commands**", value="hentai   trap   nsfwneko", inline=False)
    embed.add_field(name="**Commands for Moderators**", value="prefix   changeprefix   clear   kick   ban   unban")
    await ctx.send(embed=embed)


# Moderator commands

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry you are missing permission to do that! Message an Admin instead."
        await ctx.send(text)
    else:
        await ctx.send(f'Please specifiy an amount of messages to delete.')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await Member.kick(reason=reason)
    await ctx.send(f'Kicked!')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry you are missing permission to do that! Message an Admin instead."
        await ctx.send(text)
    else:
        await ctx.send("Please mention the Member you want to kick and **DON'T** kick the person without any reasons! The Owner can see the audit log!")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    emoji = get(ctx.message.server.emojis, name='WumpusBan')
    await member.ban(reason=reason, delete_message_days=1)
    await ctx.send(f'Banned! {emoji}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry you are missing permission to do that! Message an Admin instead.')
    else:
        await ctx.send("Please mention the Member you want to kick and **DON'T** kick the person without any reasons! The Owner can see the audit log!")


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member : int):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "You cant just unban someone! Tell the person to send an unban application instead."
        await ctx.send(text)
    else:
        await ctx.send("Please send the users name with his prefix '#'\nExample: .unban SSagun#1050")


# For Members

@client.command()
async def serverinfo(ctx):
    name = ctx.guild.name
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)  
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name + " Server Information", description=description, color=0xFFFF00)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Total Members", value=memberCount, inline=True)

    await ctx.send(embed=embed)


client.run(os.environ['DISCORD_TOKEN'])