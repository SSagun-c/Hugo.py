import discord
import os
from discord.ext import commands
from discord import Intents

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='h!', intents=Intents.all())

activity = discord.Activity(type=discord.ActivityType.watching, name=f"Your and {len(client.guilds)} other servers // h!help")

client.remove_command('help')

# Events

@client.event
async def on_ready():
    print("Bot is online and ready to use!")


# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'```{client.latency * 1000}ms```')


# Loads all of the Cogs

client.load_extension('cogs.error')
client.load_extension('cogs.help')
client.load_extension('cogs.image')
client.load_extension('cogs.info')
client.load_extension('cogs.misc')
client.load_extension('cogs.moderator')
client.load_extension('cogs.reddit')

client.run(os.environ['DISCORD_TOKEN'])