import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludo(ctx, nombre:str):
    await ctx.send(f'Hola {nombre} Bienvenido al servidor!')

@bot.command()
async def suma(ctx, numero1:int,numero2:int):
    await ctx.send(f"El Resultado de la suma es: {numero1 + numero2}")

@bot.command()
async def multi(ctx, numero1:int,numero2:int):
    await ctx.send(f"El Resultado de la multiplicacion es: {numero1 * numero2}")

@bot.command()
async def resta(ctx, numero1:int,numero2:int):
    await ctx.send(f"El Resultado de la resta es: {numero1 - numero2}")

bot.run("")
