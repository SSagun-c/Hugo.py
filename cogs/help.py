from aiohttp import helpers
import discord
from discord.ext import commands


class helpCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Commands", color=0xFFFF00)
        embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
        embed.set_thumbnail(url='https://i.postimg.cc/xdyWm6Fj/images.jpg')
        embed.add_field(name="**General Commands**", value="■ `h!ping`\n■ `h!8ball`\n■ `h!pussy`\n■ `h!serverinfo`\n■ `h!roll`\n■ `h!support`\n■ `h!kill`\n■ `h!invite`\n■ `h!repeat (aliases: say)`\n■ `h!avatar`\n■ `h!userinfo`", inline=True)
        embed.add_field(name="**Reddit Command**", value="■ `h!reddit <your subreddit here>`", inline=True)
        embed.add_field(name="**Anime Related Commands**", value="■ `h!anime`\n■ `h!neko`\n■ `h!blush`\n■ `h!animeweb`", inline=True)
        embed.add_field(name="**NSFW Commands**", value="■ `h!hentai`\n■ `h!trap`\n■ `h!nsfwneko`", inline=True)
        embed.add_field(name="**Commands for Moderators**", value="■ `h!clear`\n■ `h!kick`\n■ `h!ban`\n■ `h!unban`")
        embed.set_footer(text='Need more information? Try h!dhelp for detailed Information and h!nsfwhelp for detailed Information about the NSFW commands!' )
        await ctx.send(embed=embed)


    @commands.command()
    async def dhelp(self, ctx):
        embed = discord.Embed(title="Detailed Information", color=0xFFFF00)
        embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
        embed.add_field(name="General Command Infomration", value="**What does `h!ping` do?**\nThe `h!ping` command shows you the response time for the Bot, that means how long the Bot takes to answer to your command\n**What does `h!8ball` do?**\nType `h!8ball` and a random question, the Bot now will give you a random logical answer to your question.\n**What does `h!pussy` do and is it NSFW?**\nThe `h!pussy` command is not NSFW related. It shows you a random cute cat with a funny Title.\n**What does `h!serverinfo` do?**\nThis command is self explanatory, it shows you Information about your Server in a cool Embed.\n**What does `h!roll` do?**\nThe `h!roll` command gives you a random number between 1 and 100.\n**What is `h!support`?**\n The `h!support` command invites you to the official Hugo.py Help Server, where you can suggest things, report Bugs or get help by Moderators!\n**What does `h!kill` do?**\n`h!kill` lets you kill people in different funny ways! **this is NOT nsfw and DOES NOT promote suicide!!!**\n**What is `h!userinfo`?\nThis command gives you highly detailed information about a member who is in the same server as you", inline=False)
        embed.add_field(name="Reddit Command Information", value="**What does the `h!reddit` command do?**\nWith the `h!reddit` command you can search for random pictures on a subreddit by your choice! If you just type in `.reddit` it will give you a random image from the Meme Subreddit. Be aware, if you try to execute a NSFW Subreddit it won't work!.", inline=False)
        embed.add_field(name="Anime Related Command Information", value="**What does `h!anime` do?**\nThe `h!anime` command fetches you a random Image from a Library with 52.199 Anime pictures.\n**What does `h!neko` do?**\nThe command `h!neko` fetches you a random neko Image from a Library that contains 33.046 Neko Images.\n**What does `h!blush` do?**\nThe command `h!blush` is something more likely used for Roleplay, it gives you a random Anime character that blushes and says: `[Username] blushes`\n**What does `h!animeweb` do?**\nThe command `h!animeweb` sends you a random website where you can watch anime on!", inline=False)
        embed.add_field(name="Moderator Command Information", value="**All the now listed commands are only for Administrators!**\n**What is `h!clear` for?**\n`.clear` deletes your selected amount of messages to deleted in one channel.\n**What does `h!ban` do?**\nI think this command is self explanatory but `h!ban` bans the user you mentioned from the Server.\n**What does `h!unban` do?**\nThis command requires you to write the users name you banned once with his Discriminator. As an Example: `h!unban SSagun.py#6969`", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def nsfwhelp(self, ctx):
        embed = discord.Embed(title="NSFW Command Information", color=0x9ACD32)
        embed.set_author(name="SSagun.py#6969", url="https://www.instagram.com/ssagun.py/", icon_url="https://i.postimg.cc/KjhmssMM/sagunicon.jpg")
        embed.set_thumbnail(url='https://i.postimg.cc/RhHXLLBF/unnamed.jpg')
        embed.add_field(name="NSFW Commands", value="**KEEP IN MIND**\nThe channel has to be NSFW for the commands to work!\n**What does `h!hentai` do?**\n`h!hentai` sends you a random Hentai Image from a Library that contains 33.677 Images\n**What does `h!trap` do?**\nDo you like Traps? `h!trap` sends you a random Trap related Image from a Library that contains 25.358 Trap Images\n**What does `h!nsfwneko` do?**\nThe `h!nsfwneko` command sends you a random lewded neko Image from a Library that contains 22.017 Lewded Neko Images **PLEASE REPORT WHEN THIS BOT IS SENDING MINORS** `h!support`.\n**What is `h!yuri`?**\nThe command `h!yuri` sends a random Image from a Library that contains 26.867 Images. Yuri means Lesbian.", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(helpCog(bot))