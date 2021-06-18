import discord
from discord.ext import commands



class configCog(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, prefix=None):

        data = await self.bot.prefixes.find(ctx.guild.id)

        if data is None or "prefix" not in data:

            data = {"_id": ctx.guild.id, "prefix": prefix}

        data["prefix"] = prefix

        await self.bot.prefixes.upsert(data)

        await ctx.send(f"Succesfully changed the prefix to `{prefix}`")

    
    @commands.command()
    @commands.has_permissions(managae_guild=True)
    async def clearprefix(self, ctx):
        
        await self.bot.prefixes.unset({"_id": ctx.guild.id, "prefix": 1})

        await ctx.send("The servers prefix has been set to default. `h!`")



def setup(bot):
    bot.add_cog(configCog(bot))