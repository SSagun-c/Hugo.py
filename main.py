from asyncio.tasks import sleep
from datetime import date
import discord
import json
import random
import os
import aiohttp
import asyncio
import datetime
import typing as t
from discord import message
from discord.ext.commands.core import Command, command
import praw
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
from discord.ext.commands import has_permissions, MissingPermissions, NSFWChannelRequired, CommandOnCooldown
from discord.ext.commands.errors import CommandError
from discord.utils import get
from praw.models.listing.mixins import subreddit
from praw.reddit import Subreddit

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='h!')

client.remove_command('help')
# Event

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

@tasks.loop(seconds=120)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers! h!help"))


# Fun commands

@client.command()
async def ping(ctx):
    await ctx.send(f'```{client.latency * 1000}ms```')

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
    embed = discord.Embed()
    embed.set_author(name=random.choice(title), url=pussyjson['link'])
    embed.set_image(url=pussyjson['link'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@pussy.error
async def pussy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
async def neko(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/neko')
        nekojson = await request.json()
    embed = discord.Embed()
    embed.set_author(name="Neko", url=nekojson['url'])
    embed.set_image(url=nekojson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@neko.error
async def neko_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
@commands.is_nsfw()
async def hentai(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/hentai')
        hentaijson = await request.json()
    embed = discord.Embed()
    embed.set_author(name="Hentai", url=hentaijson['url'])
    embed.set_image(url=hentaijson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@hentai.error
async def hentai_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)


@client.command()
@cooldown(1, 8)
async def anime(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/anime')
        animejson = await request.json()
    embed = discord.Embed()
    embed.set_author(name='Anime Girl', url=animejson['url'])
    embed.set_image(url=animejson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@anime.error
async def anime_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)

@client.command()
@cooldown(1, 8)
@commands.is_nsfw()
async def trap(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/trap')
        trapjson = await request.json()
    embed = discord.Embed()
    embed.set_author(name="Thats a trap", url=trapjson['url'])
    embed.set_image(url=trapjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@trap.error
async def trap_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
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
    embed.set_author(name="Lewded Neko", url=nsfwnekojson['url'])
    embed.set_image(url=nsfwnekojson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@nsfwneko.error
async def nsfwneko_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is ratelimited, please try again in a few seconds", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

@client.command()
@cooldown(1, 5)
async def roll(ctx):
    number = random.randint(1, 100)
    if number == 69:
        await ctx.send("You rolled 69 nice.")
    else:
        await ctx.send(f"You rolled {number}")

@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Woah woah calm down sonic, I'm ratelimited", delete_after=5)
        

@client.command()
@cooldown(1, 5)
async def blush(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.waifu.pics/sfw/blush')
        blushjson = await request.json()
    embed = discord.Embed(title=f'{ctx.message.author.display_name} blushes')
    embed.set_image(url=blushjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.command()
@commands.is_nsfw()
@cooldown(1, 8)
async def yuri(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://api.computerfreaker.cf/v1/yuri')
        yurijson = await request.json()
    embed = discord.Embed()
    embed.set_author(name="Yuri", url=yurijson['url'])
    embed.set_image(url=yurijson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="If the Image is not loading just click the title")
    await ctx.send(embed=embed)

@yuri.error
async def yuri_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This Command is on a cooldown. Try again in a few seconds.", delete_after=5)
    elif isinstance(error, NSFWChannelRequired):
        await ctx.send("NSFW Channel is required to run this command", delete_after=5)

@client.command()
async def suggest(ctx):
    await ctx.send('Have any suggestion for the bot? Join the Help Server! https://discord.gg/6JkmzhDsps')

@client.command()
async def kill(ctx, member : discord.Member):
    kills = random.choice([f'{member.display_name} got killed by {ctx.message.author.display_name} with a banana',
                        f'{member.display_name} choked on air',
                        f'{member.display_name} got stabbed by a monkey',
                        f'{member.display_name} got killed by a creeper explosion. Haha noob',
                        f'{member.display_name} I slapped you and you died of shock', 
                        f"{ctx.message.author.display_name} ordered me to kill you but I refuse!", 
                        f'{member.display_name} got smashed by an ant',
                        f'{member.display_name} died of death',
                        f'{member.display_name} picked one of the thousand ways to bite into grass',
                        f'{member.display_name} wanted to go to his Grandma but then slipped over a stone a died'])
    if ctx.message.author == member:
        await ctx.send(f"You cant kill yourself {ctx.message.author.display_name}. Tag someone else to kill")
    else:
        await ctx.send(kills)



# help

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", color=0xFFFF00)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.set_thumbnail(url='https://i.postimg.cc/xdyWm6Fj/images.jpg')
    embed.add_field(name="**General Commands**", value="■ `.ping`\n■ `.8ball`\n■ `.pussy`\n■ `.serverinfo`\n■ `.roll`\n■ `.suggest`\n■ `.kill`\n■ `.invite`\n■ `.repeat (aliases: say)`", inline=True)
    embed.add_field(name="**Reddit Command**", value="■ `.reddit <your subreddit here>`", inline=True)
    embed.add_field(name="**Anime Related Commands**", value="■ `.anime`\n■ `.neko`\n■ `.blush`", inline=True)
    embed.add_field(name="**NSFW Commands**", value="■ `.hentai`\n■ `.trap`\n■ `.nsfwneko`\n■ `.animeweb`", inline=True)
    embed.add_field(name="**Commands for Moderators**", value="■ `.clear`\n■ `.kick`\n■ `.ban`\n■ `.unban`")
    embed.set_footer(text='Need more information? Try .dhelp for detailed Information and .nsfwhelp for detailed Information about the NSFW commands!' )
    await ctx.send(embed=embed)

@client.command()
async def dhelp(ctx):
    embed = discord.Embed(title="Detailed Information", color=0xFFFF00)
    embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
    embed.add_field(name="General Command Infomration", value="**What does `.ping` do?**\nThe `.ping` command shows you the response time for the Bot, that means how long the Bot takes to answer to your command\n**What does `.8ball` do?**\nType `.8ball` and a random question, the Bot now will give you a random logical answer to your question.\n**What does `.pussy` do and is it NSFW?**\nThe `.pussy` command is not NSFW related. It shows you a random cute cat with a funny Title.\n**What does `.serverinfo` do?**\nThis command is self explanatory, it shows you Information about your Server in a cool Embed.\n**What does `.roll` do?**\nThe `.roll` command gives you a random number between 1 and 100.\n**What is `.suggest`?**\n The `.suggest` command invites you to the official Hugo,py Help Server, where you can suggest things, report Bugs or get help by Moderators!\n**What does `.kill` do?**\n`.kill` lets you kill people in different funny ways! **this is NOT nsfw and DOES NOT promote suicide!!!**", inline=False)
    embed.add_field(name="Reddit Command Information", value="**What does the `.reddit` command do?**\nWith the `.reddit` command you can search for random pictures on a subreddit by your choice! If you just type in `.reddit` it will give you a random image from the Meme Subreddit. Be aware, if you try to execute a NSFW Subreddit it won't work!.", inline=False)
    embed.add_field(name="Anime Related Command Information", value="**What does `.anime` do?**\nThe `.anime` command fetches you a random Image from a Library with 52.199 Anime pictures.\n**What does `.neko` do?**\nThe command `.neko` fetches you a random neko Image from a Library that contains 33.046 Neko Images.\n**What does `.blush` do?**\nThe command `.blush` is something more likely used for Roleplay, it gives you a random Anime character that blushes and says: `[Username] blushes`\n**What does `.animeweb` do?**\nThe command `.animeweb` sends you a random website where you can watch anime on!", inline=False)
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
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry you are missing permission for that"
        await ctx.send(text)
    else:
        await ctx.send(f'Please specifiy an amount of messages to delete.', delete_after=5)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
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
        await ctx.send('Please mention the member you want to ban.')


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
    description = ctx.guild.description

    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    memberCount = ctx.guild.member_count

    icon = ctx.guild.icon_url

    embed = discord.Embed(title=name + " Server Information", description=description, color=0xFFFF00)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Total Members", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def animeweb(ctx):
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

# Reddit (I should learn cogs)

REDDIT_APP_ID = os.getenv("RAI")
REDDIT_APP_SECRET = os.getenv("RAS")
USERNAME = os.getenv("user")
PASSWORD = os.getenv("pass")

rreddit = praw.Reddit(client_id = os.environ['RAI'],
                    client_secret = os.environ['RAS'],
                    username = os.environ['user'],
                    password = os.environ['pass'],
                    user_agent = 'SSagunPraw')

@client.command()
@cooldown(1, 8)
async def reddit(ctx, subred = "meme"):  # default subreddit is meme
    subreddit = rreddit.subreddit(subred)
    all_subs = []

    top = subreddit.top(limit = 75)

    for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)

    if submission.over_18 == True:
        await ctx.send("Sorry but this subreddit is marked as NSFW!")
    else: 
        sr_name = random_sub.subreddit
        author = random_sub.author
        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title=author, description=name, color=0xFF4500)
        embed.set_author(name=f'r/{sr_name}',url=url, icon_url='https://i.postimg.cc/pTzSdRqC/reddit-logo.png')
        embed.set_image(url=url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"If the Image is not loading just click on r/{sr_name}")
        await ctx.send(embed=embed)

@reddit.error
async def reddit_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Woah Woah you are too fast! Try again in a few seconds", delete_after=5)


@client.command()
async def invite(ctx):
    await ctx.send('Thanks for the thoughts of inviting me! https://discord.com/api/oauth2/authorize?client_id=832922273597227019&permissions=4582438&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D')


@client.command(aliases=["say"])
async def repeat(ctx, *, repeat):
    if repeat == "i am stupid":
        await ctx.send("We know")
    else:
        await ctx.send(repeat)

client.run(os.environ['DISCORD_TOKEN'])