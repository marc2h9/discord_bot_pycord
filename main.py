import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online")

@bot.command(description="Sends bot latency")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {round(bot.latency)}ms")

# starting bot
bot.run(os.getenv('TOKEN'))
