import discord
from discord.ext import commands
import json

class Admins(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		

		for ban_entry in banned_users:
			user = ban_entry.user
		if user == None:
			await ctx.send("`Enter username#descriminator To Unban Someone")
		else:
			await ctx.send("You Don't Have Permissions To Unban.")
		member_name, memeber_discriminator = member.split('#')
		if (user.name, user.discriminator) == (member_name, memeber_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f"{user} has been unbanned!")
			return



	@commands.command(aliases=['b'])
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx,member : discord.Member = None,*,reason= "No Reason Given"):
		if member == None:
			await ctx.send("`Mention User To Ban`")
		
		else:
			await ctx.send("You don't have Permission To Ban Someone.")
			return

		await ctx.send(member.name + " Has Been Banned From the AG3NT's Server, Reason: "+reason)
		await member.ban(reason=reason)



	@commands.command()
	@commands.has_permissions(administrator=True)
	async def changeprefix(self, ctx, prefix):
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		prefixes[str(ctx.guild.id)] = prefix

		with open('prefixes.json', 'w') as f:
			json.dump(prefixes, f)
		await ctx.send(f"prefix is now '{prefix}'!")




	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		prefixes[str(guild.id)] = '#'

		with open('prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=4)


	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		prefixes.pop(str(guild.id))

		with open('prefixes.json', 'w') as f:
			json.dump(prefixes, f)



def setup(client):
	client.add_cog(Admins(client))
