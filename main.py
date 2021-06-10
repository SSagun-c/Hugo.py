import discord
import os
import random
from discord.ext import commands, tasks
from discord import Intents
from itertools import cycle

token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix='h!', intents=Intents.all())
client.remove_command('help')


# Events

@tasks.loop(seconds=120)
async def change_status():
    status = cycle([f'with {len(client.guilds)} Servers! h!help'])
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")


@client.event
async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"Sorry {ctx.message.author.display_name}, either you or I am missing permissions to do this.")
            elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("One or more required Arguments are missing")
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"That command is on cooldown. Try again in {error.retry_after:,.2f} secs.")
            elif isinstance(error, commands.NSFWChannelRequired):
                await ctx.send("NSFW Channel is required to run this command")


# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'```{client.latency * 1000}ms```')


# Loads all of the Cogs

client.load_extension('cogs.help')
client.load_extension('cogs.image')
client.load_extension('cogs.info')
client.load_extension('cogs.misc')                    # I really could do this simpler
client.load_extension('cogs.moderator')
client.load_extension('cogs.reddit')
client.load_extension('cogs.roleplay')
client.run(os.environ['DISCORD_TOKEN'])