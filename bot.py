# bot.py
import os
import random
import json
import discord

from discord.ext import commands
from dotenv import load_dotenv

#opens json for all entries
f = open('list.json')
answ = json.load(f)

#loads config
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#setup listener
bot = commands.Bot(command_prefix='!')

#coin flip kek
@bot.command(name='flip')
async def coin_flip(ctx):
    response = random.choice(answ["flip"])
    await ctx.send(response)

#iterates all mentioned guides
@bot.command(name='guide')
async def flow_chart(ctx, *args):
    for arg in args:
        await ctx.send(answ["guide"][arg])

#iterates all classes (just one tree yet)
@bot.command(name='class')
async def all_classes(ctx, *args):
    for arg in args:
        await ctx.send(answ["class"][arg])

#iterates all stuff for cosmetics
@bot.command(name='weeb')
async def weeb_shit_4_leo(ctx, *args):
    for arg in args:
        await ctx.send(answ["weeb"][arg])

#guide for setting up todo list for daily and weekly
@bot.command(name='todo')
async def todo(ctx):
    await ctx.send(answ["todo"]["link"])
    await ctx.send("Parse follwoing string into " + answ["todo"]["import"] + " code -> paste")
    await ctx.send(file=discord.File('files/todo.txt'))

#server info
@bot.command(name='server')
async def serv(ctx):
    await ctx.send(answ["server"])

#binds bot to specific 'lost-ark' text channels
@bot.event
async def on_message(message):
    if message.channel.name == 'lost-ark':
        await bot.process_commands(message)
        
#runs this shit
bot.run(TOKEN)