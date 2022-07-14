import discord
import json
import random
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
from discord.flags import Intents

import praw

import os


def get_prefix(client, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]


intents = discord.Intents.all()
client = commands.Bot(command_prefix = get_prefix, intents = discord.Intents.all())
client.remove_command('help')

TOKEN = open("TOKEN.txt", "r").read()



for cog in os.listdir("cogs"):
	if cog.endswith(".py"):
		try:
			cog = f"cogs.{cog.replace('.py', '')}"
			client.load_extension(cog)

		except Exception as e:
			print(f"{cog} cannot be loaded!")
			raise e

client.run(TOKEN)