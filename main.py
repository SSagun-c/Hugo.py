import discord
import os
import random
import topgg
from discord.ext import commands, tasks
from discord import Intents
from itertools import cycle

token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='h!', intents=Intents.all())
bot.remove_command('help')

dbl_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgzMjkyMjI3MzU5NzIyNzAxOSIsImJvdCI6dHJ1ZSwiaWF0IjoxNjIzNTk0MjM3fQ.B7SfrpVkf7ilGU2JiVPE7xy8Fn49wqWiLpZ1yy7X6Do"
bot.topggpy = topgg.DBLClient(bot, dbl_token)

# Events

@tasks.loop(seconds=120)
async def change_status():
    status = cycle([f'with {len(bot.guilds)} Servers! h!help'])
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

@tasks.loop(minutes=30)
async def update_stats():
    try:
        await bot.topgg.post_guild_count()
        print(f"Posted!")
    except Exception as e:
        print(f"Failed! \n{e.__class__.__name__}: {e}")




@bot.event
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


# Ping

@bot.command()
async def ping(ctx):
    await ctx.send(f'```{bot.latency * 1000}ms```')


# Bot owner only commands
@bot.command(pass_context=True)
@commands.is_owner()
async def servers(ctx):
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)

# Loads all of the Cogs

bot.load_extension('cogs.help')
bot.load_extension('cogs.image')
bot.load_extension('cogs.info')
bot.load_extension('cogs.misc')                    # I really could do this simpler
bot.load_extension('cogs.moderator')
bot.load_extension('cogs.reddit')
bot.load_extension('cogs.roleplay')
update_stats.start()
bot.run(os.environ['DISCORD_TOKEN'])