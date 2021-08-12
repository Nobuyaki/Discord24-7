import discord, os, keep_alive, asyncio, datetime, pytz, random

from discord.ext import tasks, commands

client = commands.Bot(
  	command_prefix=':',
  	self_bot=True
)

@client.event
async def on_connect():
	await client.change_presence(activity=discord.Streaming(name="24/7 Stream", url="https://www.twitch.tv/Danish8409"))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ndx Aka Family"))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Tenshura Niki"))
	await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} server's"))

async def ch_pr():
 	await client.wait_until_ready()
 	statuses = [
 		f"In Night Raid Server's",
 		f"In {len(client.guilds)} Server's",
 		"Mobile Legends",
 		"Discord 24/7"]
 	while not client.is_closed():
   		status = random.choice(statuses)
   		await client.change_presence(activity=discord.Game(name=status))
   		await asyncio.sleep(5)
client.loop.create_task(ch_pr())

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
