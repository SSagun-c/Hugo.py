import discord
import os
from discord.ext import commands
from discord import Intents

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='h!', intents=Intents.all())

client.remove_command('help')

# Events

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")

@client.event
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"You and {len(client.guilds)} other Servers︱h!help"))


# Ping

@client.command()
async def ping(ctx):
    await ctx.send(f'```{client.latency * 1000}ms```')


# Loads all of the Cogs

extensions = ['cogs.moderator', 'cogs.error', 'cogs.info', 'cogs.image', 'cogs.help', 'cogs.reddit', 'cogs.misc']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

client.run(os.environ['DISCORD_TOKEN'])