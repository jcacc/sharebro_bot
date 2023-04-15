import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
print(TOKEN)



intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# # Setting `Listening` status
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a really annoying song on repeat."))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('sharebro'):
        await message.channel.send(f'Hello, {message.author.mention}. What\'s up?')

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.content.startswith('!roll'):
        roll = message.content.split(' ')[1]
        try:
            rolls, limit = map(int, roll.split('d'))
            if rolls > 25:
                await message.channel.send('I can only roll up to 25 dice at once.')
                return
        except Exception:
            await message.channel.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await message.channel.send(result)


bot.run(TOKEN)

