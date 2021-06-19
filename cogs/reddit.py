import discord
import asyncpraw
import datetime
import random
import os
from discord.ext import commands
from discord.ext.commands import cooldown

class redditCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    REDDIT_APP_ID = os.getenv("RAI")
    REDDIT_APP_SECRET = os.getenv("RAS")
    USERNAME = os.getenv("user")
    PASSWORD = os.getenv("pass")

    reddit = asyncpraw.Reddit(client_id = os.environ['RAI'],
                        client_secret = os.environ['RAS'],
                        username = os.environ['user'],
                        password = os.environ['pass'],
                        user_agent = 'SSagunPraw')

    @commands.command(name=('reddit'), aliases=['r'])
    @cooldown(1, 8, commands.BucketType.user)
    async def _reddit(self, ctx, subred = "meme"):  # default subreddit is meme
        reddit = asyncpraw.Reddit(client_id = os.environ['RAI'],
                        client_secret = os.environ['RAS'],
                        username = os.environ['user'],
                        password = os.environ['pass'],
                        user_agent = 'SSagunPraw')

        subreddit = await reddit.subreddit(subred)
        all_subs = []

        top = subreddit.top(limit = 75)

        async for submission in top:
            all_subs.append(submission)
        
        random_sub = random.choice(all_subs)

        if submission.over_18 == True:
            await ctx.send("Sorry but this subreddit is marked as NSFW!")
        else: 
            sr_name = random_sub.subreddit
            author = random_sub.author
            name = random_sub.title
            url = random_sub.url

            embed = discord.Embed(title=author, description=name, color=0xFF4500)
            embed.set_author(name=f'r/{sr_name}',url=url, icon_url='https://i.postimg.cc/pTzSdRqC/reddit-logo.png')
            embed.set_image(url=url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"If the Image is not loading just click on r/{sr_name}!")
            await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(redditCog(bot))