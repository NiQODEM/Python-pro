import discord
from discord.ext import commands
import random
import os
import requests
from password_generator import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

@bot.command()
async def emoji(ctx):
    emoji = gen_emodji()
    await ctx.send(emoji)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def haslo(ctx, ilosc = 5):
    hasslo = gen_pass(ilosc)
    await ctx.send(f'twoje hasło: {hasslo}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):

    memy = os.listdir('images')
    mem = random.choice(memy)

    with open(f'images/{mem}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def oznacz(ctx, kto = "", ile = 2):
    for i in range(ile):
        await ctx.send(kto)

@bot.command()
async def pomocy(ctx):
    await ctx.send(f'lista komend(prefix - $):\nemoji\nhello\nhaslo(ilośc znaków)\nheh(ilolśc powtórzeń)\nmem\nduck\noznacz(kto np. @DMS NIQODEM, ile razy oznaczyć)')

bot.run("TOKEN")
