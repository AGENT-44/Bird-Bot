import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self,member):
        em = discord.Embed(title = "Welcome!", color = 0xfffff,description =f"{member.mention} Welcome To Server! \n**just joined The Server!** :Siren:")
        em.set_footer(text="Made By AGΣПƬ")
        em.set_thumbnail(url="https://cdn.discordapp.com/icons/703249428944781380/a_055079d4834ca3dc9a95fa9129e7e665.gif?size=1024")
        await self.client.get_channel(763459905955823646).send(embed=em)
        



def setup (client):
    client.add_cog(welcome(client))
