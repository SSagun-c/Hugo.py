import discord
from discord.ext import commands


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
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