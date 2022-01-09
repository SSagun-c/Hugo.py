import discord
import datetime as dt
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

class InformationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help_command(self, ctx):
        """This command shows a list with all commands"""
        reddit_emote = '<:reddit:872393789761781780>'
        
        embed = discord.Embed(title="My command list", color=0xED61D3)
        embed.add_field(name='🎈 Misc Commands', value="`ping` | `8ball` | `pussy` | `serverinfo` | `roll` | `support` | `kill` | `invite` | `repeat` | `avatar` | `userinfo` | `wallpaper` | `botinfo` | `wouldyourather` | `weather <city>`", inline = False)
        embed.add_field(name='🎭 Roleplay Commands', value="`bully` | `cuddle` | `cry` | `poke` | `lick` | `pat` | `nom` | `hug` | `kiss` | `smug` | `blush` | `bonk` | `yeet` | `smile` | `wave` | `highfive` | `handhold` | `bite` | `glomp` | `slap` | `kill` | `kick` | `happy` | `wink` | `dance` | `cringe", inline = False)
        embed.add_field(name='🖋 Anime Commands', value="`waifu` | `neko` | `awoo` | `shinobu` | `anime <Anime Name>` | `manga <Manga Name>`")
        embed.add_field(name='🔞 NSFW Commands', value="`hentai` | `trap` | `thighs` | `boobs` | `yuri` | `bondage` | `bdsm` | `ass` | `cum` | `tentacles` | `blowjob` | `masturbation` | `ero` | `ahegao` | `uniform`", inline = False)
        embed.add_field(name=f'{reddit_emote} Reddit Command', value="`reddit <your subreddit here> (takes up to 10 seconds)`", inline = False)
        embed.add_field(name="About the Bot", value="[Invite the bot](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot) - [Vote for me!](https://top.gg/bot/832922273597227019/vote)", inline=False)
        embed.timestamp = dt.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InformationCog(bot))