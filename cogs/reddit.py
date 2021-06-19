import discord
import asyncpraw
import datetime
import random
import os
import redditeasy
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
        post = redditeasy.AsyncSubreddit(subreddit = subred,

                                        client_id = os.environ['RAI'],

                                        client_secret = os.environ['RAS'],

                                        username = os.environ['user'],

                                        password = os.environ['pass'],

                                        user_agent = 'SSagunPraw')


        postoutput = await post.get_post()


        embed = discord.Embed(title=f"{postoutput.title}", description=f"💬 {postoutput.comment_count}", url=postoutput.post_url, color=0xFF4500) 

        embed.set_author(name=postoutput.author)

        embed.set_image(url=postoutput.content)

        embed.set_footer(text=f"Created at {postoutput.created_at}")

        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)



    @commands.command(aliases=['wyr'])
    @cooldown(1, 8, commands.BucketType.user)
    async def wouldyourather(self, ctx):

        reddit = asyncpraw.Reddit(client_id = os.environ['RAI'],

                        client_secret = os.environ['RAS'],

                        username = os.environ['user'],

                        password = os.environ['pass'],

                        user_agent = 'SSagunPraw')


        subreddit = await reddit.subreddit("wouldyourather")
        all_subs = []


        top = subreddit.top(limit = None)


        async for submission in top:
            all_subs.append(submission)
        

        sub = random.choice(all_subs)


        author = sub.author
        name = sub.title

        embed = discord.Embed(title=name, color=0xFF4500)



        embed.set_author(name=author, icon_url='https://i.postimg.cc/pTzSdRqC/reddit-logo.png')


        embed.timestamp = datetime.datetime.utcnow()


        embed.set_footer(text="Would you rather....?")


        await ctx.send(embed=embed)

        
        
def setup(bot):
    bot.add_cog(redditCog(bot))