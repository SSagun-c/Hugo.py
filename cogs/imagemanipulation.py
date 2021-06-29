import discord
from discord import Member
from io import BytesIO
from typing import Optional
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont


class imagemanipulationCog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

    
    @commands.command()
    async def simp(self, ctx, target: Optional[Member]):
        target = target or ctx.message.author
        simp = Image.open('./cogs/Images/simpcard.jpg')

        asset = target.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((285,269))

        simp.paste(pfp, (169,252))

        simp.save('./cogs/Images/psimp.jpg')

        await ctx.send(file=discord.File("./cogs/Images/psimp.jpg"))


    @commands.command()
    async def license(self, ctx, target: Optional[Member]):
        target = target or ctx.message.author
        lic = Image.open('./cogs/Images/license.jpg')

        usr = target.display_name

        draw = ImageDraw.Draw(lic)
        font = ImageFont.truetype('arial.ttf', 26)

        text = usr
        draw.text((456,105), text, (0,0,0), font=font)
        lic.save("./cogs/Images/plicense.jpg")

        await ctx.send(file=discord.File("./cogs/Images/plicense.jpg"))


    @commands.command()
    async def unoreverse(self, ctx, target: Optional[Member]):
        target = target or ctx.message.author
        simp = Image.open('./cogs/Images/unoreverse.jpg')

        asset = target.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((383,397))

        simp.paste(pfp, (845,155))

        simp.save('./cogs/Images/punoreverse.jpg')
        
        await ctx.send(f"{target.mention} Pulls the Uno Reverse card!!!")
        await ctx.send(file=discord.File("./cogs/Images/punoreverse.jpg"))


def setup(bot):
    bot.add_cog(imagemanipulationCog(bot))