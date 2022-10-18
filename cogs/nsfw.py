import discord
import hmtai
from discord.ext import commands
from discord.ext.commands import cooldown


class nsfwimgCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="image")
    @commands.is_nsfw()
    
