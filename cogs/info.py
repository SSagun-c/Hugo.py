import discord
import datetime
from discord.ext import commands
from discord import Member, Embed
from typing import Optional

from discord.ext.commands.core import cooldown

class infoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['memberinfo', 'mi', 'ui'])
    async def userinfo(self, ctx, target: Optional[Member]):
        target = target or ctx.message.author

        embed = discord.Embed(title='User Information', colour=target.colour, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)
        fields = [("ID", target.id, False),
                ("Name", str(target), True),
                ("Bot?", target.bot, True),
                ("Highest Role", target.top_role.mention, True),
                ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                ("Created at:", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("Joined at:", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("Boost", bool(target.premium_since), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)


    @commands.command(aliases=["si", "gi"])
    async def serverinfo(self, ctx):
        embed = Embed(title="Server information",
                        colour=ctx.guild.owner.colour,
                        timestamp=datetime.datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("ID", ctx.guild.id, True),
                    ("Owner", ctx.guild.owner, True),
                    ("Region", ctx.guild.region, True),
                    ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                    ("Members", len(ctx.guild.members), True),
                    ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                    ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                    ("Banned members", len(await ctx.guild.bans()), True),
                    ("Statuses", f"🟢 {statuses[0]}  🟠 {statuses[1]}  🔴 {statuses[2]}  ⚪ {statuses[3]}", True),
                    ("Text channels", len(ctx.guild.text_channels), True),
                    ("Voice channels", len(ctx.guild.voice_channels), True),
                    ("Categories", len(ctx.guild.categories), True),
                    ("Roles", len(ctx.guild.roles), True),
                    ("Invites", len(await ctx.guild.invites()), True),
                    ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(infoCog(bot))