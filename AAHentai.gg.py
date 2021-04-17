import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')


# Commands

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('hanime.tv'))
    print("Bot is online and ready to use!")


# Fun commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

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


# help

@client.command()
async def help(ctx):
    await ctx.send(f'**Command prefix** "." \n**Help**\n  *help*\n**Fun Commands**\n  *ping 8ball*\n**Moderator commands (admin permissions required)**\n  *clear kick ban*')


# Moderator commands

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



client.run("ODMyOTIyMjczNTk3MjI3MDE5.YHq1UA._bgG5OsCWv8AcwhVTyrnaeEDNc0")