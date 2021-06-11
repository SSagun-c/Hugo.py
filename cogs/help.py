import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(title="Currently being edited", description="For help join the help Server [here](https://discord.gg/6JkmzhDsps)\nPrefix  `h!`", color=0x8962AA)

        embed.add_field(name='⚙ General Commands', value="`ping` `8ball` `pussy`\n`serverinfo` `roll` `support`\n`kill` `invite` `repeat`\n`avatar` `userinfo` `wallpaper`", inline=True)
        embed.add_field(name="🎭 Roleplay Commands", value="`kiss` `cry` `hug` `poke`\n`lick` `pat` `nom` `pout`\n`punch` `slap` `blush`\n`smug` `sleep` `tickle`", inline=True)
        embed.add_field(name="About the Bot", value="[Invite the bot](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot) - [Join the Help Server](https://discord.gg/6JkmzhDsps) - [Vote for me!](https://top.gg/bot/832922273597227019/vote)", inline=False)

        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpCog(bot))