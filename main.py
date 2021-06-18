import datetime
import discord
import os
import random
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

topggtoken = os.getenv("TOPGGTOKEN")
token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=get_prefix, intents=Intents.all())
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



# Botinfo

@client.command()
@cooldown(1, 10, commands.BucketType.user)
async def botinfo(ctx):
    activeservers = client.guilds

    sum = 0

    for s in activeservers:
        sum += len(s.members)
    

    embed = discord.Embed(title="Hugo.py │ Information about me", description="Hello! I am Hugo.py. Nice to meet you!\n\n", color=0xFFFFFF)

    embed.set_thumbnail(url='https://i.postimg.cc/sD6BcgbH/letter-h-logo-idea-monogram-weave-of-vector-13221348-2.jpg')


    embed.add_field(name="About me", value="**Name:** Hugo.py#9153\n**ID:** 832922273597227019\n**Avatar:** [Click Me!](https://i.postimg.cc/sD6BcgbH/letter-h-logo-idea-monogram-weave-of-vector-13221348-2.jpg)\n**Prefix:** `h!`\n**My Developer:** SSagun.py#6969 **ID:** 544810950952353823", inline=False)
    
    embed.add_field(name="Short description", value="Image commands / Roleplay commands and more! Simple and Easy to use Bot for especially your Anime Server!", inline=False)

    embed.add_field(name="Info about my Servers and Users", value=f"**Amount of Servers I serve:** {len(client.guilds)} Servers\n**Users Active:** {sum} Users!\n**Raw Latency:** {client.latency * 100}ms", inline=False)

    embed.add_field(name="Support me!", value="[Vote for me!](https://top.gg/bot/832922273597227019/vote) - [Support Server](https://discord.gg/6JkmzhDsps) - [Invite me](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot)")


    embed.timestamp = datetime.datetime.utcnow()


    embed.set_footer(text=f"Requested by {ctx.message.author}")


    await ctx.send(embed=embed)



# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!\n```{client.latency * 100}```')


# Bot owner only commands

@client.command(pass_context=True)
@commands.is_owner()
async def servers(ctx):

        activeservers = client.guilds

        for guild in activeservers:

            await ctx.send(guild.name)

            print(guild.name)


# Help 1

@client.command()
async def help(ctx):
    reddit = '<:reddit:853000371601277018>'
    embed = discord.Embed(title="Hugo.py Commands", description=f"For help join the help Server [here](https://discord.gg/6JkmzhDsps)\nPrefix for this server  `{get_prefix}`", color=0x8962AA)

    embed.add_field(name='⚙️ General Commands', value="`ping`  `8ball`  `pussy`\n`serverinfo`  `roll`  `support`\n`kill`  `invite`  `repeat`\n`avatar`  `userinfo`  `wallpaper`\n`botinfo`", inline=True)
    embed.add_field(name="🎭 Roleplay Commands", value="`kiss`  `cry`  `hug`  `poke`\n`lick`  `pat`  `nom`  `pout`\n`punch`  `slap`  `blush`\n`smug`  `sleep`  `tickle`", inline=True)
    embed.add_field(name="🖋 Anime Commands", value="`anigirl`  `neko`  `animeweb`  `anime <Anime Name>`  `manga <Manga Name>`", inline=True)
    embed.add_field(name="🔞 NSFW Commands", value="`hentai`  `trap`  `thighs`\n`boobs`  `yuri`", inline=True)
    embed.add_field(name=f"{reddit} Reddit Command", value="`reddit <your subreddit here>`", inline=True)
    embed.add_field(name="🔎 Moderator Commands", value="`ban`  `kick`  `clear`\n`mute`  `unmute`  `unban`  `prefix`  `clearprefix`", inline=True)
    embed.add_field(name="About the Bot", value="[Invite the bot](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot) - [Join the Help Server](https://discord.gg/6JkmzhDsps) - [Vote for me!](https://top.gg/bot/832922273597227019/vote)", inline=False)
    
    embed.set_footer(text="Dont know how to use the Moderator commands? Just send h!mod")

    await ctx.send(embed=embed)

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

    'cogs.config'
    
]

if __name__ == '__main__':

    client.mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("mongodata"))

    client.db = client.mongo["discord"]

    client.prefixes = discordmongo.Mongo(connection_url=client.db, dbname="prefixes")

    for x in ext:

        client.load_extension(x)


update_stats.start()

client.run(os.environ['DISCORD_TOKEN'])