import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def help(self, ctx):
        reddit = '<:reddit:853000371601277018>'
        embed = discord.Embed(title="Hugo.py Commands", description="For help join the help Server [here](https://discord.gg/6JkmzhDsps)", color=0x8962AA)

        embed.add_field(name='🥳 Misc Commands', value="`ping`  `8ball`  `pussy`  `serverinfo`  `roll`  `support`  `kill`  `invite`  `repeat`  `avatar`  `userinfo`  `wallpaper`  `botinfo`  `wouldyourather`  `weather (shows in metric) <city>`  `iweather (shows in imperial) <city>`", inline=False)
        embed.add_field(name="📸 Image Manipulation", value="`simp`  `license`", inline=False)
        embed.add_field(name="🎭 Roleplay Commands", value="`kiss`  `cry`  `hug`  `poke`  `lick`  `pat`  `nom`  `pout`  `punch`  `slap`  `blush`  `smug`  `sleep`  `tickle`", inline=False)
        embed.add_field(name="🖋 Anime Commands", value="`waifu`  `neko`  `animeweb`  `anime <Anime Name>`  `manga <Manga Name>`", inline=False)
        embed.add_field(name="🔞 NSFW Commands", value="`hentai`  `trap`  `thighs`  `boobs`  `yuri` `bondage`  `bdsm`  `ass`  `cum`  `tentacles`  `blowjob`  `masturbation`  `ero`  `ahegao`  `gif`  `uniform`" , inline=False)
        embed.add_field(name=f"{reddit} Reddit Command", value="`reddit <your subreddit here>`", inline=False)
        embed.add_field(name="🔎 Moderator Commands", value="`ban`  `kick`  `clear`  `mute`  `unmute`  `unban`  `prefix`  `clearprefix`", inline=False)
        embed.add_field(name="About the Bot", value="**Report bugs**\n`report`\n\n[Invite the bot](https://discord.com/oauth2/authorize?client_id=832922273597227019&permissions=269348086&scope=bot) - [Join the Help Server](https://discord.gg/6JkmzhDsps) - [Vote for me!](https://top.gg/bot/832922273597227019/vote)", inline=False)
        
        embed.set_footer(text="Dont know how to use the Moderator commands? Just send h!mod")

        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def mod(self, ctx):
      embed = discord.Embed(title="Info About the Moderation Commands", color=0x738ADB)
     
      embed.add_field(name="Ban", value="`h!ban <Member> <Reason(Optional)>`", inline=False)
      embed.add_field(name="Kick", value="`h!kick <Member> <Reason(Optional)>`", inline=False)
      embed.add_field(name="Mute", value="`h!mute <time(Leave blank for permamute)> <Reason(Optional)>`", inline=False)
      embed.add_field(name="Unban", value="`h!unban <User and Discriminator(e.g. h!unban SSagun.py#6969)>`", inline=False)
      embed.add_field(name="Unmute", value="`h!unmute <member>`", inline=False)
      embed.add_field(name="Clear", value="`h!clear <amount(Please dont exaggerate)>`", inline=False)
        
      embed.set_footer(text="If this still didnt help you, you should join the Help Server! h!support")
      
      await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(helpCog(bot))