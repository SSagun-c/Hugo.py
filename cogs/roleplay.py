import discord 
import aiohttp
import datetime
from typing import Optional
from discord.ext import commands
from discord.ext.commands import cooldown

class roleplayCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
 
  @commands.commands()
  @cooldown(1, 5, commands.BucketType.guild)
  async def cry(self, ctx, target: Optional[Member]):
    
    target = target or ctx.message.author
    
    async with aiohttp.ClientSession() as session:
      request = await session.get("https://shiro.gg/api/images/cry")
      cryjson = await request.json()
      
    embes = discord.Embed()
    embed.set_author(name=f"{target.display_name} is crying T_T", url=cryjson['url'])
    embed.set_image(url=cryjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {target.display_name"})
    await ctx.send(embed=embed)