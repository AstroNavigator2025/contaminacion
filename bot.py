import discord
from discord.ext import commands
from dotenv import load_dotenv
import main,os

load_dotenv()
token= os.getenv("MTQzOTI3MDc1OTgxNzI4MTYyNw.GQpIUU.8spJNuBhZrHQbYunJMbkxEUx87yRZUQvNwAEUo")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name="psw")
async def generate_psw(ctx,leight=25):
    password= main.create_pasword(leight)
    await ctx.send(f"Contraseña Generada: {password}")
    
@bot.command(name="meme")
async def mem(ctx):
    with open("IMG/Meme1.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command(name="etiqueta")
async def eco(ctx):
    etiquet = main.etiqueta_eco()
    await ctx.send(embed=etiquet)
    
bot.run(token)