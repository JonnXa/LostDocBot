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

#getting all those keys
pComm = ""
cComm = ""
gComm = ""
wComm = ""
for k in answ["pages"]:
    pComm = pComm + k + ", "
for k in answ["class"]:
    cComm = cComm + k + ", "
for k in answ["guide"]:
    gComm = gComm + k + ", "
for k in answ["weeb"]:
    wComm = wComm + k + ", "



#loads config
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#setup listener
bot = commands.Bot(command_prefix='!')

@bot.command(name='git')
async def git(ctx):
    await ctx.send("https://github.com/JonnXa/LostDocBot")

#coin flip kek
@bot.command(name='flip', help="just do it\n do a flip")
async def coin_flip(ctx):
    response = random.choice(answ["flip"])
    await ctx.send(response)

#iterates all know pages
@bot.command(name='page', help="All usefull webpages:\n" + pComm)
async def page(ctx, *args):
    for arg in args:
        await ctx.send(answ["page"][arg])

#iterates all mentioned guides
@bot.command(name='guide', help="Query all possible guides als follows:\n" + gComm)
async def flow_chart(ctx, *args):
    for arg in args:
        await ctx.send(answ["guide"][arg])

#iterates all classes (just one tree yet)
@bot.command(name='class', help="Currently only German Guide for following classes:\n " + cComm )
async def all_classes(ctx, *args):
    for arg in args:
        await ctx.send(answ["class"][arg])

#iterates all stuff for cosmetics
@bot.command(name='weeb', help="All cosmetics and shit as follows:\n" + wComm)
async def weeb_shit_4_leo(ctx, *args):
    for arg in args:
        await ctx.send(answ["weeb"][arg])

#guide for setting up todo list for daily and weekly
@bot.command(name='todo', help="usefull todo list for daily and weekly shit")
async def todo(ctx):
    await ctx.send(answ["todo"]["link"])
    await ctx.send("Parse following string into " + answ["todo"]["import"] + " code -> paste")
    await ctx.send(file=discord.File('files/todo.txt'))

#server info
@bot.command(name='server')
async def serv(ctx):
    await ctx.send(answ["server"])

#binds bot to specific 'lost-ark' text channels
@bot.event
async def on_message(message):
    if message.channel.name == 'lostarkbot':
        await bot.process_commands(message)
        
#runs this shit
bot.run(TOKEN)
