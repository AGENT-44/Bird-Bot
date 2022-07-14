import discord
import asyncio
from discord.ext import commands



class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client




	@commands.command(aliases=['k'])
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx,member : discord.Member,*,reason= "No Reason Given"):
		await ctx.send(member.name + " Has Been Kicked From the AG3NT's Server, Reason: "+reason)
		await member.kick(reason=reason)

	

def setup(client):
	client.add_cog(Moderation(client))