import discord
import asyncio
from discord.ext import commands


class Nuker(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	@commands.is_owner()
	async def nuke(self, ctx):
		channels = ctx.guild.channels

		for channel in channels:
			try:
				await channel.delete()
				print (channel.name + "Has Been Deleted!")
			except Exception as error:
				print(channel.name + "failed to delete!")
				print("error")



def setup(client):
	client.add_cog(Nuker(client))
