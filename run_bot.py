import os
import discord
from discord.ext import commands

from commands.dado.Dado import Dado


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!',intents = intents)

@bot.command()
async def dado(context, sides): 
    dado = Dado(context, sides)
    response_message = dado.roll()
    await context.send(response_message)
    if(dado.gif):
        await context.send(dado.gif)

bot.run(os.getenv('BOT_TOKEN'))