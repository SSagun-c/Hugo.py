import discord
import aiohttp
import datetime
from discord.ext import commands
from discord.ext.commands import cooldown



class animeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['aq'])
    @cooldown(1, 5, commands.BucketType.guild)

    async def animequote(self, ctx):

        async with aiohttp.ClientSession() as Session:


            request = await Session.get('https://animechan.vercel.app/api/random')

            aqjson = await request.json()


        embed = discord.Embed(title=f"Anime: {aqjson['anime']}", description=f"Character: {aqjson['character']}", color=0xE0A899)

        embed.add_field(name="Quote", value=aqjson['quote'])


        await ctx.send(embed=embed)


    @commands.command(aliases=['anilist'])
    async def anime(self, ctx, *, animeName: str):

        api = 'https://graphql.anilist.co'
        query = '''
        query ($name: String){
          Media(search: $name, type: ANIME) {
            id
            idMal
            description
            title {
              romaji
              english
            }
            coverImage {
              large
            }
            startDate {
              year
              month
              day
            }
            endDate {
              year
              month
              day
            }
            synonyms
            format
            status
            episodes
            duration
            nextAiringEpisode {
              episode
            }
            averageScore
            meanScore
            source
            genres
            tags {
              name
            }
            studios(isMain: true) {
              nodes {
                name
              }
            }
            siteUrl
          }
        }
        '''
        variables = {
            'name': animeName
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(api, json={'query': query, 'variables': variables}, headers = self.bot.userAgentHeaders) as r:
                if r.status == 200:
                    json = await r.json()
                    data = json['data']['Media']

                    embed = discord.Embed(color=ctx.author.top_role.colour)
                    embed.set_footer(text='API provided by AniList.co | ID: {}'.format(str(data['id'])))
                    embed.set_thumbnail(url=data['coverImage']['large'])
                    if data['title']['english'] == None or data['title']['english'] == data['title']['romaji']:
                        embed.add_field(name='Title', value=data['title']['romaji'], inline=False)
                    else:
                        embed.add_field(name='Title', value='{} ({})'.format(data['title']['english'], data['title']['romaji']), inline=False)

                    
                    if data['synonyms'] != []:
                        embed.add_field(name='Synonymus', value=', '.join(data['synonyms']), inline=True)

                    embed.add_field(name='Typ', value=data['format'].replace('_', ' ').title().replace('Tv', 'TV'), inline=True)
                    if data['episodes'] > 1:
                        embed.add_field(name='Episodes', value='{} à {} min'.format(data['episodes'], data['duration']), inline=True)
                    else:
                        embed.add_field(name='Time', value=str(data['duration']) + ' min', inline=True)

                    embed.add_field(name='Started at', value='{}.{}.{}'.format(data['startDate']['day'], data['startDate']['month'], data['startDate']['year']), inline=True)
                    if data['endDate']['day'] == None:
                        embed.add_field(name='Released Episodes', value=data['nextAiringEpisode']['episode'] - 1, inline=True)
                    elif data['episodes'] > 1:
                        embed.add_field(name='Ended at', value='{}.{}.{}'.format(data['endDate']['day'], data['endDate']['month'], data['endDate']['year']), inline=True)

                    embed.add_field(name='Status', value=data['status'].replace('_', ' ').title(), inline=True)

                    try:
                        embed.add_field(name='Main Studio', value=data['studios']['nodes'][0]['name'], inline=True)
                    except IndexError:
                        pass
                    embed.add_field(name='Ø Score', value=data['averageScore'], inline=True)
                    embed.add_field(name='Genres', value=', '.join(data['genres']), inline=False)
                    tags = ''
                    for tag in data['tags']:
                        tags += tag['name'] + ', '
                    embed.add_field(name='Tags', value=tags[:-2], inline=False)
                    try:
                        embed.add_field(name='Adapted by', value=data['source'].replace('_', ' ').title(), inline=True)
                    except AttributeError:
                        pass

                    embed.add_field(name='AniList Link', value=data['siteUrl'], inline=False)
                    embed.add_field(name='MyAnimeList Link', value='https://myanimelist.net/anime/' + str(data['idMal']), inline=False)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send("Couldn't find your Anime!")




def setup(bot):
    bot.add_cog(animeCog(bot))