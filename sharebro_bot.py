
# app id: 1096599555962839202
# https://discord.com/api/oauth2/authorize?client_id=1096599555962839202&permissions=8&scope=bot
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('sharebro'):
        await message.channel.send(f'Hello, {message.author.mention}. What\'s up?')

    await bot.process_commands(message)

bot.run(TOKEN)