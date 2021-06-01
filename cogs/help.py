import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Commands", color=0xFFFF00)
        embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
        embed.set_thumbnail(url='https://i.postimg.cc/xdyWm6Fj/images.jpg')
        embed.add_field(name="**General Commands**", value="■ `h!ping`\n■ `h!8ball`\n■ `h!pussy`\n■ `h!serverinfo`\n■ `h!roll`\n■ `h!support`\n■ `h!kill`\n■ `h!invite`\n■ `h!repeat (aliases: say)`\n■ `h!avatar`\n■ `h!userinfo`", inline=True)
        embed.add_field(name="**Reddit Command**", value="■ `h!reddit <your subreddit here>`", inline=True)
        embed.add_field(name="**Roleplay Commands**", value="■ `h!kiss`\n■ `h!cry`\n■ `h!hug`\n■ `h!poke`\n■ `h!lick`\n■ `h!pat`\n■ `h!nom`\n■ `h!pout`\n■ `h!punch`\n■ `h!slap`\n■ `h!blush`\n■ `h!smug`\n■ `h!sleep`", inline=True)
        embed.add_field(name="**Anime Related Commands**", value="■ `h!anime`\n■ `h!neko`\n■ `h!animeweb`", inline=True)
        embed.add_field(name="**NSFW Commands**", value="■ `h!hentai`\n■ `h!trap`\n■ `h!nsfwneko`", inline=True)
        embed.add_field(name="**Commands for Moderators**", value="■ `h!clear`\n■ `h!kick`\n■ `h!ban`\n■ `h!unban`")
        embed.set_footer(text='Hope this helped! If you have questions join the Help-Server! h!support' )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(helpCog(bot))