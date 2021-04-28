import discord
from discord.ext import commands
import config
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


clientBot = discord.Client()
bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)




bot.run(config.TOKEN)
