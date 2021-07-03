import datetime, time
import discord
import os
import asyncio
import discordmongo
import topgg
import motor.motor_asyncio
from discord.ext import commands, tasks
from discord import Intents
from itertools import cycle
from discord.ext.commands import cooldown

async def get_prefix(client, message):

    if not message.guild:

        return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)
    
    try:

        data = await client.prefixes.find(message.guild.id)

        if not data or "prefix" not in data:
            
            return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)

        return commands.when_mentioned_or(data["prefix"])(client, message)

    except:

        return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)

topggtoken = os.getenv("topgg")
token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=get_prefix, intents=Intents.all(),  case_insensitive=True)
client.DEFAULT_PREFIX = "h!"
client.remove_command('help')

dbl_token = topggtoken
client.topgg = topgg.DBLClient(client, dbl_token)

# Events

@tasks.loop(seconds=120)
async def change_status():

    status = cycle([f'with {len(client.guilds)} Servers! h!help'])

    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():

    change_status.start()

    print("Bot is online and ready to use!")

    global startTime
    startTime = time.time()

@tasks.loop(minutes=30)
async def update_stats():

    try:

        await client.topgg.post_guild_count()

        print(f"Posted!")

    except Exception as e:

        print(f"Failed! \n{e.__class__.__name__}: {e}")

@client.event
async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                embed = discord.Embed(title=f"❌ {error}", color=0xFF0000)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(title=f"❌ {error}", color=0xFF0000)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.CommandOnCooldown):
                embed = discord.Embed(title=f"❌ Ratelimited. Try again in {error.retry_after:,.2f} secs.", color=0xFF0000)
                await ctx.send(embed=embed)
                
            elif isinstance(error, commands.NSFWChannelRequired):
                embed = discord.Embed(title="❌ Uh Oh looks like this is not a NSFW Channel", color=0xFF0000)
                await ctx.send(embed=embed)

@client.event
async def on_guild_remove(guild):

    await client.prefixes.unset({"_id": guild.id, "prefix": 1})
    print(f"Left {guild.name}")

    logchannel = client.get_channel(857276576269729884)
    await logchannel.send(f"Left {guild.name}")

@client.event
async def on_guild_join(guild):

    logchannel = client.get_channel(857276576269729884)

    await logchannel.send(f"Joined {guild.name}")

# Botinfo

@client.command(aliases=['about', 'info'])
@cooldown(1, 10, commands.BucketType.user)
async def botinfo(ctx):
    activeservers = client.guilds

    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))

    sum = 0

    for s in activeservers:
        sum += len(s.members)
    

    embed = discord.Embed(title="Hugo.py │ Information about me", description="Hello! I am Hugo.py. Nice to meet you!\n\n", color=0xFFFFFF)

    embed.set_thumbnail(url='https://i.postimg.cc/sD6BcgbH/letter-h-logo-idea-monogram-weave-of-vector-13221348-2.jpg')


    embed.add_field(name="💠 About me", value="**Name:** Hugo.py#9153\n**ID:** 832922273597227019\n**Avatar:** [Click Me!](https://i.postimg.cc/sD6BcgbH/letter-h-logo-idea-monogram-weave-of-vector-13221348-2.jpg)\n**Standardprefix:** `h!`\n**My Developer:** SSagun.py#6969 **ID:** 544810950952353823", inline=False)
    
    embed.add_field(name="💠 Short description", value="Image commands / Roleplay commands and more! Simple and Easy to use Bot for especially your Anime Server!", inline=False)

    embed.add_field(name="💠 Info about my Servers and Users", value=f"**Amount of Servers I serve:** {len(client.guilds)} Servers\n**Users Active:** {sum} Users!\n**Raw Latency:** {client.latency * 100}ms", inline=False)

    embed.add_field(name="💠 Uptime", value=uptime, inline=False)

    embed.add_field(name="💠 Support me!", value="[Vote for me!](https://top.gg/bot/832922273597227019/vote) - [Support Server](https://discord.gg/6JkmzhDsps) - [Invite me](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot)")


    embed.timestamp = datetime.datetime.utcnow()


    embed.set_footer(text=f"Requested by {ctx.message.author}")


    await ctx.send(embed=embed)

# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!\n```{client.latency * 100}ms```')


@client.command()
async def report(ctx, *, report):

    channel = client.get_channel(856146296607997983)

    embed = discord.Embed(title=f"Report from {ctx.message.author}", description=report, color=0xFF0000)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_footer(text=f"Reported by {ctx.message.author}")

    await ctx.send("Sending your report...")

    await channel.send(embed=embed)

    await asyncio.sleep(3)

    em = discord.Embed(title=f"Hello {ctx.message.author.display_name}, thanks for reporting your issue we will try to fix it as soon as possible!", description="For more information join the [help server](https://discord.gg/6JkmzhDsps)", color=0x0000FF)
    await ctx.send(embed=em)


# Bot owner only commands

@client.command(pass_context=True)
@commands.is_owner()
async def servers(ctx):

        activeservers = client.guilds

        for guild in activeservers:

            await ctx.send(guild.name)

            print(guild.name)


# Loads all of the Cogs

ext = [

    'cogs.anime',

    'cogs.help',

    'cogs.image',

    'cogs.info',

    'cogs.misc',

    'cogs.moderator',

    'cogs.reddit',

    'cogs.roleplay',

    'cogs.config',

    'cogs.imagemanipulation',

    'cogs.nsfwsearch',
    
    'cogs.weather'
    
]

if __name__ == '__main__':

    client.mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("mongodata"))

    client.db = client.mongo["discord"]

    client.prefixes = discordmongo.Mongo(connection_url=client.db, dbname="prefixes")

    for x in ext:

        client.load_extension(x)


update_stats.start()

client.run(os.environ['DISCORD_TOKEN'])