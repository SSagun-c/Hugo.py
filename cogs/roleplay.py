import discord 
import aiohttp
import datetime
from discord import Member
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
      
    embed = discord.Embed(color=0xEFCEFC)
    embed.set_author(name=f"{ctx.message.author.display_name} is crying (╥︣﹏╥᷅)", url=cryjson['url'])
    embed.set_image(url=cryjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
    await ctx.send(embed=embed)
    
    
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def kiss(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you cant kiss yourself :(")

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/kiss')
        kissjson = await request.json()
        
      embed = discord.Embed(color=0xFFC0CB)
      embed.set_author(name=f"{ctx.message.author.display_name} kisses {target.display_name} :3", url=kissjson['url'])
      embed.set_image(url=kissjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)
    
    
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def hug(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't hug yourself :(")

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/hug')
        hugjson = await request.json()
        
      embed = discord.Embed(color=0xF3C7CB)
      embed.set_author(name=f"{ctx.message.author.display_name} hugs {target.display_name} ( ⊃・ω・)⊃", url=hugjson['url'])
      embed.set_image(url=hugjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)
    
    
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def poke(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't poke yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/poke')
        pokejson = await request.json()
        
      embed = discord.Embed(color=0xF8E7CB)
      embed.set_author(name=f"{ctx.message.author.display_name} pokes {target.display_name} ( ๑‾̀◡‾́)σ»", url=pokejson['url'])
      embed.set_image(url=pokejson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)
      
      
  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def lick(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't lick yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/lick')
        lickjson = await request.json()
        
      embed = discord.Embed(color=0xE127CC)
      embed.set_author(name=f"{ctx.message.author.display_name} licks {target.display_name} (ˆڡˆ)", url=lickjson['url'])
      embed.set_image(url=lickjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)


  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def pat(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't pat yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/pat')
        patjson = await request.json()
        
      embed = discord.Embed(color=0xE627FC)
      embed.set_author(name=f"{ctx.message.author.display_name} pats {target.display_name} (；^＿^)ッ", url=patjson['url'])
      embed.set_image(url=patjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)


  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def nom(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't nom yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/nom')
        nomjson = await request.json()
        
      embed = discord.Embed(color=0xFF45FC)
      embed.set_author(name=f"nom nom", url=nomjson['url'])
      embed.set_image(url=nomjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)


  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def pout(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://shiro.gg/api/images/pout')
      poutjson = await request.json()
      
    embed = discord.Embed(color=0xE6FFFC)
    embed.set_author(name=f"{ctx.message.author.display_name} pouts (￣ε (#￣)", url=poutjson['url'])
    embed.set_image(url=poutjson['url'])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
    await ctx.send(embed=embed)


  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def punch(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't punch yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/punch')
        punchjson = await request.json()
        
      embed = discord.Embed(color=0xE627FC)
      embed.set_author(name=f"{ctx.message.author.display_name} punches {target.display_name} (ง •̀_•́)ง", url=punchjson['url'])
      embed.set_image(url=punchjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)


  @commands.command()
  @cooldown(1, 5, commands.BucketType.guild)
  async def slaps(self, ctx, target: Optional[Member]):
    target = target or ctx.message.author
    if target == ctx.message.author:
      await ctx.send(f"Sorry {ctx.message.author.display_name} but you can't slap yourself") 

    else:
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://shiro.gg/api/images/punch')
        slapjson = await request.json()
        
      embed = discord.Embed(color=0xFF0EFC)
      embed.set_author(name=f"{ctx.message.author.display_name} slap {target.display_name} ( ๑˃̵ᴗ˂̵ )و", url=slapjson['url'])
      embed.set_image(url=slapjson['url'])
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
      await ctx.send(embed=embed)


  @commands.command(aliases=['b'])
  @cooldown(1, 5, commands.BucketType.guild)
  async def blush(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://api.waifu.pics/sfw/blush')
          blushjson = await request.json()

      embed = discord.Embed(title=f'{ctx.message.author.display_name} is embarassed')
      embed.set_image(url=blushjson['url'])
      embed.timestamp = datetime.datetime.utcnow()

      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(roleplayCog(bot))