import discord
from discord.ext import commands



class errorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"Sorry {ctx.message.author.display_name}, you do not meet the required permissions.", delete_after=5)
            elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("One or more required Arguments are missing", delete_after=5)
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"That command is on cooldown. Try again in {error.retry_after:,.2f} secs.", delete_after=5)
            elif isinstance(error, commands.NSFWChannelRequired):
                await ctx.send("NSFW Channel is required to run this command", delete_after=5)