import discord
from discord

intents = discord.Intents.default()
intents.members = True

@bot.event
async def on_ready():
    print(f'{bot.user}')

bot.run('TOKEN')
