import discord
import asyncio
from discord.ext import commands


class unload(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, module_name = None):

        try:
            if module_name is None:
                embed = discord.Embed(title="Enter Module Name To Unload!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)

            else:
                self.client.unload_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title=f"{module_name}Module Unloaded Successfully!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title=f"Module Failed To Unload {module_name} Module!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)   


def setup(client):
    client.add_cog(unload(client)) 