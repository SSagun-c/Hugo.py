import discord 
import aiohttp
import datetime
from typing import Optional
from discord.ext import commands
from discord.ext.commands import cooldown

class roleplayCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
 
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def cry(self, ctx):
    
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://shiro.gg/api/images/cry')
      cryjson = await request.json()
      
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.message.author.display_name} is crying T_T", url=cryjson['url'])
    embed.set_image(url=cryjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
    await ctx.send(embed=embed)
    
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def kiss(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://shiro.gg/api/images/kiss')
      kissjson = await request.json()
      
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.message.author.display_name} kisses {target.display_name} :3", url=kissjson['url'])
    embed.set_image(url=kissjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
    await ctx.send(embed=embed)
    
    
def setup(bot):
  bot.add_cog(roleplayCog(bot))