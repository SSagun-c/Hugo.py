import discord
import datetime
import aiohttp
from discord import Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def waifu(self, ctx):
        """
        I love anime girls
        """
        async with aiohttp.ClientSession() as Ses:
            request = await Ses.get("https://api.waifu.pics/sfw/waifu")
            waifujson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"I Love Anime Girls", url=waifujson['url'])
        embed.set_image(url=waifujson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def neko(self, ctx):
        """
        I love anime girls
        """
        async with aiohttp.ClientSession() as Ses:
            request = await Ses.get("https://api.waifu.pics/sfw/neko")
            nekojson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"Nekomimi", url=nekojson['url'])
        embed.set_image(url=nekojson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def shinobu(self, ctx):
        """
        I love anime girls
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/shinobu")
            shinobujson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"Girls in their own World", url=shinobujson['url'])
        embed.set_image(url=shinobujson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def bully(self, ctx, target: Optional[Member]):
        """
        Tons of API requests :grief:
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Get bullied {ctx.message.author.display_name} teehee~"
        else:
            title = f"{ctx.message.author.display_name} bullys {target.display_name}"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/bully")
            bullyjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=bullyjson['url'])
        embed.set_image(url=bullyjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def cuddle(self, ctx, target: Optional[Member]):
        """
        i can do this simpler but im stupid
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Awww {ctx.message.author.display_name} cuddles with me~"
        else:
            title = f"{ctx.message.author.display_name} cuddles with {target.display_name} OwO"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/cuddle")
            cuddlejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=cuddlejson['url'])
        embed.set_image(url=cuddlejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def cry(self, ctx):
        """
        sad
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/cry")
            cryjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} cries (╥︣﹏╥᷅)", url=cryjson['url'])
        embed.set_image(url=cryjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def hug(self, ctx, target: Optional[Member]):
        """
        i can do this simpler but im stupid
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Here is a hug for you {ctx.message.author.display_name} ( ⊃・ω・)⊃"
        else:
            title = f"{ctx.message.author.display_name} hugs {target.display_name} how cute~"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/hug")
            hugjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=hugjson['url'])
        embed.set_image(url=hugjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def awoo(self, ctx):
        """
        I love wolf girls
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/awoo")
            awoojson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name="We love Wolfgirls awoo~", url=awoojson['url'])
        embed.set_image(url=awoojson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def kiss(self, ctx, target: Optional[Member]):
        """
        i can do this simpler but im stupid
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Here's a kiss :3 {ctx.message.author.display_name}"
        else:
            title = f"{ctx.message.author.display_name} kisses {target.display_name} :3"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/kiss")
            kissjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=kissjson['url'])
        embed.set_image(url=kissjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def lick(self, ctx, target: Optional[Member]):
        """
        i can do this simpler but im stupid
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Got you hehe {ctx.message.author.display_name}"
        else:
            title = f"{ctx.message.author.display_name} licks {target.display_name} teehee~"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/lick")
            lickjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=lickjson['url'])
        embed.set_image(url=lickjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def pat(self, ctx, target: Optional[Member]):
        """
        please someone pat me
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Here's a pat for you owo {ctx.message.author.display_name}"
        else:
            title = f"{ctx.message.author.display_name} pats {target.display_name} mmmh comfy.."
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/pat")
            patjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=patjson['url'])
        embed.set_image(url=patjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def cuddle(self, ctx):
        """
        i can do this simpler but im stupid
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/smug")
            cuddlejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} smugs, I know what you are on hehe ¬‿¬", url=cuddlejson['url'])
        embed.set_image(url=cuddlejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def bonk(self, ctx, target: Optional[Member]):
        """
        bonk
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"{ctx.message.author.display_name} BONK"
        else:
            title = f"{ctx.message.author.display_name} bonks {target.display_name} Itai! Ouch!"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/bonk")
            bonkjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=bonkjson['url'])
        embed.set_image(url=bonkjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def yeet(self, ctx, target: Optional[Member]):
        """
        yeet go go go
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Get your Helmet {ctx.message.author.display_name}"
        else:
            title = f"{ctx.message.author.display_name} yeets {target.display_name} weeeeeeee"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/yeet")
            yeetjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=yeetjson['url'])
        embed.set_image(url=yeetjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def blush(self, ctx):
        """
        Its not like I like you or anything!!! baka!
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/blush")
            blushjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} blushes, Its not like I like your or anything b-baka!", url=blushjson['url'])
        embed.set_image(url=blushjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def smile(self, ctx):
        """
        keep smiling :) (telling this to myself) 
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/smile")
            smilejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} smiles (* ^ ω ^)", url=smilejson['url'])
        embed.set_image(url=smilejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def wave(self, ctx):
        """
        Bye Bye, Mata ne o7
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/wave")
            wavejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} is waving o/", url=wavejson['url'])
        embed.set_image(url=wavejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def highfive(self, ctx, target: Optional[Member]):
        """
        highfive YO
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Highfive! {ctx.message.author.display_name}"
        else:
            title = f"{ctx.message.author.display_name} highfives {target.display_name}"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/highfive")
            hfjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=hfjson['url'])
        embed.set_image(url=hfjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def handhold(self, ctx, target: Optional[Member]):
        """
        holding hands is cute
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"{ctx.message.author.display_name} Holds my hand, WOAH >///<"
        else:
            title = f"{ctx.message.author.display_name} holds {target.display_name} hands, so cute òwó"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/handhold")
            hhjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=hhjson['url'])
        embed.set_image(url=hhjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def nom(self, ctx):
        """
        nom nom oishiiii!
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/nom")
            nomjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} noms, nom nom", url=nomjson['url'])
        embed.set_image(url=nomjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def bite(self, ctx, target: Optional[Member]):
        """
        ouch
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Ouch! {ctx.message.author.display_name} what are you doing, that hurt!"
        else:
            title = f"{ctx.message.author.display_name} bites {target.display_name}, that must've hurt!"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/bite")
            bitejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=bitejson['url'])
        embed.set_image(url=bitejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def glomp(self, ctx, target: Optional[Member]):
        """
        glomp? whats this
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Glad to see you again {ctx.message.author.display_name}!"
        else:
            title = f"{ctx.message.author.display_name} really is glad to see you again {target.display_name} "
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/glomp")
            glompjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=glompjson['url'])
        embed.set_image(url=glompjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def slap(self, ctx, target: Optional[Member]):
        """
        bamm
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"{ctx.message.author.display_name} WHAT WAS THAT FOR?"
        else:
            title = f"{ctx.message.author.display_name} slaps {target.display_name} uh-oh"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/slap")
            slapjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=slapjson['url'])
        embed.set_image(url=slapjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def kill(self, ctx, target: Optional[Member]):
        """
        911 yes hello this man right here
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"{ctx.message.author.display_name} oh, I'm die thank you forever"
        else:
            title = f"{ctx.message.author.display_name} kills {target.display_name}, better hide the body "
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/kill")
            killjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=killjson['url'])
        embed.set_image(url=killjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def kick(self, ctx, target: Optional[Member]):
        """
        karate
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"Bring it on {ctx.message.author.display_name}! >:)"
        else:
            title = f"{ctx.message.author.display_name} kicks {target.display_name}, wow what a kick!!!"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/kick")
            kickjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=kickjson['url'])
        embed.set_image(url=kickjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def happy(self, ctx, target: Optional[Member]):
        """
        stay happy
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/happy")
            happyjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} is happy（‐＾▽＾‐）", url=happyjson['url'])
        embed.set_image(url=happyjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def wink(self, ctx):
        """
        wink wink
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/wink")
            winkjson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} winks to you ;)", url=winkjson['url'])
        embed.set_image(url=winkjson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def poke(self, ctx, target: Optional[Member]):
        """
        poking uwu
        """
        target = target or ctx.message.author
        if target == ctx.message.author:
            title = f"I poke {ctx.message.author.display_name} ( ๑‾̀◡‾́)σ»"
        else:
            title = f"{ctx.message.author.display_name} pokes {target.display_name}, heeee leave me aloneee"
        
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/poke")
            pokejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=title, url=pokejson['url'])
        embed.set_image(url=pokejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def dance(self, ctx, target: Optional[Member]):
        """
        LETS DANCE
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/dance")
            dancejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name=f"{ctx.message.author.display_name} is dancing, cheer them on o7", url=dancejson['url'])
        embed.set_image(url=dancejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def cringe(self, ctx, target: Optional[Member]):
        """
        oh nooo cringe (spanish accent)
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get("https://api.waifu.pics/sfw/cringe")
            cringejson = await request.json()
            
        embed = discord.Embed(color=0xED61D3)
        embed.set_author(name="Oh hecks nah that was cringe ( >︹<)", url=cringejson['url'])
        embed.set_image(url=cringejson['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author.display_name}")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(images(bot))