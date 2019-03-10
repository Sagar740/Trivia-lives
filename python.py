import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import time
discord.__version__
'1.0.0a'
 
bot = commands.Bot(command_prefix='.')
 
@bot.event
async def on_ready():
    print ('I am online.')
    print('I am running as ' + bot.user.name+',''with the ID:' + bot.user.id+' and I am connected in '+str(len(bot.servers))+' servers.'' I am connected with '+str(len(set(bot.get_all_members())))+' members')
 
 
 
bot.run("NTM3MjExOTMwMDY3MzM3MjE2.D2Z-TA.IxTLnCBGSUUc3aUZwmg3QdV1oe8")
