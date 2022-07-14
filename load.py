import discord
import asyncio
from discord.ext import commands

class load(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, module_name = None):

        try:
            if module_name is None:
                embed = discord.Embed(title="Enter Module Name To Load!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)

            else:
                self.client.load_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title=f"{module_name}Module Loaded Successfully!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title=f"Module Failed To Load {module_name} Module!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)    


def setup(client):
    client.add_cog(load(client))