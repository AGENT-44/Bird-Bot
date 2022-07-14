import discord
from discord.ext import commands
import asyncio

class help(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.client.remove_command('help')

	@commands.command(pass_context=True)
	async def help(self, ctx):

		
		embed = discord.Embed(title='***Commands For Bird Bot!***', description='This is the Commands for Bird Bot.', colour=0x7fff00)
		embed.add_field(name='avatar:', value="Give's you avatar of mentioned user!.")
		embed.add_field(name='askjinni:', value="Askjinni Your Questions. 'Example- #askjinni is Riuu a bot?", inline=False)
		embed.add_field(name='ban:', value="Only for Admins.", inline=False)
		embed.add_field(name='clear:', value="Clear Text's in Channel.", inline=False)
		embed.add_field(name='changeprefix:', value="Only For Admins Change Bot's Prefix.", inline=False)
		embed.add_field(name='covid:', value="Use #covid [country name or world] for Covid-19's Stats Across the World.", inline=False)
		embed.add_field(name='hello:', value="Send's Back a Hello.", inline=False)
		embed.add_field(name='help:', value="Show's this message!", inline=False)
		embed.add_field(name='invite:', value="Give's You Link to Invite this Bot in Your Own Server.", inline=False)
		embed.add_field(name='kick:', value="Only For Moderator's And Admins Kick's specific Person From the server!", inline=False)
		embed.add_field(name='load:', value="Admins Only!", inline=False)
		embed.add_field(name='meme:', value="Get MEME's From Reddit.", inline=False)
		embed.add_field(name='nuke:', value="Most Dangerous Command Only Server Owner's Can use This. Clear's Your Whole Server!", inline=False)
		embed.add_field(name='ping:', value="Tell's You Bot Response Time in 'MS'.", inline=False)
		embed.add_field(name='server_url', value="***Give's You Server URL (command used in)***", inline=False)
		embed.add_field(name='translate:', value="Work's as Google Translator 'do #translate [lang] [text]..' ", inline=False)
		embed.add_field(name='unban:', value="Only For Admin's Unban Users!", inline=False)
		embed.add_field(name='unload:', value="Admin's Only.", inline=False)
		embed.add_field(name='userinfo:', value="Get Specific User's Info!")


		await ctx.send(embed=embed)





def setup(client):
	client.add_cog(help(client))

