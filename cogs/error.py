from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, MissingPermissions, MissingRequiredArgument, NSFWChannelRequired

class errorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def on_command_error(self, ctx, exc):
        if isinstance(exc, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author.display_name}, you do not meet the required permissions.")
        elif isinstance(exc, commands.MissingRequiredArgument):
            await ctx.send("One or more required Arguments are missing")
        elif isinstance(exc, commands.CommandOnCooldown):
            await ctx.send(f"That command is on {str(exc.cooldown.type).split('.')[-1]} cooldown. Try again in {exc.retry_after:,.2f} secs.")
        elif isinstance(exc, commands.NSFWChannelRequired):
            await ctx.send("NSFW Channel is required to use this command")

def setup(bot):
    bot.add_cog(errorCog(bot))