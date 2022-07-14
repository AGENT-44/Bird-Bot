import discord
import asyncio
from discord import client
from discord import emoji
from discord import message
from discord.ext import commands
import requests


class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.command()
	async def whoisabot(self, ctx):
		await ctx.send('Hello')


	@commands.command(aliases=['inv'])
	async def invite(self, ctx):
		await ctx.send('https://discord.com/api/oauth2/authorize?client_id=740839083382669394&permissions=8&scope=bot')


	@commands.command()
	async def ping(self, ctx):
	
		a = round(self.client.latency * 1000)
		embed=discord.Embed(title="`Response Time Of The Bot!.`", description=f":satellite:\n **__{a}__** `ms`", color=0x1f8b4c)
		embed.set_author(name=ctx.author)
		message = await ctx.send(embed=embed)
		emoji = '\U0001f6f0'
		await message.add_reaction(emoji)
		


	@commands.command()
	async def hello(self, ctx):
		await ctx.send('Hello There')

	@commands.command()
	async def covid(self, ctx, *, countryName = None):
		try:
			if countryName is None:
				embed=discord.Embed(title=f"You Can Use This Command as:- ```#covid [countryname]```", colour=0x8b0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=embed)

			
			else:
				url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
				stats = requests.get(url)
				json_stats = stats.json()
				country = json_stats["country"]
				totalCases = json_stats["cases"]
				todayCases = json_stats["todayCases"]
				totalDeaths = json_stats["deaths"]
				todayDeaths = json_stats["todayDeaths"]
				recovered = json_stats["recovered"]
				active = json_stats["active"]
				critical = json_stats["critical"]
				casesPerOneMillion = json_stats["casesPerOneMillion"]
				deathsPerOneMillion = json_stats["deathsPerOneMillion"]
				totalTests = json_stats["totalTests"]
				testsPerOneMillion = json_stats["testsPerOneMillion"]

				embed2 = discord.Embed(title=f"**COVID-19 Stats For {country} :skull_crossbones:**!", description="This Information Isn't Live Always, Hence It May Not Be 100% Accurate!", colour=0x8b0000, timestamp=ctx.message.created_at)
				embed2.add_field(name="**TOTAL CASES**", value=totalCases, inline=True)
				embed2.add_field(name="**TODAY CASES**", value=todayCases, inline=True)
				embed2.add_field(name="**TOTAL DEATHS**", value=totalDeaths, inline=True)
				embed2.add_field(name="**TODAY DEATHS**", value=todayDeaths, inline=True)
				embed2.add_field(name="**RECOVERED**", value=recovered, inline=True)
				embed2.add_field(name="**ACTIVE CASES**", value=active, inline=True)
				embed2.add_field(name="**CRITICAL CASES**", value=critical, inline=True)
				embed2.add_field(name="**CASES PER ONE MILLION**", value=casesPerOneMillion, inline=True)
				embed2.add_field(name="**DEATHS PER ONE MILLION**", value=deathsPerOneMillion, inline=True)
				embed2.add_field(name="**TOTAL TESTS DONE**", value=totalTests, inline=True)
				embed2.add_field(name="**TESTS PER ONE MILLION**", value=testsPerOneMillion, inline=True)

				embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/744460555154096211/746444122252116128/Webp.net-resizeimage.png")
				await ctx.send(embed=embed2)

		except:
			embed3 = discord.Embed(title="Invalid Country Name Or API Error, Try Again Later...!", colour=0x32cd32, timestamp=ctx.message.created_at)
			embed3.set_author(name="ERROR!")
			await ctx.send(embed=embed3)
			


def setup(client):
	client.add_cog(Misc(client))