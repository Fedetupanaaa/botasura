import discord
import os
import random
from discord.ext import commands
import time
import requests
from botasura_logic import gen_eco
from botasura_logic import gen_consejo


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'entramos como: {bot.user}')

@bot.command()
async def eco(ctx):
    await ctx.send(f" {gen_eco()}")

@bot.command()
async def consejo(ctx):
    await ctx.send(f" {gen_consejo()}")



bot.run("")
