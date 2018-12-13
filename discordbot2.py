import discord
from discord.ext import commands 
from discord.ext.commands import bot
import asyncio
import random
import json

#above this comment is all the IMPORT garbage. 

#try:
 #   configDict = json.load(open('config.json'))
#except Exception as e:
 #   configDict = {}

#configDict = json.load(open('config.json'))



bot = commands.Bot(command_prefix='!')

#just a fun little start up message here, bot.user.name giving you the name of the bot and then followed by bot.user.id giving you the id of the bot.

@bot.event
async def on_ready():
	print("I'm afraid I can do that Dave")
	print(bot.user.name)
	print(bot.user.id)

#add to file function, this is what creates the log file that keeps all the messages sent while the bot is active
def add_to_file(filename,text):
	with open(filename, 'a') as file:
		file.write(text)


#this event here is what is logging all the messages on the bot. 
@bot.event
async def on_message(message):
	print(message.author.name, message.content)
	await bot.process_commands(message)
	add_to_file('file.txt',message.content)

#simple ping command sending back pong, useful to make sure the bot is working and in the server

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("Pong!")


#fun little boot command, kicks people from the server with a message saying Later nerd! 
@bot.command(pass_context=True)
async def boot(ctx, user: discord.Member):
	await bot.say('Later Nerd!   {}    '.format(user.name))
	await bot.kick(user)



#choose command, hungry and cant decide what to eat? want to find a color and dont what to have to pick yourself? use this! will pick a random string you enter, works like !choose 1 2 and will pick one of those. 

@bot.command()
async def choose(*choices: str):
	await bot.say(random.choice(choices))





#here you are going to want to put your server ID so the bot can join it. 

#bot.run(configDict["discord_id"])
bot.run("NTIyMDc4ODY4NTY0MjEzNzcy.DvRyQA.bZFzIViVfGDG38AtVTE8gKKE5MQ")

