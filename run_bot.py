import os
import discord
from discord.ext import commands

from commands.dado.main import dice_handler

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!',intents = intents)

@bot.command()
async def dado(channel, sides = None): 
    responses = dice_handler(sides)
    responses[0] = f'{channel.author.display_name}: {responses[0]} <a:dice:997154628355510334>'
    for response in responses:
        await channel.send(response)

@bot.command()
async def comandos(channel):
    for key in bot.all_commands.keys():
        if key != 'help' and key!= 'comandos':
            await channel.send(f'!{key}')

bot.run(os.getenv('BOT_TOKEN'))