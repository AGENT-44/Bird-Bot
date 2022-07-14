import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle 



class Events(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_ready(self):
		print('Hello Your Bot is Ready!')
		while True:
			await self.client.change_presence(activity=discord.Game("#help!"))
			await asyncio.sleep(10)
			await self.client.change_presence(activity=discord.Game("Under Development"))
			await asyncio.sleep(10)


		

	


def setup(client):
	client.add_cog(Events(client))