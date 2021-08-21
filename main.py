import discord, os, keep_alive, asyncio, datetime, random
from discord.ext import tasks, commands

client = commands.Bot(command_prefix="n!", case_insensitive=True, self_bot=True)

@client.event
async def ch_pr():
 	await client.wait_until_ready()
#presence
 	game = [
 		"Mobile Legends", 
 		"Valorant",
 		"Clash Of Clan",
 		"PointBlank"
 	]
 	anime = [
 		"Tenshura Nikki S2",
 		"Vanitas No Carte",
 		"Boku No Hero S5",
 		"Fumetsu No Anata"
 	]
 	music = [
 		"YOASOBI - 夜に駆ける", 
 		"TUYU-compared Child",
 		"Ndx-Angin Dalu"
 	]
 	while not client.is_closed():
   		status1 = random.choice(game)
   		status2 = random.choice(anime)
   		status3 = random.choice(music)
   		
   		#playing presence{(status1)}
   		await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status1, type=3))
   		await asyncio.sleep(10)
   		
   		#watching presence{(status2)}
   		await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=status2))
   		await asyncio.sleep(10)
   		
   		#listening presence{(status3)}
   		await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=status3))
   		await asyncio.sleep(10)
client.loop.create_task(ch_pr())

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
