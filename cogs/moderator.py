import discord
import datetime
from discord.ext import commands

class moderatorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.message.delete()
        embed = discord.Embed(title="Case: Kick", description=f"User: {member}", color=0xf1c40f)
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="Reason", value=f"{reason}")
        embed.set_footer(text=f"Kicked by {ctx.message.author}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        embed = discord.Embed(title="Case: Ban", description=f"User: {member}", color=0xe74c3c)
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="Reason", value=f"{reason}")
        embed.set_footer(text=f"Banned by {ctx.message.author}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member : int):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member} on {datetime.datetime.utcmow()} by {ctx.message.author}')
                return


def setup(bot):
    bot.add_cog(moderatorCog(bot))