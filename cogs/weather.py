import discord
import aiohttp
import datetime as dt
from discord import Embed
from discord.ext import commands
from discord.ext.commands import cooldown
from discord.ext.commands.cooldowns import BucketType

class weatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="weather -metric", aliases=['weather', 'weather -met', 'weather -m'])
    @cooldown(1, 10, commands.BucketType.user)
    async def weather_m(self, ctx, *, city_name):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=08c3bc9d0b3e4eb229d9a271bebb05ef&units=metric")
            weatherjson = await request.json()

        embed = discord.Embed(title=weatherjson['name'], description=f"{weatherjson['weather'][0]['description']}\nLocated in: {weatherjson['sys']['country']}", colour=0xEEEFFF)
        embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{weatherjson['weather'][0]['icon']}@2x.png")
        embed.add_field(name=f"Temperature {weatherjson['main']['temp']}°C", value=f"Feels Like {weatherjson['main']['feels_like']}°C\nMinimum Temperature {weatherjson['main']['temp_min']}°C\nMaximum Temperature {weatherjson['main']['temp_max']}°C\nPressure {weatherjson['main']['pressure']}PA\nHumidity {weatherjson['main']['humidity']}%", inline=False)
        embed.add_field(name="Wind", value=f"Speeds {weatherjson['wind']['speed']}kmh", inline=False)
        embed.timestamp = dt.datetime.utcnow()
        embed.set_footer(text="Showing in Metric")

        await ctx.send(embed=embed)

    @commands.command(name="weather -imperial", aliases=['weather -imp', 'weather -i'])
    @cooldown(1, 10, commands.BucketType.user)
    async def weather_i(self, ctx, *, city_name):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=08c3bc9d0b3e4eb229d9a271bebb05ef&units=metric")
            weatherjson = await request.json()

        embed = discord.Embed(title=weatherjson['name'], description=f"{weatherjson['weather'][0]['description']}\nLocated in: {weatherjson['sys']['country']}", colour=0xFFFEEE)
        embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{weatherjson['weather'][0]['icon']}@2x.png")
        embed.add_field(name=f"Temperature {weatherjson['main']['temp']}°F", value=f"Feels Like {weatherjson['main']['feels_like']}°F\nMinimum Temperature {weatherjson['main']['temp_min']}°F\nMaximum Temperature {weatherjson['main']['temp_max']}°F\nPressure {weatherjson['main']['pressure']}PA\nHumidity {weatherjson['main']['humidity']}%", inline=False)
        embed.add_field(name="Wind", value=f"Speeds {weatherjson['wind']['speed']}mph", inline=False)
        embed.timestamp = dt.datetime.utcnow()
        embed.set_footer(text="Showing in Imperial")

        await ctx.send(embed=embed)


    
def setup(bot):
    bot.add_cog(weatherCog(bot))