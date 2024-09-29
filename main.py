from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

bot = commands.Bot(command_prefix='<')

async def load_extensions():
    await bot.load_extension('cogs.new_disease')

@bot.event
async def on_ready():
    await load_extensions()
    print(f'{bot.user} has connected to Discord and is ready to be used!')

bot.run(os.getenv('BOT_TOKEN'))