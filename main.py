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
    status = cycle(['with some users... h!help', 'annoying my guy Unnamed... h!help', 'osu! h!help', 'with you... h!help'])
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    print("Bot is online and ready to use!")


@client.event
async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"Sorry {ctx.message.author.display_name}, you do not meet the required permissions.", delete_after=5)
            elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("One or more required Arguments are missing", delete_after=5)
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"That command is on cooldown. Try again in {error.retry_after:,.2f} secs.", delete_after=5)
            elif isinstance(error, commands.NSFWChannelRequired):
                await ctx.send("NSFW Channel is required to run this command", delete_after=5)


@client.event
async def on_message(message):
    messages = ['hugo sucks',
                'hugo is trash',
                'hugo is ass']
    answers = ['Wow that hurt...',
               'sorry',
               'Yikes...']
    if messages in message.content:
        await message.channel.send(random.choice(answers))


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
client.run(os.environ['DISCORD_TOKEN'])