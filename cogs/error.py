from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, MissingPermissions, MissingRequiredArgument

class errorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author.display_name}, you do not meet the required permissions.")
        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("One or more required Arguments are missing")
        elif isinstance(exc, CommandOnCooldown):
            await ctx.send(f"That command is on {str(exc.cooldown.type).split('.')[-1]} cooldown. Try again in {exc.retry_after:,.2f} secs.")

def setup(bot):
    bot.add_cog(errorCog(bot))