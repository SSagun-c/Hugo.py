import discord
import os
from discord.ext import commands, tasks
from discord import Intents
from itertools import cycle

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='h!', intents=Intents.all())

client.remove_command('help')

# Events

@tasks.loop(seconds=120)
async def change_status():
    status = cycle(['with some users... h!help', 'annoying my guy Unnamed... h!help', 'osu! h!help', 'with you... h!help'])
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'```{client.latency * 1000}ms```')


# Loads all of the Cogs

client.load_extension('cogs.help')
client.load_extension('cogs.image')
client.load_extension('cogs.info')
client.load_extension('cogs.misc')
client.load_extension('cogs.moderator')
client.load_extension('cogs.reddit')

client.run(os.environ['DISCORD_TOKEN'])