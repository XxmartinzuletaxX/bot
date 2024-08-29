import discord
import random
from bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi')

@bot.command()
async def bye(ctx):
    await ctx.send('🙁') 

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))
    

    
bot.run("MTI3NTk3ODI1MTU4MzM1Njk2OA.GglnaT.9Jrz0gSjeQWWgcspdLBTKDWnqXq-Un-5Xg3WJ0")


