import datetime
from re import escape
import discord
import os
import random
import topgg
from discord.ext import commands, tasks
from discord import Intents
from itertools import cycle
from discord.ext.commands import cooldown

topggtoken = os.getenv("TOPGGTOKEN")
token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix='h!', intents=Intents.all())
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
                embed = discord.Embed(title=f"❌ Sorry {ctx.message.author.display_name}, either you or I am missing permissions to do this", color=0xFF0000)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(title=f"❌ Its a regired Argument thats missing", color=0xFF0000)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.CommandOnCooldown):
                embed = discord.Embed(title=f"❌ Ratelimited. Try again in {error.retry_after:,.2f} secs.")
                await ctx.send(embed=embed)
                
            elif isinstance(error, commands.NSFWChannelRequired):
                embed = discord.Embed(title="❌ This is not a NSFW Channel")
                await ctx.send(embed=embed)



# Botinfo

@client.command()
@cooldown(1, 10, commands.BucketType.user)
async def botinfo(ctx):
    activeservers = client.guilds

    sum = 0

    for s in activeservers:
        sum += len(s.members)
    

    embed = discord.Embed(title="Information about me", color=0xFF00FF)


    embed.add_field(name="Servers", value=f"{len(client.guilds)} Servers", inline=True)

    embed.add_field(name="Users", value=f"{sum} Users", inline=True)

    embed.add_field(name="Latency", value=f"{client.latency * 100}ms")

    embed.add_field(name="Support me", value="[Vote for me](https://top.gg/bot/832922273597227019/vote) │ [Invite me](https://top.gg/bot/832922273597227019) │ [Help Server](https://discord.gg/6JkmzhDsps)")

    embed.set_footer(text=f"Requested by {ctx.message.author}")

    embed.timestamp = datetime.datetime.utcnow()


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

# Loads all of the Cogs

client.load_extension('cogs.help')
client.load_extension('cogs.image')
client.load_extension('cogs.info')
client.load_extension('cogs.misc')                    # I really could do this simpler
client.load_extension('cogs.moderator')
client.load_extension('cogs.reddit')
client.load_extension('cogs.roleplay')
client.load_extension('cogs.anime')
update_stats.start()
client.run(os.environ['DISCORD_TOKEN'])