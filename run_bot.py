import os
import discord
from time import sleep
from discord.ext import commands

from commands.dado.main import roll_dice

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!',intents = intents)

@bot.command()
async def dado(channel, sides = None):
    await channel.send(roll_dice(sides))

@bot.command()
async def comandos(channel):
    for key in bot.all_commands.keys():
        if key != 'help' and key!= 'comandos':
            await channel.send(key)

bot.run(os.getenv('token'))