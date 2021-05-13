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
from discord import colour
from discord.abc import GuildChannel
from discord.colour import Color
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from discord import Member
from discord.ext.commands import Bot, BucketType, cooldown
from discord.ext.commands import has_permissions, MissingPermissions, CommandOnCooldown, NSFWChannelRequired
from discord.ext.commands.errors import CommandError
from discord.utils import get

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='.')


client.remove_command('help')
# Event

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

@tasks.loop(seconds=120)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers! .help"))

@client.event
@commands.has_permissions(administrator=False)
async def on_message(message):
    if ['youtube.com',
        'twitch.tv',
        'instagram',
        'facebook',] is message.content.lower():
        await message.delete()
        await message.send("Please do not advertise here")
    await client.process_commands(message)



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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
@commands.is_nsfw()
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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('http://meme-api.herokuapp.com/gimme')
        memejson = await request.json()
    embed = discord.Embed(title=memejson['title'], color=0xFF8800)
    embed.set_author(name=memejson['author'], icon_url='https://i.postimg.cc/pTzSdRqC/reddit-logo.png')
    embed.set_image(url=memejson['url'])
    await ctx.send(embed=embed)

@meme.error
async def meme_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
@commands.is_nsfw()
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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

@client.command()
@commands.is_nsfw()
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
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

@client.command()
async def roll(ctx):
    await ctx.send(f"You rolled {random.randint(1, 100)}!")

@client.command()
@cooldown(1, 5)
async def blush(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.waifu.pics/sfw/blush')
        blushjson = await request.json()
    await ctx.send(f'{ctx.message.author} blushes')
    embed = discord.Embed()
    embed.set_image(url=blushjson['url'])
    await ctx.send(embed=embed)

@client.command()
@commands.is_nsfw()
@cooldown(1, 8)
async def yuri(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/yuri')
        yurijson = await request.json()
    embed = discord.Embed()
    embed.set_image(url=yurijson['url'])
    await ctx.send(embed=embed)

@yuri.error
async def yuri_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

@client.command()
async def suggest(ctx):
    await ctx.send('Have any suggestion for the bot? Join the Help Server! https://discord.gg/6JkmzhDsps')

# help

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", color=0xFFFF00)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.set_thumbnail(url='https://i.postimg.cc/xdyWm6Fj/images.jpg')
    embed.add_field(name="**General Commands**", value="■ `.ping`\n■ `.8ball`\n■ `.pussy`\n■ `.serverinfo`\n■ `.roll`\n■ `.suggest`", inline=False)
    embed.add_field(name="**Meme Command**", value="■ `.meme`", inline=False)
    embed.add_field(name="**Anime Related Commands**", value="■ `.anime`\n■ `.foxgirl`\n■ `.neko`\n■ `.blush`", inline=True)
    embed.add_field(name="**NSFW Commands**", value="■ `.hentai`\n■ `.trap`\n■ `nsfwneko`", inline=True)
    embed.add_field(name="**Commands for Moderators**", value="■ `.clear`\n■ `.kick`\n■ `.ban`\n■ `.unban`")
    embed.set_footer(text='Need more information? Try .dhelp for detailed Information and .nsfwhelp for detailed Information about the NSFW commands!' )
    await ctx.send(embed=embed)

@client.command()
async def dhelp(ctx):
    embed = discord.Embed(title="Detailed Information", color=0xFFFF00)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.add_field(name="General Command Infomration", value="**What does `.ping` do?**\nThe `.ping` command shows you the response time for the Bot, that means how long the Bot takes to answer to your command\n**What does `.8ball` do?**\nType `.8ball` and a random question, the Bot now will give you a random logical answer to your question.\n**What does `.pussy` do and is it NSFW?**\nThe `.pussy` command is not NSFW related. It shows you a random cute cat with a funny Title.\n**What does `.serverinfo` do?**\nThis command is self explanatory, it shows you Information about your Server in a cool Embed.\n**What does `.roll` do?**\nThe `.roll` command gives you a random number between 1 and 100.\n**What is `.suggest`?**\n The `.suggest` command invites you to the official Hugo,py Help Server, where you can suggest things, report Bugs or get help by Moderators!", inline=False)
    embed.add_field(name="Meme Command Information", value="**What does the `.meme` command do?**\nThe `.meme` command fetches a random Image from the official Meme Subreddit with the official Title and official author.", inline=False)
    embed.add_field(name="Anime Related Command Information", value="**What does `.anime` do?**\nThe `.anime` command fetches you a random Image from a Library with 52.199 Anime pictures.\n**What does the `.foxgirl` command do?**\nThe `.foxgirl` command fetches a random Image related to Foxgirl's (similar to neko's).\n**What does `.neko` do?**\nThe command `.neko` fetches you a random neko Image from a Library that contains 33.046 Neko Images.\n**What does `.blush` do?**\nThe command `.blush` is something more likely used for Roleplay, it gives you a random Anime character that blushes and says: `[Username] blushes`", inline=False)
    embed.add_field(name="Moderator Command Information", value="**All the now listed commands are only for Administrators!**\n**What is `.clear` for?**\n`.clear` deletes your selected amount of messages to deleted in one channel.\n**What does `.ban` do?**\nI think this command is self explanatory but `.ban` bans the user you mentioned from the Server.\n**What does `.unban` do?**\nThis command requires you to write the users name you banned once with his Discriminator. As an Example: `.unban SSagun.py#6969`", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nsfwhelp(ctx):
    embed = discord.Embed(title="NSFW Command Information", color=0x9ACD32)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.set_thumbnail(url='https://i.postimg.cc/RhHXLLBF/unnamed.jpg')
    embed.add_field(name="NSFW Commands", value="**KEEP IN MIND**\nThe channel has to be NSFW for the commands to work!\n**What does `.hentai` do?**\n`.hentai` sends you a random Hentai Image from a Library that contains 33.677 Images\n**What does `.trap` do?**\nDo you like Traps? `.trap` sends you a random Trap related Image from a Library that contains 25.358 Trap Images\n**What does `.nsfwneko` do?**\nThe `.nsfwneko` command sends you a random lewded neko Image from a Library that contains 22.017 Lewded Neko Images.\n**What is `.yuri`?**\nThe command `.yuri` sends a random Image from a Library that contains 26.867 Images. Yuri means Lesbian.", inline=True)
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
        await ctx.send(f'Please specifiy an amount of messages to delete.', delete_after=5)


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
        await ctx.send("Please mention the Member you want to kick.")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason, delete_message_days=1)
    await ctx.send(f'Banned!')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry you are missing permission to do that! Message an Admin instead.')
    else:
        await ctx.send('Please mention the member you want to kick.')


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
        await ctx.send("Please send the users name with his Discriminator '#'\nExample: .unban SSagun#1050")


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