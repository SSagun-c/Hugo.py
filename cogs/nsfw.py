from re import I
from turtle import color
import discord
import aiohttp
import datetime as dt
from discord import member
from typing import Optional
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class roleplayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="waifu", 
    aliases=["waifu"
    "neko"
    "shinobu"
    "megumin"
    "bully"
    "cuddle"
    "cry"
    "hug"
    "awoo"
    "kiss"
    "lick"
    "pat"
    "smug"
    "bonk"
    "yeet"
    "blush"
    "smile"
    "wave"
    "highfive"
    "handhold"
    "nom"
    "bite"
    "glomp"
    "slap"
    "kill"
    "kick"
    "happy"
    "wink"
    "poke"
    "dance"
    "cringe"])
    @commands.cooldown(1, 5, BucketType.user)
    async def rp(self, ctx):
        commandDefine = ctx.message
        print(commandDefine)

        async with aiohttp.ClientSession() as Ses:
            request = await Ses.get("https://api.waifu.pics/sfw/" + {commandDefine})
            rpjson = await request.json()
        
        embed = discord.Embed(color=0xc777d9)
        embed.set_author(ctx.message.author.display_name, url=rpjson['url'])
        embed.set_image(url=rpjson.url)
        embed.timestamp = dt.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(roleplayCog(bot))