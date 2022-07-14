import discord
from discord.ext import commands

import asyncio

import random

import praw

import googletrans
from googletrans import Translator



class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client





	@commands.command()
	async def meme(self, ctx):

		reddit = praw.Reddit(client_id = "v4Hveux5PsqHfw",
					 	client_secret = "APk8LxNbARPvPOYlsayB5JV5TC8",
					 	username = "Agent_Gaming4411",
					 	password = "Vinay@123",
					 	user_agent = "Bird123")

		subreddit = reddit.subreddit("memes")
		all_sub = []


		top = subreddit.top(limit = 50)

		for submission in top:
			all_sub.append(submission)

		random_sub = random.choice(all_sub)

		name = random_sub.title
		url = random_sub.url

		em = discord.Embed(title = name)

		em.set_image(url = url)

		await ctx.send(embed= em)
		return

	@commands.command()
	async def askjinni(self, ctx, *, question):
		responses = ["It is certain.",
				 "It is decidedly so.",
				 "Without a doubt.",
				 "Yes - definitely.",
				 "You may rely on it.",
				 "As I see it, yes.",
				 "Most likely.",
				 "Outlook good.",
				 "Yes.",
				 "Signs point to yes.",
				 "Reply hazy, try again.",
				 "Ask again later.",
				 "Better not tell you now.",
				 "Cannot predict now.",
				 "Concentrate and ask again.",
				 "Don't count on it.",
				 "My reply is no.",
	  			 "My sources say no.",
				 "Outlook not so good.",
				 "Very doubtful."]
		await ctx.send(f'Question:{question}\nAnswer: {random.choice(responses)}')



	@commands.command()
	async def userinfo(self, ctx, member: discord.Member = None):
		member = ctx.author if not member else member
		roles = [role for role in member.roles]

		embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

		embed.add_field(name="ID:", value=member.id)
		embed.add_field(name="User_Name:", value=member.display_name)

		embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

		embed.add_field(name="Roles: ", value=" ".join([role.mention for role in roles]))
		embed.add_field(name="Top role:", value=member.top_role.mention)

		embed.add_field(name="Bot?", value=member.bot)

		await ctx.send(embed=embed)


	@commands.command()
	async def avatar(self, ctx, *, member : discord.Member = None):

		if member is None:
			embed = discord.Embed(title="You Can Use this Command Like This -> ```#avatar @member```", colour=0x306998, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return

		else:
			embed2 = discord.Embed(title=f"{member}'s Avatar!", colour=0x7fff00, timestamp=ctx.message.created_at)
			embed2.add_field(name="Animated?", value=member.is_avatar_animated())
			embed2.set_image(url=member.avatar_url)
			await ctx.send(embed=embed2)

	@commands.command()
	async def translate(self, ctx, lang, *, args):
		t = Translator()
		a = t.translate(args, dest=lang)

		embed = discord.Embed(colour=0x7fff00)
		embed.add_field(name='Translated', value=a.text, inline=False)
		await ctx.send(embed=embed)


	@commands.command()
	async def rolldice(self,ctx):
		await ctx.send (random.randint(1,6))


	@commands.command()
	async def servericon(self, ctx):
		icon_url = ctx.guild.icon_url
		await ctx.send(f"Guild Icon = {icon_url}")


def setup(client):
	client.add_cog(Fun(client))
