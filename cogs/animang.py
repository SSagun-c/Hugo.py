from attr import field
import discord
import kitsu
from discord.ext import commands


client = kitsu.Client()

class animangCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def anime(self, ctx, *, aniname):
        entries = await client.search('anime', aniname)
        if not entries:
            embed = discord.Embed(title="❌ Nothing Found!")
            await ctx.send(embed=embed)
        
        else:
        
            for anime in enumerate(entries, 1):
                embed = discord.Embed(title=f"Results for {anime.title}")
                fields = [
                            'Sub-Type', anime.subtype, False,

                            'Status', anime.status, False,

                            'Sypnosis', anime.sypnosis, False,

                            'Episodes', anime.episode_count, False,

                            'Age Rating', anime.age_rating_guide, False,

                            'Popularity', anime.popularity_rank, False,

                            'Rating', anime.rating_rank, False  
                        
                        ]


                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

            if anime.started_at:

                embed.add_field(name='Started', value=anime.started_at.strftime('%Y/%m/%d'))

            if anime.ended_at:

                embed.add_field(name="Ended", value=anime.ended_at.strftime('%Y/%m/%d'))
                

            streaming_links = await client.fetch_anime_streaming_links(anime)

            if streaming_links:

                for link in streaming_links:

                    embed.add_field(name="Streaming Links", value=f'[{link.title}]({link.url})')

            embed.add_field(name="Kitsu Page", value=anime.url)

            await ctx.send(embed=embed)

                
def setup(bot):
    bot.add_cog(animangCog(bot))