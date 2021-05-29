import discord
import datetime
from discord import client
from discord.ext import commands

class moderatorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount + 1)

    @client.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} got kicked at {datetime.datetime.utcnow()} because of: {reason}')

    @client.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        embed = discord.Embed(title="Case: Ban", description=f"User: {member}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="Reason", value=f"{reason}")
        embed.set_footer(text=f"Banned by {ctx.message.author}")
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(moderatorCog(bot))